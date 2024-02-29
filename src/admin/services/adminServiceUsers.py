from flask import render_template as render
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from src.admin.model.adminModelUser import ModelUser

class AdminServiceUser:
    
    @classmethod
    def ongetAdminServiceUser(self, page):
        try:
            page = page
            pages = 10
            userList = User.query.order_by(User.pfsusersid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            return userList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def ongetAdminServiceUserName(self, search, page):
        try:
            page = page
            pages = 10
            userList = User.query.filter(User.pfsusersnombres.like(search)).paginate(per_page=pages,error_out=False)
            return userList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
    @classmethod
    def onGetAdminServiceUserSave(self, pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername, pfsusersemail, pfsuserspassword, pfsusersdireccion, pfsuserscellphone, pfsusersphone, pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat):
        try:
            modelUser = ModelUser(0, pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername,
                                pfsusersemail, pfsuserspassword, pfsusersdireccion, pfsuserscellphone, pfsusersphone, 
                                pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat)
            
            newUser = User( pfsuserscedula = modelUser.getpfsuserscedula(), 
                                    pfsusersnombres = modelUser.getpfsusersnombres(),
                                    pfsusersapellidos = modelUser.getpfsusersapellidos(), 
                                    pfsusersusername = modelUser.getpfsusersusername(), 
                                    pfsusersemail = modelUser.getpfsusersemail(), 
                                    pfsuserspassword = modelUser.getpfsuserspassword(), 
                                    pfsusersdireccion = modelUser.getpfsusersdireccion(), 
                                    pfsuserscellphone = modelUser.getpfsuserscellphone(),
                                    pfsusersphone = modelUser.getpfsusersphone(),
                                    pfsusersisadmin = modelUser.getpfsusersisadmin(),
                                    pfsusersavatar = modelUser.getpfsusersavatar(),
                                    pfsusersestado = modelUser.getpfsusersestado(),
                                    pfsuserscreatedat = modelUser.getpfsuserscreatedat())
            newUser.onGetSetPassword(pfsuserspassword = modelUser.getpfsuserspassword())
            db.session.add(newUser)
            db.session.commit()

        except SQLAlchemyError as e:
            return render('errors/error500.html', e)