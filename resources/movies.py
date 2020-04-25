import models

from flask import Blueprint

movies = Blueprint('movies', 'movies')

# GET /api/v1/movies
@movies.route('/', methods=['GET'])
def movies_index():
  return "movies resource working"

# CREATE /api/v1/movies/
@movies.route('/', methods=['POST'])
def create_movie():
  return "movies create route hitting"