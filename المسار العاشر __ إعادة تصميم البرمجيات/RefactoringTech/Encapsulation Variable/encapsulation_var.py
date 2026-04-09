user_name = {'firstName': 'Zeyad', 'lastName': 'Mubarak'}


def get_username():
    return user_name


def set_username(data):
     user_name = data


print(get_username())
set_username({'firstName': 'salem', 'lastName': 'ahmed'})
print(get_username())
