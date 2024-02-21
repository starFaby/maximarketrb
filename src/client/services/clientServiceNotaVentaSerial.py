from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
import datetime
import pandas as pd

class ClientServiceNotaVentaSerial:

    @classmethod
    def onGetClientServiceNotaVentaSerial(self, serial):
        try:
            serialOne = pd.Series(Producto.query.filter(Producto.pfsabprodserial == serial))
            return serialOne
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
