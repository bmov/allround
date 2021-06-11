from unittest.mock import patch
from app_server.libs.routes_merge import routes_merge


class Actions:
    def test_1():
        return 'Hello. This is initial data for test!!'

    def test_2():
        return 'Hello. This is second function of test!!!!'

    def test_3():
        return 'Wonderful action!'

    def changed_test_1():
        return 'Hello. This is changed new function test_1!'

    def changed_test_2():
        return 'Hello. This is changed new function test_2!'


act = Actions()
initial_routes = [
    {
        'route': '/test_1',
        'func': act.test_1
    },
    {
        'route': '/test_2',
        'func': act.test_2
    }
]


@patch('app_server.libs.routes_merge.routes_common', initial_routes)
def merge(r):
    return routes_merge(r)


def test_routes():
    """
    [
        {
            'route': '/test_2',
            'func': act.changed_test_1
        },
        {
            'route': '/test_3',
            'func': act.test_3
        },
        {
            'route': '/test_1',
            'func': act.test_1
        }
    ]
    """

    global act
    data = [
        {
            'route': '/test_2',
            'func': act.changed_test_1
        },
        {
            'route': '/test_3',
            'func': act.test_3
        }
    ]

    data = merge(data)

    assert data[0]['route'] == '/test_2'
    assert data[0]['func'] == act.changed_test_1
    assert data[1]['route'] == '/test_3'
    assert data[1]['func'] == act.test_3
    assert data[2]['route'] == '/test_1'
    assert data[2]['func'] == act.test_1


def test_routes_2():
    """
    [
        {
            'route': '/test_1',
            'func': act.test_3
        },
        {
            'route': '/anotherTest',
            'func': act.changed_test_2
        },
        {
            'route': '/test_3',
            'func': act.test_3
        },
        {
            'route': '/test_2',
            'func': act.test_2
        }
    ]
    """

    global act
    data = [
        {
            'route': '/test_1',
            'func': act.test_3
        },
        {
            'route': '/anotherTest',
            'func': act.changed_test_2
        },
        {
            'route': '/test_3',
            'func': act.test_3
        }
    ]

    data = merge(data)

    assert data[0]['route'] == '/test_1'
    assert data[0]['func'] == act.test_3
    assert data[1]['route'] == '/anotherTest'
    assert data[1]['func'] == act.changed_test_2
    assert data[2]['route'] == '/test_3'
    assert data[2]['func'] == act.test_3
    assert data[3]['route'] == '/test_2'
    assert data[3]['func'] == act.test_2


def test_routes_not_overwrites():
    """
    [
        {
            'route': '/testNewRoute',
            'func': act.changed_test_1
        },
        {
            'route': '/testNewRoute2',
            'func': act.changed_test_2
        },
        {
            'route': '/test_1',
            'func': act.test_1
        },
        {
            'route': '/test_2',
            'func': act.test_2
        }
    ]
    """

    global act
    data = [
        {
            'route': '/testNewRoute',
            'func': act.changed_test_1
        },
        {
            'route': '/testNewRoute2',
            'func': act.changed_test_2
        }
    ]

    data = merge(data)

    assert data[0]['route'] == '/testNewRoute'
    assert data[0]['func'] == act.changed_test_1
    assert data[1]['route'] == '/testNewRoute2'
    assert data[1]['func'] == act.changed_test_2
    assert data[2]['route'] == '/test_1'
    assert data[2]['func'] == act.test_1
    assert data[3]['route'] == '/test_2'
    assert data[3]['func'] == act.test_2
