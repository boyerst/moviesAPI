import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict 

movies = Blueprint('movies', 'movies')


# GET /api/v1/movies
@movies.route('/', methods=['GET'])
def movies_index():
  return "movies resource working"



# CREATE /api/v1/movies/
@movies.route('/', methods=['POST'])
def create_movie():
  payload = request.get_json()
  print(payload)
  new_movie=models.Movie.create(title=payload['title'], genre=payload['genre'], release_year=payload['release_year'])
  print(new_movie)
  print(dir(new_movie))
  movie_dict = model_to_dict(new_movie)
  return jsonify(
    data=movie_dict,
    message='you created a movie',
    status=200             
  ), 201