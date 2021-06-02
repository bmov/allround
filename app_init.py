from app_server.app import app
from environment import config
from werkzeug.serving import run_simple

if __name__ == '__main__':
    run_simple('localhost', int(config['API_SERVER_PORT']), app,
               use_reloader=True, use_debugger=True, use_evalex=True)
