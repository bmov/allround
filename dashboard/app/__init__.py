from flask import Flask
from werkzeug.exceptions import default_exceptions

def create_app():
    app = Flask(__name__)

    return app
