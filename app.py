from flask import Flask 




DEBUG=True
PORT=8000


app = Flask(__name__)



# GET /
@app.route('/')
def hello():
  return 'testing movies API server'










if __name__ == '__main__':
 
  app.run(debug=DEBUG, port=PORT)