"""Define objects of all extensions."""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
csrf_protect = CSRFProtect()
