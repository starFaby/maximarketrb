# ingresar al sistema ya registrado
from flask import request, render_template as render , flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from src.client.services.clientServiceNotaVentaSerial import ClientServiceNotaVentaSerial
from src.client.services.clientServiceNotaVentaCreate import ClientServiceNotaVentaCreate
from src.client.services.clientServiceDetalleNotaVenta import ClientServiceDetalleNotaVenta
from src.middlewares.middlewaresLoginIn import UserModel
from sqlalchemy.exc import SQLAlchemyError
from src.auth.security.securityAuth import SecurityAuth
import numpy as np
from datetime import datetime
from flask_login import current_user
class ClientControllerNotaVenta():

    def onGetClientControllerNotaVentaView():
        auxDetalleTotal = []
        detalleNoVe = ClientServiceDetalleNotaVenta.onGetClientServiceDetalleNotaVentaAll()
        for item in detalleNoVe:
            auxDetalleTotal.append(item.pfsabdctotal)
        auxSuma = np.sum(auxDetalleTotal)
        return render('client/clientNotaVenta.html', detalleNoVe=detalleNoVe, auxSuma = auxSuma)
        
    
    def onGetClientControllerNotaVentaSerial():
        idUser = 0
        if current_user.is_authenticated:
            idUser = current_user.iduser
            if idUser >= 1:
                idUser = 1
            else:
                idUser = 0        

        pfsabprodserial = request.form['txtSerial']
        
        serial = ClientServiceNotaVentaSerial.onGetClientServiceNotaVentaSerial(pfsabprodserial)
        aux = serial.count()
        if aux >= 1:
            existe = 1
            flash('Producto Listadas', category='success')
            return render('client/clientNotaVenta.html', existe = existe, serial = serial, idUser = idUser) 
        else:
            existe = 0
            return render('client/clientNotaVenta.html', existe = existe, serial = serial, idUser = idUser) 
    

    def onGetClientControllerNotaVentaCreate():
        createNumNotaVenta = ClientServiceNotaVentaCreate.onGetClientServiceNotaVentaCreateComprobar()
        numNoVeOneNew = ClientServiceNotaVentaCreate.onGetClientServiceNotaVentaCreate()
        numNoVeOneNewNoVe = numNoVeOneNew.count()
        aux = createNumNotaVenta.count() # Cuenta las lineas de la tabla cansta
        numMayor = [] #objeto vacio para contar el numero mayor
        for item in createNumNotaVenta: 
            numMayor.append(item.pfsabcnstnumpf)
        if aux != 0 and numMayor != []: # comparamos que no este vacio
            nMayor = np.max(numMayor) # Sacamos el numero mayor
            if aux == nMayor: # Comparamos si los dos son iguales para crear la factura
                if numNoVeOneNewNoVe == 0:
                    ClientControllerNotaVenta.onGetClientControllerNotaVentaCreateSave(nMayor)

        else:
            ClientControllerNotaVenta.onGetClientControllerNotaVentaCreateSaveInit()


    def onGetClientControllerNotaVentaCreateSaveInit(): # Iniciando la factura
        pfsabcnstnumpf = 1
        pfsabcnstsubtotal = 0
        pfsabcnstdto = 0
        pfsabcnstiva = 0
        pfsabcnstotal = 0
        pfsabcnstestado = 1
        pfsabcnstcreatedat = datetime.now()
        pfsusersid = current_user.iduser
        if pfsabcnstnumpf != '' and pfsabcnstsubtotal != '' and pfsabcnstdto != '' and pfsabcnstiva != '' and pfsabcnstotal != ''and pfsabcnstestado != ''and pfsabcnstcreatedat != '' and pfsusersid !='':
            ClientServiceNotaVentaCreate.onGetClientServiceNotaVentaCreateSave(pfsabcnstnumpf, pfsabcnstsubtotal, pfsabcnstdto, pfsabcnstiva, pfsabcnstotal, pfsabcnstestado, pfsabcnstcreatedat, pfsusersid)
            flash('Creado la Factura correctamente', category='success')
        else:
            flash('Error al crear la factura', category='success')


    def onGetClientControllerNotaVentaCreateSave(nMayor): # Continuar facturando
        pfsabcnstnumpf = nMayor + 1
        pfsabcnstsubtotal = 0
        pfsabcnstdto = 0
        pfsabcnstiva = 0
        pfsabcnstotal = 0
        pfsabcnstestado = 1
        pfsabcnstcreatedat = datetime.now()
        pfsusersid = current_user.iduser
        if pfsabcnstnumpf != '' and pfsabcnstsubtotal != '' and pfsabcnstdto != '' and pfsabcnstiva != '' and pfsabcnstotal != ''and pfsabcnstestado != ''and pfsabcnstcreatedat != '' and pfsusersid !='':
            ClientServiceNotaVentaCreate.onGetClientServiceNotaVentaCreateSave(pfsabcnstnumpf, pfsabcnstsubtotal, pfsabcnstdto, pfsabcnstiva, pfsabcnstotal, pfsabcnstestado, pfsabcnstcreatedat, pfsusersid)
            flash('Creado la Factura correctamente', category='success')
        else:
            flash('Error al crear la factura', category='success')