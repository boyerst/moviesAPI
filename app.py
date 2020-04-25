from flask import Flask, jsonify

from resources.movies import movies

import models


DEBUG=True
PORT=8000


app = Flask(__name__)

app.register_blueprint(movies, url_prefix='/api/v1/movies')



# GET /
@app.route('/')
def hello():
  return 'testing movies API server'








if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)