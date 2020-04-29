from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('movies.sqlite')


class User(UserMixin, Model):
  username=CharField(unique=True)
  email=CharField(unique=True)
  password=CharField()

  class Meta:
    database = DATABASE


class Movie(Model):
  title = CharField()
  genre = CharField()
  release_year = IntegerField()
  created_at: DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE


def initialize():
  DATABASE.connect()

  DATABASE.create_tables([User, Movie], safe=True)
  print("You are connected to the Database and have created tables that have not yet existed")

  DATABASE.close()