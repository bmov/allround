from flask import Response, abort
from app import create_app
from components.render_json import message
from components.fileio import read_file

app = create_app()


@app.errorhandler(403)
def forbidden(error):
    return message(None, message='Forbidden', code=403)


@app.errorhandler(404)
def page_not_found(error):
    return message(None, message='Page not found', code=404)


@app.errorhandler(500)
def server_error(error):
    return message(None, message='Internal Server Error', code=500)


@app.route("/LICENSE")
def license():
    license = read_file('./LICENSE')
    if license:
        return Response(
            response=license, status=200,  mimetype="text/plain")
    else:
        abort(404)
