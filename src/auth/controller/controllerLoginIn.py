# ingresar al sistema ya registrado
from flask import request, render_template as render , flash
from flask_login import login_user, logout_user, login_required
from src.auth.services.serviceAuth import ServiceAuth
from src.middlewares.middlewaresLoginIn import UserModel
from sqlalchemy.exc import SQLAlchemyError
from src.auth.security.securityAuth import SecurityAuth
class ControllerLoginIn():

    def onGetControllerLoginView():
        return render('auth/loginin.html')
    
    def onGetControllerLoginIn():
        try:
            txtUsername = request.form['txtUsername']
            txtPassword = request.form['txtPassword']
            user = ServiceAuth.onGetUserByUserName(pfsusersusername = txtUsername)
            if user is not None:
                if user.onGetCheckPassword(txtPassword): 
                    userModel = UserModel(user)
                    login_user(userModel)
                    token = SecurityAuth.onGetSecurityAuthToken()
                    flash('logiado correctamente', category='success')
                    return render('client/clientNotaVenta.html')
                else:
                    flash('Password Incorrecto', category='info')
                    return render('auth/login.html')
            else:
                flash('Usuario y password Incorrecto', category='error')
                return render('auth/login.html')
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
    