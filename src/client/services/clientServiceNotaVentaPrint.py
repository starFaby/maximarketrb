from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
import datetime
import pandas as pd

class ClientServiceNotaVentaPrint:

    @classmethod
    def onGetClientServiceNotaVentaPrintUser(self, idUser):
        try:
            userId = pd.Series(User.query.filter(User.pfsusersid == idUser))
            return userId
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetClientServiceNotaVentaPrintIdDetalleNotaVenta(self, idCanasta):
        try:
            #detalleNotaVenta = pd.Series(Detallecanasta.query.filter(Detallecanasta.pfsabcanastaid == idCanasta))
            detalleNotaVenta =Detallecanasta.query.join(Producto, Detallecanasta.pfsabproductoid == Producto.pfsabprodid).add_columns(Detallecanasta.pfsabdcantidad, Producto.pfsabprodnombre, Detallecanasta.pfsabdcprecio, Detallecanasta.pfsabdctotal).filter(Detallecanasta.pfsabcanastaid == idCanasta).filter(Detallecanasta.pfsabdcestado == 1)
            return detalleNotaVenta
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)

        
    @classmethod
    def onGetClientServiceNotaVentaPrintIdNotaVenta(self, idUser, idCanasta):
        try:
            canasta = pd.Series(Canasta.query.filter(Canasta.pfsusersid == idUser).filter(Canasta.pfsabcnstid == idCanasta))
            return canasta
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    