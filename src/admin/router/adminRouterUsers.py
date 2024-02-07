from flask import Blueprint
from src.admin.controller.adminControllerUser import AdminControllerUser
# admin - categoria - caso
aru= Blueprint('aru', __name__)
#rath.route('/racnt', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminCanasta.onGetControllerAdminCanastaList)
#rauth.route('/racnt/<int:page>', methods=['GET', 'POST'])(ControllerAdminCanasta.onGetControllerAdminCanastaList)
aru.route('/aru', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserList)

