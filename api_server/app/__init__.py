from flask import Flask
from werkzeug.exceptions import default_exceptions
from api_server.libs.render_json import render_json

def create_app():
    app = Flask(__name__)

    def _handle_http_exception(e):
        return render_json({}, message = e.description, code = e.code)

    for code in default_exceptions:
        app.errorhandler(code)(_handle_http_exception)

    return app
