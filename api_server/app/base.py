from flask import Blueprint
from api_server.app import create_app
from api_server.api.common import routes_common
from api_server.api.v1 import routes_v1

app = create_app()

api_v1 = Blueprint('api_v1', __name__)

for r in routes_common:
    api_v1.add_url_rule(r['route'], view_func=r['func'])

for r in routes_v1:
    api_v1.add_url_rule(r['route'], view_func=r['func'])

app.register_blueprint(api_v1, url_prefix='/api/v1')
