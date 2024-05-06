def message(body, message='', code=200):
    dict = {}
    dict['status'] = code
    dict['message'] = message

    if body is not None:
        dict['body'] = body

    json_data = dict
    return json_data, code
