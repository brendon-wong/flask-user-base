"""Production Flask config settings."""

# The instance folder is not supposed to be committed to version control

# Flask Settings

ENV = 'production'
DEBUG = False

SECRET_KEY = 'this_is_an_insecure_non_production_key'

# Flask-SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'postgres://'
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning

# Flask-Mail SMTP server settings for Gmail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'username@gmail.com'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = '"Project" <username@gmail.com>'

# Flask-User settings
USER_APP_NAME = "Project"  # Shown in and email templates and page footers
# Either email or username authentication must be True
USER_ENABLE_EMAIL = True  # Enable email authentication
USER_ENABLE_USERNAME = False  # Disable username authentication
USER_EMAIL_SENDER_NAME = USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = "username@gmail.com"

# Flask-User email confirmation
USER_ENABLE_CONFIRM_EMAIL = True
USER_SEND_REGISTERED_EMAIL = True

# Flask-User email editing
USER_ENABLE_MULTIPLE_EMAILS = True

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
