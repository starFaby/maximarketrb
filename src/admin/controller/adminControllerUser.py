from flask import render_template as render, request, flash, redirect, url_for
from src.admin.services.adminServiceUsers import AdminServiceUser
from sqlalchemy.exc import SQLAlchemyError
from src.auth.security.securityAuth import SecurityAuth
from datetime import datetime

class AdminControllerUser:
    
    def onGetAdminControllerUserList(page):
        try:
            page = page
            users = AdminServiceUser.ongetAdminServiceUser(page)
            if users != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    users = AdminServiceUser.ongetAdminServiceUserName(search, page)
                    return render("admin/adminUsers.html", users=users, tag = tag)
                else:
                    flash('Categorias Listadas', category='success')
                    return render("admin/adminUsers.html", users=users)
            else:
                flash('No existe categorias', category='success')
                return render("admin/adminUsers.html", users=users)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
    
    def onGetAdminControllerUserSaveView():
        view = 1
        users = []
        return render("admin/adminUsers.html", view=view, users=users)
    
    def onGetAdminControllerUserSave():
        pfsuserscedula = request.form['txtCedula']
        pfsusersnombres = request.form['txtNombres']
        pfsusersapellidos = request.form['txtApellidos']
        pfsusersusername = request.form['txtUsername']
        pfsusersemail = request.form['txtEmail']
        pfsuserspassword = "mmrb2024"
        pfsusersdireccion = request.form['txtDireccion']
        pfsuserscellphone = request.form['txtCelular']
        pfsusersphone = request.form['txtTelefono']
        pfsusersisadmin = False
        pfsusersavatar = "https://res.cloudinary.com/dfqa22y7u/image/upload/v1708548108/aux/notimgaval_xlgtpm.webp"
        pfsusersestado = request.form['txtCedula']
        pfsuserscreatedat = datetime.now()
        if  pfsuserscedula != '' and pfsusersnombres != '' and pfsusersapellidos != '' and pfsusersusername != '' and pfsusersemail != '' and pfsuserspassword != '' and pfsusersdireccion != '' and pfsuserscellphone != '' and pfsusersphone != '' and pfsusersisadmin != '' and pfsusersavatar != '' and pfsusersestado != 'Elija...' and pfsuserscreatedat != '':
            AdminServiceUser.onGetAdminServiceUserSave(pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername, pfsusersemail, pfsuserspassword, pfsusersdireccion, pfsuserscellphone, pfsusersphone, pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat)
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('aru.onGetAdminControllerUserList')) 
        else:
            flash('LLene los campos completos porfabor', category='success')
            print("Datos vacios")
            return redirect(url_for('aru.onGetAdminControllerUserList'))  
