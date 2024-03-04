from flask import Blueprint
from src.client.controller.clientControllerNotaVenta import ClientControllerNotaVenta
# admin - categoria - caso
ccnvv= Blueprint('ccnvv', __name__)
ccnvv.route('/ccnvv', methods=['GET'])(ClientControllerNotaVenta.onGetClientControllerNotaVentaView)
ccnvv.route('/ccnvvs', methods=['GET', 'POST'])(ClientControllerNotaVenta.onGetClientControllerNotaVentaSerial)
