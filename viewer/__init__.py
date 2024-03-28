import json
import requests
from flask import Flask, request

from app.environment import env


def req_route(path, args):
    req_path = env['ALLROUND_API_URI'] + '/api/v1/pages/viewRoute'
    req = requests.post(req_path, json={
        'route': path,
        'query': args
    }).json()
    return req['data']


def create_app():
    """This initializes the viewer, and creates the Flask app object.
    """
    app = Flask(__name__)

    return app
