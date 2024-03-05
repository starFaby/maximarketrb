# ingresar al sistema ya registrado
from flask import request, render_template as render , flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from src.client.services.clientServiceNumNotaVentaUser import ClientServiceNumNotaVentaUser
from src.client.services.clientServiceDetalleNotaVenta import ClientServiceDetalleNotaVenta
from datetime import datetime

class ClientControllerDetalleNotaVenta():
    
    def onGetClientControllerDetalleNotaVentaSave():
        idCanasta = 0
        cnstNum = 0
        auxIdNumUser = ClientServiceNumNotaVentaUser.onGetClientServiceNumNotaVentaUser()
        #detalleNoVe = ClientServiceDetalleNotaVenta.onGetClientServiceDetalleNotaVentaAll()
        for item in auxIdNumUser:
            idCanasta = item.pfsabcnstid
            cnstNum = item.pfsabcnstnumpf
        numIdUser = auxIdNumUser.count()
        if numIdUser != 0:
            if idCanasta == cnstNum:
                pfsabdcnumpf = cnstNum
                pfsabdcantidad = request.form['txtCantidad']
                pfsabdcprecio = request.form['txtPrecio']
                pfsabdctotal = request.form['txtTotal']
                pfsabdcestado = 1
                pfsabdcreatedat = datetime.now()
                pfsabproductoid = request.form['txtIdProducto']
                pfsabcanastaid = idCanasta

                if pfsabdcnumpf != '' and pfsabdcantidad != '' and pfsabdcprecio != '' and pfsabdctotal != '' and pfsabdcestado != '' and  pfsabdcreatedat != '' and pfsabproductoid != '' and pfsabcanastaid != '':
                    ClientServiceDetalleNotaVenta.onGetClientServiceDetalleNotaVentaSave(pfsabdcnumpf, pfsabdcantidad, pfsabdcprecio, pfsabdctotal, pfsabdcestado, pfsabdcreatedat, pfsabproductoid, pfsabcanastaid)
                    flash('Producto Listadas', category='success')
                    return render('client/clientNotaVenta.html')
                else:
                    flash('No se pudo Guardar', category='info')
                    return render('client/clientNotaVenta.html')
            else:
                flash('La Canasta y el Numero de usuario no coicide', category='info')
                return render('client/clientNotaVenta.html')
        else:
            flash('El Usuario no Existe', category='info')
            return render('client/clientNotaVenta.html')

    
    
                    

