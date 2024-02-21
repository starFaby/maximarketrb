from flask import Blueprint
from src.client.controller.clientControllerLoginUserAuth import ClientControllerLoginUserAuth
# admin - categoria - caso
crlua= Blueprint('crlua', __name__)
crlua.route('/crluas', methods=['GET', 'POST'])(ClientControllerLoginUserAuth.onGetClientControllerLoginUserAuth)