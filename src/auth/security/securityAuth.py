from flask import make_response
import datetime
import jwt
import pytz
from src.auth.jwt.jwtoken import PayLoad
from flask_login import current_user

class SecurityAuth:

    global secret
    global tz
    secret = "jtD@8iPFvE&5x7Jy"
    tz = pytz.timezone("America/Guayaquil")

    @classmethod
    def onGetSecurityAuthToken(self):
        #payload = PayLoad.onGetPayLoad
        payload = {
            'iat': datetime.datetime.now(tz=tz),
            'exp': datetime.datetime.now(tz=tz) + datetime.timedelta(minutes=10),
            'username': current_user.id,
            'fullname': current_user.email
        }
        jwtoken = jwt.encode(payload,secret, algorithm="HS256")
        print(jwtoken)
        return make_response({"token": jwtoken}, 200)
    
    @classmethod
    def verifyAuthToken(self, headers):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            print(authorization)
            encodedToken = authorization.split(" ")[1]
            print(encodedToken)
            try:
                payload = jwt.decode(encodedToken, secret, algorithms=["HS256"])
                return payload
            except(jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                return False
        return False
    
