"""The app module, containing the app factory function."""

import os
from flask import Flask, url_for, request, redirect

# Import extensions
from project.extensions import (
    db,
    migrate,
    mail,
    csrf_protect,
)

# Import blueprints
from project.blueprints.public import public
from project.blueprints.users import users
from project.blueprints.main import main

# Import models for extension configuration
from project.blueprints.users.models import User, UserEmail, Role, UserRoles

# Import extensions requiring special setup
from flask_user import UserManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Import extensions to support special setup
from flask_user import current_user, roles_required
import datetime


def create_app():
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    # If an environment variable has been set to production,
    # configure from the instance folder
    if os.environ.get('ENV') == 'prod':
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_pyfile('config.py', silent=True)
    # Else, configure from standard config.py
    else:
        app = Flask(__name__, instance_relative_config=False)
        app.config.from_pyfile('../config.py')

    register_extensions(app)
    register_blueprints(app)

    """
    register_errorhandlers(app)
    register_shellcontext(app)
    """
    # register_commands(app)

    return app


def register_extensions(app):
    """Initialize Flask extensions."""
    # Flask-SQLAlchemy
    db.init_app(app)
    # Flask-Migrate
    migrate.init_app(app, db)
    # Flask-User
    user_manager = UserManager(app, db, User, UserEmailClass=UserEmail)
    # Flask-Admin
    admin = Admin(app, name='Admin Dashboard', template_mode='bootstrap3')
    # Flask_Admin: Create custom model view class

    class RestrictedModelView(ModelView):
        # Display primary keys
        column_display_pk = True
        # Hide admin pages by overwriting Flask-Admin's is_accessible function

        def is_accessible(self):
            if not current_user.is_authenticated:
                return False
            return current_user.has_roles('admin')
        """
        # Redirect to a page if the user doesn't have access
        def inaccessible_callback(self, name, **kwargs):
            # redirect to login page if user doesn't have access
            return redirect(url_for('user.register', next=request.url))"""
    # Flask-Admin: Add views
    admin.add_view(RestrictedModelView(User, db.session))
    admin.add_view(RestrictedModelView(UserEmail, db.session))
    admin.add_view(RestrictedModelView(Role, db.session))
    admin.add_view(RestrictedModelView(UserRoles, db.session))
    # Flask-Admin: Protect admin page

    @app.before_first_request
    def restrict_admin_url():
        endpoint = 'admin.index'
        url = url_for(endpoint)
        admin_index = app.view_functions.pop(endpoint)

        @app.route(url, endpoint=endpoint)
        @roles_required('admin')
        def secure_admin_index():
            return admin_index()
    # Flask-Mail
    mail.init_app(app)
    # Flask-WTF
    csrf_protect.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public)
    app.register_blueprint(users)
    app.register_blueprint(main)
    return None
