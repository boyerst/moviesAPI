from peewee import *
import datetime

DATABASE = SqliteDatabase('movies.sqlite')


class Movie(Model):
  title = CharField()
  genre = Charfield()
  release_year = Integer()
  created_at: DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE