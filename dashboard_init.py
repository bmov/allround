from dashboard.app import app
from environment import config

if __name__ == '__main__':
    app.run(debug=True, port=config['DASHBOARD_SERVER_PORT'])
