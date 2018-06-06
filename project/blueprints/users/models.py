"""User models."""

import datetime

from project.extensions import db

from flask_user import current_user, login_required, roles_required, UserManager, UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    username = db.Column(db.String(50), nullable=True,
                         unique=True)  # changed nullable to True
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean())
    # changed nullable to True
    first_name = db.Column(db.String(50), nullable=True)
    # changed nullable to True
    last_name = db.Column(db.String(50), nullable=True)

    # Relationship
    user_emails = db.relationship('UserEmail')
    roles = db.relationship('Role', secondary='user_roles')


# Define UserEmail data-model
class UserEmail(db.Model):
    __tablename__ = 'user_emails'
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', uselist=False)

    # User email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    is_primary = db.Column(db.Boolean(), nullable=False, server_default='0')


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey(
        'roles.id', ondelete='CASCADE'))
