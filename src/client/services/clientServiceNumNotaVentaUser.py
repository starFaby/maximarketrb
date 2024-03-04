from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
import datetime
import pandas as pd
from flask_login import current_user

class ClientServiceNumNotaVentaUser:

    @classmethod
    def onGetClientServiceNumNotaVentaUser(self):
        try:
            idUser = current_user.iduser
            numIdUser = pd.Series(Canasta.query.filter(Canasta.pfsabcnstotal == 0).filter(Canasta.pfsusersid == idUser))
            return numIdUser
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)