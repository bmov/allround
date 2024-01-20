import os
from flask import Flask
from flask_migrate import Migrate
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

from api import blueprint as api
from .environment import env
from .models import db

basedir = os.path.abspath(os.path.dirname(__file__))
beaker_options = {
    'session.type': 'file',
    'session.data_dir': './data/session',
    'session.cookie_expires': True,
}


class BeakerSessionInterface(SessionInterface):
    """This code is taken in part from ``flask-beaker``."""

    def open_session(self, app, request):
        session = request.environ['beaker.session']
        return session

    def save_session(self, app, session, response):
        session.save()


def create_app():
    """This initializes the app, sets up the database and session,
    and creates the Flask app object.
    """
    app = Flask(__name__)
    app.wsgi_app = SessionMiddleware(app.wsgi_app, beaker_options)
    app.register_blueprint(api, url_prefix='/api')
    app.session_interface = BeakerSessionInterface()

    app.config['RESTX_ERROR_404_HELP'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = env['SQL_DATABASE_URI']
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    return app
