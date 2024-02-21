from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
import datetime
import pandas as pd

class ClientServiceLoginUserAuth:

    @classmethod
    def onGetClientServiceLoginUserAuth(self, cedula):
        try:
            userOne = pd.Series(User.query.filter(User.pfsuserscedula == cedula))
            return userOne
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)