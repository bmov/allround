from flask import Blueprint
from dashboard.app import create_app
from dashboard.routes import routes

app = create_app()

dashboard_bp = Blueprint('dashboard', __name__)

for r in routes:
    dashboard_bp.add_url_rule(r['route'], view_func=r['func'])

app.register_blueprint(dashboard_bp, url_prefix='/')
