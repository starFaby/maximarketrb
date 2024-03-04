from flask import Blueprint
from src.client.controller.clientControllerDetalleNotaVenta import ClientControllerDetalleNotaVenta
# admin - categoria - caso
crdnv= Blueprint('crdnv', __name__)
crdnv.route('/crdnv', methods=['GET', 'POST'])(ClientControllerDetalleNotaVenta.onGetClientControllerDetalleNotaVentaSave)
