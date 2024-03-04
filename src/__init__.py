#System

from flask import Flask
from flask_login import LoginManager
from .config.config import Config
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from src.database.database import db, ma
#Admin routes
from src.admin.router.adminRouterUsers import aru
from src.admin.router.adminRouterCategoria import arc
from src.admin.router.adminRouterProducto import arp
# Auth routes
from src.auth.router.routerAuth import rauth
from src.auth.router.routerLoginIn import rlgn
from src.auth.router.routerDataBase import pfsbdmmrb
from src.auth.router.routerLogout import rlgt

# client Routes
from src.client.router.clientRouterNotaVenta import ccnvv
from src.client.router.clientRouterLoginUserAuth import crlua 
from src.client.router.clientRouterDetalleNotaVenta import crdnv 

# middlewares
from src.middlewares.middlewaresLoginIn import UserModel

loginManager = LoginManager()
loginManager.loginView = 'auth.controller.controllerLoginIn'

@loginManager.user_loader
def loadUser(username):
    return UserModel.get(username)

def apprun():
    #Sistem
    app = Flask(__name__)
    app.config.from_object(Config)

    #   Auth
    app.register_blueprint(rauth)
    app.register_blueprint(rlgn)
    app.register_blueprint(pfsbdmmrb)
    app.register_blueprint(rlgt)
    #   Admin
    app.register_blueprint(aru)
    app.register_blueprint(arc)
    app.register_blueprint(arp)

    #   Client
    app.register_blueprint(ccnvv)
    app.register_blueprint(crlua)
    app.register_blueprint(crdnv)
    
    #Sistem
    loginManager.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    bootstrap = Bootstrap(app)
    fa = FontAwesome(app)
    return app



