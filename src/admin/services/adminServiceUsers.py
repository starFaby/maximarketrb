from flask import render_template as render
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError

class AdminServiceUser:
    
    @classmethod
    def ongetAdminServiceUser(self):
        try:
            userList = User.query.all()
            return userList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        