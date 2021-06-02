from flask import Blueprint
from api_server.app import create_app
from api_server.api.v1 import routes_v1
from api_server.libs.routes_merge import routes_merge

app = create_app()

api_v1 = Blueprint('api_v1', __name__)



for r in routes_merge(routes_v1):
    api_v1.add_url_rule(r['route'], view_func=r['func'])

app.register_blueprint(api_v1, url_prefix='/api/v1')
