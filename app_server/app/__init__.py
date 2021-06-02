from flask import Flask
from werkzeug.exceptions import default_exceptions
from app_server.libs.render_json import render_json
from .blueprints import reg_bp

to_reload = False
reload_registered = False

def reload():
    global to_reload, reload_registered
    to_reload = True

    if not reload_registered:
        reload_registered = True
        return render_json({'reloaded':False}, message = 'reload action registered')
    else:
        return render_json({'reloaded':True}, message = 'reloaded')

def get_app():
    app = Flask(__name__)

    app.add_url_rule('/reload', view_func=reload)

    def _handle_http_exception(e):
        return render_json({}, message = e.description, code = e.code)

    for code in default_exceptions:
        app.errorhandler(code)(_handle_http_exception)

    app_bp = reg_bp(app)

    return app_bp

class AppReloader(object):
    def __init__(self, create_app):
        self.create_app = create_app
        self.app = create_app()

    def get_application(self):
        global to_reload
        if to_reload:
            self.app = self.create_app()
            to_reload = False

        return self.app

    def __call__(self, environ, start_response):
        app = self.get_application()
        return app(environ, start_response)

app = AppReloader(get_app)
