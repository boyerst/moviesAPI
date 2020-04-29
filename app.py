from flask import Flask, jsonify

from resources.movies import movies

from resources.users import users

import models

from flask_cors import CORS

from flask_login import LoginManager


DEBUG=True
PORT=8000


app = Flask(__name__)

app.secret_key = "secret time"

login_manager = LoginManager()

login_manager.init_app(app) #passing in app object, defined above

CORS(movies, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(movies, url_prefix='/api/v1/movies')
app.register_blueprint(users, url_prefix='/api/v1/users')



# GET /
@app.route('/')
def hello():
  return 'testing movies API server'








if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)