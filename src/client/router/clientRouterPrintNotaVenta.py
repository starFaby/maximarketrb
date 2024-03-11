from flask import Blueprint
from src.client.controller.clientControllerPrintNotaVenta import ClientControllerPrintNotaVenta
# admin - categoria - caso
crpnv= Blueprint('crpnv', __name__)
crpnv.route('/crpnv', methods=['POST'])(ClientControllerPrintNotaVenta.onGetClientControllerPrintNotaVentaView)
