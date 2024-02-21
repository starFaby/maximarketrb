# ingresar al sistema ya registrado
from flask import request, render_template as render , flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from src.client.services.clientServiceNotaVentaSerial import ClientServiceNotaVentaSerial
from src.middlewares.middlewaresLoginIn import UserModel
from sqlalchemy.exc import SQLAlchemyError
from src.auth.security.securityAuth import SecurityAuth
class ClientControllerNotaVenta():

    def onGetClientControllerNotaVentaView():
        return render('client/clientNotaVenta.html')
    
    def onGetClientControllerNotaVentaSerial():
        pfsabprodserial = request.form['txtSerial']
        serial = ClientServiceNotaVentaSerial.onGetClientServiceNotaVentaSerial(pfsabprodserial)
        aux = serial.count()
        if aux >= 1:
            existe = 1
            flash('Producto Listadas', category='success')
            return render('client/clientNotaVenta.html', existe = existe, serial = serial) 
        else:
            existe = 0
            return render('client/clientNotaVenta.html', existe = existe, serial = serial) 
    
    def onGetClientControllerNotaVentaCreate():
        pass