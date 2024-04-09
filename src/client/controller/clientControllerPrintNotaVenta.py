from flask import request, render_template as render , flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from src.client.services.clientServiceNotaVentaPrint import ClientServiceNotaVentaPrint
from src.middlewares.middlewaresLoginIn import UserModel
from sqlalchemy.exc import SQLAlchemyError
from src.auth.security.securityAuth import SecurityAuth
import numpy as np
from datetime import datetime
from flask_login import current_user, logout_user
from win32 import win32print
class ClientControllerPrintNotaVenta():

    def onGetClientControllerPrintNotaVentaView():
        iduser = 0
        if current_user.is_authenticated:
            idUser = current_user.iduser
        idCanasta = request.form['txtIdCanasta']
        ClientControllerPrintNotaVenta.onGetClientControllerPrintNotaVentaText(idUser, idCanasta)
        ClientControllerPrintNotaVenta.onGetClientControllerPrintNotaVentaPrint()
        logout_user()
        return redirect(url_for('ccnvv.onGetClientControllerNotaVentaView'))
    
    def onGetClientControllerPrintNotaVentaText(idUser, idCanasta): 
        cedula = ""
        nombre = ""
        apellido = ""
        email = ""
        celular = ""

        resultIdUser = ClientServiceNotaVentaPrint.onGetClientServiceNotaVentaPrintUser(idUser)
        resultDetalleCanasta = ClientServiceNotaVentaPrint.onGetClientServiceNotaVentaPrintIdDetalleNotaVenta(idCanasta)
        resultCanasta = ClientServiceNotaVentaPrint.onGetClientServiceNotaVentaPrintIdNotaVenta(idUser, idCanasta)
        for item in resultIdUser:
            cedula = item.pfsuserscedula
            nombre = item.pfsusersnombres
            apellido = item.pfsusersapellidos
            email = item.pfsusersemail
            celular = item.pfsuserscellphone
        
        file = open('src/client/controller/clientrecibo.txt', 'w')
        file.write("*******************************\n")
        file.write("*********Maximarketing*********\n")
        file.write("*******************************\n")
        file.write(f"Cedula:{cedula} \n")
        file.write(f"Nombre:{nombre} \n")
        file.write(f"Apellido:{apellido} \n")
        file.write(f"email:{email} \n")
        file.write(f"celular:{celular} \n")
        file.write("cant  Nombre      Precio  Total \n")

        for item in resultDetalleCanasta:
            textPrint = f"{item.pfsabdcantidad}     {item.pfsabprodnombre}        {item.pfsabdcprecio}    {item.pfsabdctotal}"
            file.write(f"{textPrint} \n")

        file.write(f"\n")

        for item in resultCanasta:
            subtotal = item.pfsabcnstsubtotal
            file.write(f"              Subtotal    {subtotal} \n")
            dto = item.pfsabcnstdto
            file.write(f"              Dto         {dto} \n")
            iva = item.pfsabcnstiva
            file.write(f"              Iva         {iva} \n")
            total = item.pfsabcnstotal
            file.write(f"              Total       {total} \n")
        

        file.close()
    
    def onGetClientControllerPrintNotaVentaPrint():
        
        filePath = "src/client/controller/clientrecibo.txt"
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
        printerName = 'POS-58'
        fileHandle = open(filePath, 'rb')
        printerHandle = win32print.OpenPrinter(printerName)
        jobInfo = win32print.StartDocPrinter(printerHandle, 1 , (filePath, None, "RAW"))
        win32print.StartPagePrinter(printerHandle)
        win32print.WritePrinter(printerHandle, fileHandle.read())
        win32print.EndPagePrinter(printerHandle)
        win32print.EndDocPrinter(printerHandle)