from flask import Flask, jsonify

import models


DEBUG=True
PORT=8000


app = Flask(__name__)



# GET /
@app.route('/')
def hello():
  return 'testing movies API server'


@app.route('/test_json')
def get_json():
  return jsonify(['we', 'will', 'make', 'a', 'flask', 'app'])







if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)