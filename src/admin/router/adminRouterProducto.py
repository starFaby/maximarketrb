from flask import Blueprint
from src.admin.controller.adminControllerProducto import AdminControllerProducto
# admin - router - producto
arp= Blueprint('arp', __name__)
arp.route('/arp', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerProducto.onGetAdminControllerProductoList)
arp.route('/arp/<int:page>', methods=['GET', 'POST'])(AdminControllerProducto.onGetAdminControllerProductoList)
arp.route('/arps', methods=['POST'])(AdminControllerProducto.onGetControllerAdminProductoSave)