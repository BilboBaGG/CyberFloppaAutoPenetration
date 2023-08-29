from flask import Flask, render_template
from flask_cors import CORS
import yaml 

fileconfig = open("config.yaml")
configuration = yaml.load(fileconfig, Loader=yaml.FullLoader)
flask_conf= configuration["flask"]

app = Flask(flask_conf["name"], template_folder="templates")
app.config.from_object(__name__)

# Enable CORS policy
CORS(app)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return "pong!"

@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host=flask_conf["host"], port=flask_conf["port"], debug=flask_conf["debug"])