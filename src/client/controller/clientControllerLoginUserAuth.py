# ingresar al sistema ya registrado
from flask import request, render_template as render , flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from src.client.services.clientServiceLoginUserAuth import ClientServiceLoginUserAuth
from src.middlewares.middlewaresLoginIn import UserModel
from sqlalchemy.exc import SQLAlchemyError
from src.auth.security.securityAuth import SecurityAuth
class ClientControllerLoginUserAuth():

    def onGetClientControllerLoginUserAuth():
        txtCedula = request.form['txtCedula']
        userOne = ClientServiceLoginUserAuth.onGetClientServiceLoginUserAuth(txtCedula)
        print(userOne.count())
        aux = userOne.count()
        if aux >= 1:
            user = 1
            return render('client/clientNotaVenta.html', userOne=userOne, user = user)
        else:
            user=0
            return render('client/clientNotaVenta.html', userOne=userOne, user = user)