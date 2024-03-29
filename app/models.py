from flask_sqlalchemy import SQLAlchemy
from .environment import env

db = SQLAlchemy()


class Users(db.Model):
    """
    Create an Users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

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
    __tablename__ = 'docs'

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
    __tablename__ = 'token_refreshers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    refresh_token = db.Column(db.String(36), index=True, nullable=False)
    expire = db.Column(db.Integer, index=True, default=0, nullable=False)


class Pages(db.Model):
    """
    Create an Pages table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    folder = db.Column(db.Integer, default=0, index=True, nullable=False)
    page_type = db.Column(db.String(32), index=True, nullable=False)
    description = db.Column(db.Text(), nullable=True)


class PageFolders(db.Model):
    """
    Create an PageFolders table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'page_folders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    parent = db.Column(db.Integer, default=0, index=True, nullable=False)
    description = db.Column(db.Text(), nullable=True)
