from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from flask_login import current_user
import datetime
import pandas as pd

class ClientServiceNotaVentaCreate:

    @classmethod
    def onGetClientServiceNotaVentaCreateComprobar(self):
        try:
            numNoVeOne = pd.Series(Canasta.query.filter(Canasta.pfsabcnstnumpf))
            
            return numNoVeOne
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)


    @classmethod
    def onGetClientServiceNotaVentaCreate(self):
        try:
            idUser = current_user.iduser
            numNoVeOneNew = pd.Series(Canasta.query.filter(Canasta.pfsabcnstotal == 0).filter(Canasta.pfsusersid == idUser))
            return numNoVeOneNew
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)

    @classmethod
    def onGetClientServiceNotaVentaCreateSave(self, pfsabcnstnumpf, pfsabcnstsubtotal, pfsabcnstdto, pfsabcnstiva, pfsabcnstotal, pfsabcnstestado, pfsabcnstcreatedat, pfsusersid):
        try:
            newNotaVenta = Canasta(pfsabcnstnumpf, pfsabcnstsubtotal, pfsabcnstdto, pfsabcnstiva, pfsabcnstotal, pfsabcnstestado, pfsabcnstcreatedat, pfsusersid)
            db.session.add(newNotaVenta)
            db.session.commit()
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
        
        
    
        
    