from flask import Flask, jsonify

from resources.movies import movies

import models

from flask_cors import CORS


DEBUG=True
PORT=8000


app = Flask(__name__)

CORS(movies, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(movies, url_prefix='/api/v1/movies')



# GET /
@app.route('/')
def hello():
  return 'testing movies API server'








if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)