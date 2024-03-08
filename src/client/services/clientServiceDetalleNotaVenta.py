from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from src.client.model.clientModelDetalleNotaVenta import ModelDetalleNotaVenta
import datetime
import pandas as pd
from flask_login import current_user

class ClientServiceDetalleNotaVenta:

    @classmethod
    def onGetClientServiceDetalleNotaVentaSave(self, pfsabdcnumpf, pfsabdcantidad, pfsabdcprecio, pfsabdctotal, pfsabdcestado, pfsabdcreatedat, pfsabproductoid, pfsabcanastaid):
        try:
                
            modelDetalleNotaVenta = ModelDetalleNotaVenta(0,pfsabdcnumpf, pfsabdcantidad, pfsabdcprecio, pfsabdctotal, pfsabdcestado, pfsabdcreatedat, pfsabproductoid, pfsabcanastaid)
            newDetalleNotaVenta = Detallecanasta(pfsabdcnumpf = modelDetalleNotaVenta.getpfsabdcnumpf(),
                                                pfsabdcantidad = modelDetalleNotaVenta.getpfsabdcantidad(), 
                                                pfsabdcprecio = modelDetalleNotaVenta.getpfsabdcprecio(), 
                                                pfsabdctotal = modelDetalleNotaVenta.getpfsabdctotal(), 
                                                pfsabdcestado = modelDetalleNotaVenta.getpfsabdcestado(), 
                                                pfsabdcreatedat = modelDetalleNotaVenta.getpfsabdcreatedat(), 
                                                pfsabproductoid = modelDetalleNotaVenta.getpfsabproductoid(), 
                                                pfsabcanastaid = modelDetalleNotaVenta.getpfsabcanastaid())
            
            db.session.add(newDetalleNotaVenta)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetClientServiceDetalleNotaVentaAll(self):
        #if current_user.is_authenticated:
        try:
            idUser = 0
            aux = 0
            if current_user.is_authenticated:
                idUser = current_user.iduser

            numIdUser = pd.Series(Canasta.query.filter(Canasta.pfsabcnstotal == 0).filter(Canasta.pfsusersid == idUser))
            for item in numIdUser:
                aux = item.pfsabcnstnumpf
            
            #userDetaNoVe = pd.Series(Detallecanasta.query.filter(Detallecanasta.pfsabdcnumpf == aux))
            userDetaNoVe = pd.Series(Detallecanasta.query.join(Producto, Detallecanasta.pfsabproductoid == Producto.pfsabprodid).add_columns(Detallecanasta.pfsabdcantidad, Producto.pfsabproddetalle, Detallecanasta.pfsabdcprecio, Detallecanasta.pfsabdctotal, Detallecanasta.pfsabcanastaid).filter(Detallecanasta.pfsabdcnumpf == aux))
            return userDetaNoVe
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)                
