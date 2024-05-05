import os
from connexion import AsyncApp
from connexion.resolver import RestyResolver

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    """This initializes the app, sets up the database and session,
    and creates the Connexion app object.
    """
    app = AsyncApp(__name__)

    app.add_api('_openapi.yml', base_path='/api',
                resolver=RestyResolver('api'))

    return app
