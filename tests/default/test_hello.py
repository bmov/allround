from api.main._root import HelloIndexApi


def test_hello():
    test_string = 'hello world from api_main'

    get = HelloIndexApi.get()
    assert get['hello'] == test_string
