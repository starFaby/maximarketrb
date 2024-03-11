from flask import request, render_template as render , flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from src.client.services.clientServiceNotaVentaSerial import ClientServiceNotaVentaSerial
from src.client.services.clientServiceNotaVentaCreate import ClientServiceNotaVentaCreate
from src.client.services.clientServiceDetalleNotaVenta import ClientServiceDetalleNotaVenta
from src.client.services.clientServiceNoVeSaveArchi import ClientServiceNotaVentaSaveArchiv
from src.middlewares.middlewaresLoginIn import UserModel
from sqlalchemy.exc import SQLAlchemyError
from src.auth.security.securityAuth import SecurityAuth
import numpy as np
from datetime import datetime
from flask_login import current_user, logout_user
class ClientControllerPrintNotaVenta():

    def onGetClientControllerPrintNotaVentaView():
        iduser = 0
        if current_user.is_authenticated:
            idUser = current_user.iduser
        idCanasta = request.form['txtIdCanasta']
        print("La id de la canastaes: ", idCanasta)
        logout_user()
        return redirect(url_for('ccnvv.onGetClientControllerNotaVentaView'))