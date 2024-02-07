from flask import Blueprint
from src.auth.controller.controllerLogout import ControllerLogout
# auth logout
rlgt= Blueprint('rlgt', __name__)
rlgt.route('/rlgt', methods=['GET'])(ControllerLogout.onGetControllerLogout)