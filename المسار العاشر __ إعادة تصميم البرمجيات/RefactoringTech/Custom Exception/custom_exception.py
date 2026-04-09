import requests

class UserNotFoundException(Exception):
    def __init__(self, message='404: User Not Found!'):
        self.message = message
        super().__init__(self.message)



def get_user(id):
    url = f"https://app.reqres.in/api/users/{id}"
    response = requests.get(url)
    if response.status_code == 404:
        raise UserNotFoundException()
    return response.json()


print(get_user(20))