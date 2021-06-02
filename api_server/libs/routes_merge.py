from api_server.api.common import routes_common

def routes_merge(routes):
    new_list = []

    for r in routes:
        new_list.append(r)

    for cr in routes_common:
        list_exists = False
        for nr in new_list:
            if nr['route'] == cr['route']:
                list_exists = True

        if not list_exists:
            new_list.append(cr)

    return new_list
