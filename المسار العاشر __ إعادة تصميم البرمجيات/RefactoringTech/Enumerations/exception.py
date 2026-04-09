import requests
from enum import IntEnum

class HTTPStatusCode(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500

class UserNotFoundException(Exception):
    def __init__(self, message='404: User Not Found!'):
        self.message = message
        super().__init__(self.message)



def get_user(id):
    url = f"https://app.reqres.in/api/users/{id}"
    response = requests.get(url)
    if response.status_code == HTTPStatusCode.NOT_FOUND:
        raise UserNotFoundException()
    return response.json()


print(get_user(20))