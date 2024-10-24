from typing import Sequence, TypeVar

T = TypeVar('T')


class Message:
    def __init__(
        self,
        data: Sequence[T],
        message: str = '',
        status: int = 200
    ) -> None:
        dict = {}
        dict['status'] = status
        dict['message'] = message
        dict['data'] = data

        json_data = dict
        self.__json_data = json_data
        self.__status = status

    def get_response(self):
        return self.__json_data, self.__status

    def get_dict(self):
        return self.__json_data
