from ._root import ApiRoot
from .auth import Auth


routes = [
    {
        'route': '',
        'object': ApiRoot
    },
    {
        'route': '/auth',
        'object': Auth
    },
]
