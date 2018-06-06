"""Create an admin user in the database."""

from project.extensions import db
from project.app import create_app

# Import models
from project.blueprints.users.models import User, UserEmail, Role, UserRoles
import datetime

app = create_app()

# Flask-Admin create admin user
# Create 'username@gmail.com' user with 'admin' role
with app.app_context():
    admin_role = Role(
        id=0,
        name='admin'
    )
    admin_user = User(
        id=0,
        password=app.user_manager.hash_password('password'),
        active=True
    )
    admin_email = UserEmail(
        id=0,
        user_id=0,
        email='username@gmail.com',
        email_confirmed_at=datetime.datetime.utcnow(),
    )
    admin_assignment = UserRoles(
        id=0,
        user_id=0,
        role_id=0
    )
    db.session.add(admin_role)
    db.session.commit()
    db.session.add(admin_user)
    db.session.commit()
    db.session.add(admin_email)
    db.session.commit()
    db.session.add(admin_assignment)
    db.session.commit()
