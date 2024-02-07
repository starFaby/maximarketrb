from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from src.admin.model.adminModelProducto import ModelProducto
import datetime

class AdminServiceProducto:
    
    @classmethod
    def ongetAdminServiceProducto(self, page):
        try:
            page = page
            pages = 10
            productoList = Producto.query.order_by(Producto.pfsabprodid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            return productoList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def ongetAdminServiceProductoName(self, search, page):
        try:
            page = page
            pages = 10
            productoList = Producto.query.filter(Producto.pfsabprodnombre.like(search)).paginate(per_page=pages,error_out=False)
            return productoList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)

    @classmethod    
    def onGetAdminServiceProductoSave(self,pfsabprodserial, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid):
        try:
            modelProducto = ModelProducto(0,pfsabprodserial, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid)
            
            newProducto = Producto( pfsabprodserial = modelProducto.getpfsabprodserial(), 
                                    pfsabprodnombre = modelProducto.getpfsabprodnombre(),
                                    pfsabprodimage = modelProducto.getpfsabprodimage(), 
                                    pfsabproddetalle = modelProducto.getpfsabproddetalle(), 
                                    pfsabprodprecio = modelProducto.getpfsabprodprecio(), 
                                    pfsabprodstock = modelProducto.getpfsabprodstock(), 
                                    pfsabprodestado = modelProducto.getpfsabprodestado(), 
                                    pfsabprodcreatedat = modelProducto.getpfsabprodcreatedat(),
                                    pfsabcategoriaid = modelProducto.getpfsabcategoriaid())
            db.session.add(newProducto)
            db.session.commit()

        except SQLAlchemyError as e:
            return render('errors/error500.html', e)