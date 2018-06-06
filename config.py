"""Development Flask config settings."""

import os

# Flask Settings

ENV = 'development'
DEBUG = True

# SERVER_NAME = 'localhost:5000'
SECRET_KEY = 'this_is_an_insecure_development_key'

# Flask-SQLAlchemy settings
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Local sqlite3 database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.db')
# Local copy of remote Heroku Postgres db to generate migration script locally:
# SQLALCHEMY_DATABASE_URI = "postgresql://localhost/heroku_remote_database"
SQLALCHEMY_TRACK_MODIFICATIONS = False # Avoids SQLAlchemy warning

# Flask-Mail SMTP server settings for Yahoo
MAIL_SERVER = 'smtp.mail.yahoo.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'username@yahoo.com'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = '"Project" <username@yahoo.com>'

# Flask-User settings
USER_APP_NAME = "Project" # Shown in and email templates and page footers
# Either email or username authentication must be True
USER_ENABLE_EMAIL = True # Enable email authentication
USER_ENABLE_USERNAME = False # Disable username authentication
USER_EMAIL_SENDER_NAME = USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = "username@yahoo.com"

# Flask-User email confirmation
USER_ENABLE_CONFIRM_EMAIL = True
USER_SEND_REGISTERED_EMAIL = True

# Flask-User enable multiple emails to support changing user emails 
USER_ENABLE_MULTIPLE_EMAILS = True

# Flask-User additional pages
USER_ENABLE_CHANGE_PASSWORD = True

# Flask-User redirects
USER_AFTER_CHANGE_PASSWORD_ENDPOINT = 'main.dashboard'
USER_AFTER_CHANGE_USERNAME_ENDPOINT = 'main.dashboard'
USER_AFTER_CONFIRM_ENDPOINT = 'main.dashboard'
USER_AFTER_EDIT_USER_PROFILE_ENDPOINT = 'main.dashboard'
USER_AFTER_FORGOT_PASSWORD_ENDPOINT = 'main.dashboard'
USER_AFTER_LOGIN_ENDPOINT = 'main.dashboard'
USER_AFTER_LOGOUT_ENDPOINT = ''
USER_AFTER_REGISTER_ENDPOINT = 'main.dashboard'
USER_AFTER_RESEND_EMAIL_CONFIRMATION_ENDPOINT = ''
USER_AFTER_RESET_PASSWORD_ENDPOINT = 'main.dashboard'
USER_AFTER_INVITE_ENDPOINT = 'main.dashboard'
USER_UNAUTHENTICATED_ENDPOINT = 'user.login'
USER_UNAUTHORIZED_ENDPOINT = 'user.register'
USER_AFTER_REGISTER_ENDPOINT = 'main.dashboard'
