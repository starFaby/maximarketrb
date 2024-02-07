from flask import Blueprint
from src.auth.controller.controllerAuth import ControllerAuth
# admin - categoria - caso
rauth= Blueprint('rauth', __name__)
#rath.route('/racnt', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminCanasta.onGetControllerAdminCanastaList)
#rauth.route('/racnt/<int:page>', methods=['GET', 'POST'])(ControllerAdminCanasta.onGetControllerAdminCanastaList)
rauth.route('/rauth', methods=['GET', 'POST'])(ControllerAuth.onGetControllerAuth)

