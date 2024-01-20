from flask_sqlalchemy import SQLAlchemy
from .environment import env

table_prefix = env['TABLE_PREFIX']
db = SQLAlchemy()


class Users(db.Model):
    """
    Create an Users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = table_prefix + 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)
    passwd = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    intro_text = db.Column(db.Text(), nullable=True)
    signdate = db.Column(db.Integer, nullable=False)
    confirm = db.Column(db.Integer, default=0, nullable=False)
    confirm_key = db.Column(db.String(64), index=True, nullable=True)


class Docs(db.Model):
    """
    Create an Docs table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = table_prefix + 'docs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    username = db.Column(db.String(64), index=True, nullable=True)
    date = db.Column(db.Integer, index=True, nullable=False)
    update_date = db.Column(db.Integer, index=True, nullable=True)


class TokenRefreshers(db.Model):
    """
    Create an TokenRefreshers table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = table_prefix + 'token_refreshers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    refresh_token = db.Column(db.String(36), index=True, nullable=False)
    expire = db.Column(db.Integer, index=True, default=0, nullable=False)
