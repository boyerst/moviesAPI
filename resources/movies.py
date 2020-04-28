import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict 

movies = Blueprint('movies', 'movies')


# GET /api/v1/movies
@movies.route('/', methods=['GET'])
def movies_index():
  result = models.Movie
  movies = []
  for movie in result:
    movie = model_to_dict(movie)
    movies.append(movie)
  return jsonify(movies)


# CREATE /api/v1/movies/
@movies.route('/', methods=['POST'])
def create_movie():
  payload = request.get_json()
  new_movie=models.Movie.create(
    title=payload['title'], 
    genre=payload['genre'], 
    release_year=payload['release_year']
    )
  movie_dict = model_to_dict(new_movie)
  return jsonify(
    data=movie_dict,
    message='you created a movie',
    status=200             
  ), 201


# DESTROY
@movies.route('/<id>', methods=['DELETE']) 
def delete_movie(id):
  delete_query = models.Movie.delete().where(models.Movie.id == id)
  num_of_rows_deleted = delete_query.execute()
  print(num_of_rows_deleted)
  return jsonify(
    data={},
    message="Successfully deleted {} movie with id {}".format(num_of_rows_deleted, id),
    status=200
  ), 200