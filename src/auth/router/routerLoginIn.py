from flask import Blueprint
from src.auth.controller.controllerLoginIn import ControllerLoginIn
# admin - categoria - caso
rlgn= Blueprint('rlgn', __name__)
#rath.route('/racnt', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminCanasta.onGetControllerAdminCanastaList)
#rauth.route('/racnt/<int:page>', methods=['GET', 'POST'])(ControllerAdminCanasta.onGetControllerAdminCanastaList)
rlgn.route('/rlgn', methods=['GET', 'POST'])(ControllerLoginIn.onGetControllerLoginView)
rlgn.route('/rlgin', methods=['POST'])(ControllerLoginIn.onGetControllerLoginIn)