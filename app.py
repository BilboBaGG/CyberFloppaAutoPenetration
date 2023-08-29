from flask import Flask
from flask_cors import CORS
import yaml 

fileconfig = open("config.yaml")
configuration = yaml.load(fileconfig, Loader=yaml.FullLoader)
flaskConfiguration = configuration["flask"]

app = Flask(flaskConfiguration["name"])
app.config.from_object(__name__)

# Enable CORS policy
CORS(app)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return "pong!"

if __name__ == '__main__':
    app.run(host=flaskConfiguration["host"], port=flaskConfiguration["port"], debug=flaskConfiguration["debug"])