import json
from flask import Response

def render_json(body, message = '', code = 200):
    dict = {}
    dict['code'] = code
    dict['message'] = message
    dict['body'] = body

    json_data = json.dumps(dict)
    return Response(json_data, mimetype='application/json'), code
