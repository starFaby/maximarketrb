import datetime
import jwt
import pytz
from flask_login import current_user
import json
from flask import jsonify



class PayLoad:
    global tz
    tz = pytz.timezone("America/Guayaquil")

    @classmethod  
    def onGetPayLoad():
        payload = {
            'iat': datetime.datetime.now(tz=tz),
            'exp': datetime.datetime.now(tz=tz) + datetime.timedelta(minutes=10),
            'username': current_user.id,
            'fullname': current_user.email
        }
        return    jsonify(payload)