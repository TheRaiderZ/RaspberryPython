import flask
import json

#CORS to allow cross-origin resource sharing
from flask_cors import CORS


app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app, resources={r"/*": {"origins": "*"}})
data = {
    "data": [
    {
      "rotationG": -28,
      "rotationR": -12
    },
    {
      "distance": 20,
    }
  ]
}


@app.route('/getData', methods=['GET'])
def home():
    return json.dumps(data)



app.run()



