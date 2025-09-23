from model import Model
from field import *
from db import DataBase

Model.db = DataBase('database.sqlite')
Model.connection = Model.db.connect()

class Post(Model):
    title = CharField()
    body = TextField()
    created_at = DateTimeField()
    published = BooleanField()


class User(Model):
    f_name = CharField()
    l_name = CharField(max_length=255)
    age = IntegerField()


if __name__ == '__main__':
    post = Post()
    user = User()