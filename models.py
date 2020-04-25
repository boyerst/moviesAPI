from peewee import *
import datetime

DATABASE = SqliteDatabase('movies.sqlite')


class Movie(Model):
  title = CharField()
  genre = CharField()
  release_year = IntegerField()
  created_at: DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE


def initialize():
  DATABASE.connect()

  DATABASE.create_tables([Movie], safe=True)
  print("You are connected to the Database and have created tables that have not yet existed")

  DATABASE.close()