import json
from flask import request
from viewer import create_app, req_route

app = create_app()


@app.route('/<path:path>')
def get_route(path):
    get_args = request.args.to_dict()

    return req_route(path, get_args)
