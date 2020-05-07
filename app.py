from flask import Flask, jsonify

from resources.movies import movies

from resources.users import users

import models

from flask_cors import CORS

from flask_login import LoginManager

from flask_login import login_user, current_user, logout_user


DEBUG=True
PORT=8000


app = Flask(__name__)

app.secret_key = "secret time"

login_manager = LoginManager()

login_manager.init_app(app) #passing in app object, defined above


@login_manager.user_loader
def load_user(user_id):
  try:
    print("loading the following user")
    user = models.User.get_by_id(user_id) # IMPORTANT CHANGE 

    return user 
  except models.DoesNotExist: 
    return None

@login_manager.unauthorized_handler
def unauthorized():
  return jsonify(
    data={
      'error': "User not logged in"
    },
    message='You must be logged in to access that resource',
    status=401
  ), 401



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