import jwt
import time

def gen_auth_token(username, secret):
    payload = {
        "username" : username,
        "creation_time" : int(time.time()),
    }
    return jwt.encode(payload, secret, "HS256")

def is_valid_auth_jwt(jwt_token, secret, jwt_TTL):
    try:
        user_info = jwt.decode(jwt_token, secret, "HS256")
        if user_info["creation_time"] + jwt_TTL > int(time.time()):
            return True
        else:
            return False
    except:
        return False
    