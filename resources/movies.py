import models

from flask import Blueprint

movies = Blueprint('movies', 'movies')


@movies.route('/', methods=['GET'])
def movies_index():
  return "movies resource working"