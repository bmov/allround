from app_server.libs.render_json import render_json

def hello():
    return render_json({}, message = 'hello')
