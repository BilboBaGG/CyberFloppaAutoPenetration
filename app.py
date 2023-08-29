from flask import Flask, render_template
from flask_cors import CORS
import yaml 
import argparse

parser = argparse.ArgumentParser(description='Web inteface for the most popular penetration testing tools.', epilog="AutoPenetration by CyberFloppa")
parser.add_argument('-p', dest='password', help='pass for admin user')

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

@app.route('/', methods=['GET'])
def index():
    return app.config["admin_password"]


@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

if __name__ == '__main__':
    args = parser.parse_args()

    if args.password:
        app.config["admin_password"] = args.password
        app.run(host=flask_conf["host"], port=flask_conf["port"], debug=flask_conf["debug"])
    else:
        parser.print_help()