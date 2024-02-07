from flask import render_template as render, request, flash, redirect, url_for
from src.admin.services.adminServiceCategoria import AdminServiceCategoria
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from src.admin.model.adminModelCategoria import ModelCategoria


class AdminControllerCategoria:

    def onGetAdminControllerCategoriaList(page):
        try:
            page = page
            categorias = AdminServiceCategoria.ongetAdminServiceCategoria(page)
            if categorias != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    categorias = AdminServiceCategoria.ongetAdminServiceCategoriaName(search, page)
                    return render("admin/adminCategoria.html", categorias=categorias, tag = tag)
                else:
                    flash('Categorias Listadas', category='success')
                    return render("admin/adminCategoria.html", categorias=categorias)
            else:
                flash('No existe categorias', category='success')
                return render("admin/adminCategoria.html", categorias=categorias)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
        
    def onGetControllerAdminCategoriaSave():

        pfsabcatenombre = request.form['txtNombre']
        pfsabcateimage = request.form['txtImage']
        pfsabcatedetalle = request.form['txtDetalle']
        pfsabcateestado = request.form['selectEstado']
        pfsabcatecreatedat = datetime.now()

        if pfsabcatenombre != '' and pfsabcateimage != '' and pfsabcatedetalle != '' and pfsabcateestado != 'Elija...' and pfsabcatecreatedat != '':
            AdminServiceCategoria.onGetAdminServiceCategoriaSave(pfsabcatenombre, pfsabcateimage, pfsabcatedetalle, pfsabcateestado, pfsabcatecreatedat)
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('arc.onGetAdminControllerCategoriaList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            return redirect(url_for('arc.onGetAdminControllerCategoriaList'))  