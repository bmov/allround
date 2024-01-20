from flask import Blueprint
from flask_restx import Api

from .main import routes as api_main
from .v1 import routes as api_v1

blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    version='0.1',
    title="Allround API",
    description="Allround backend API",
    license="MIT License"
)


def add_routes(routes, prefix):
    for r in routes:
        route = prefix + r['route']
        api.add_namespace(r['object'], route)


add_routes(api_main, '/main')
add_routes(api_v1, '/v1')
