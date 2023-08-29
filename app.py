from flask import Flask
from flask_cors import CORS
import yaml 

config_file = open("config.yaml")
configuration = yaml.load(config_file, Loader=yaml.FullLoader)
flask_conf = configuration["flask"]

app = Flask(flask_conf["name"])
app.config.from_object(__name__)

# Enable CORS policy
CORS(app)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return "pong!"



if __name__ == '__main__':
    app.run(host=flask_conf["host"], port=flask_conf["port"], debug=flask_conf["debug"])