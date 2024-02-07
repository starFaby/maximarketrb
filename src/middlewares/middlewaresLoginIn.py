from flask_login import UserMixin
from src.auth.services.serviceAuth import ServiceAuth
class UserModel(UserMixin):
    def __init__(self, userData):
        self.id = userData.pfsusersusername
        self.iduser = userData.pfsusersid
        self.password = userData.pfsuserspassword
        self.email = userData.pfsusersemail
        self.avatar = userData.pfsusersavatar
        self.isadmin = userData.pfsusersisadmin
        self.estado = userData.pfsusersestado
        
    @staticmethod
    def get(pfsusersusername):
        userData = ServiceAuth.onGetUserByUserName(pfsusersusername = pfsusersusername)
        return UserModel(userData)