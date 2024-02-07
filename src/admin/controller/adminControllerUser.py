from flask import render_template as render, request
from src.admin.services.adminServiceUsers import AdminServiceUser
from sqlalchemy.exc import SQLAlchemyError
from src.auth.security.securityAuth import SecurityAuth

class AdminControllerUser:

    def onGetAdminControllerUserList():
        print("request.headers")
        print(request.headers)
        hasAccess = SecurityAuth.verifyAuthToken(request.headers)
        print(hasAccess)
        #if hasAccess:
        try:
            users = AdminServiceUser.ongetAdminServiceUser()
            if users is not None:
                return render("admin/adminUsers.html", users = users)
            else:
                return render("admin/adminUsers.html", users = users)
        except SQLAlchemyError as e:
                print("Error en Service User ", e)
                return render('errors/error500.html')    
        #else:
            #return render('errors/error401.html')