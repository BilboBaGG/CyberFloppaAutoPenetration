from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_cors import CORS
import yaml 
import argparse
from tokens import *
from tools.web.sqlmap.thirdparty.bottle.bottle import cookie_encode

parser = argparse.ArgumentParser(description='Web inteface for the most popular penetration testing tools.', epilog="AutoPenetration by CyberFloppa")
parser.add_argument('-u', dest='username', help='username admin user')
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
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET'])
def dashboard():
    cookie = request.cookies.get("Auth")
    if is_valid_auth_jwt(cookie, flask_conf["jwt_secret"], flask_conf["jwt_TTL"]):
        return render_template("dashboard.html")
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == app.config['admin_username'] and password == app.config['admin_password']:
            response = make_response(redirect(url_for('dashboard')))

            response.set_cookie("Auth", value = gen_auth_token(username, flask_conf["jwt_secret"]), httponly = True)
            return response
        else:
            return render_template("login.html", message="Wrong usernane or password")
    else:
        cookie = request.cookies.get("Auth")
        if cookie:
            if is_valid_auth_jwt(cookie, flask_conf["jwt_secret"], flask_conf["jwt_TTL"]):
                return redirect(url_for("dashboard"))
            else:
                return render_template("login.html", message="Your token is not valid")
        else:    
            return render_template("login.html")


if __name__ == '__main__':
    args = parser.parse_args()

    if args.password and args.username:
        app.config["admin_password"] = args.password
        app.config['admin_username'] = args.username
        app.run(host=flask_conf["host"], port=flask_conf["port"], debug=flask_conf["debug"])
    else:
        parser.print_help()