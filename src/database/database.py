from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

#---------------------------
#drop database flaskmysql
#create database flaskmysql
#---------------------------

#----------------------------
#----------usuario----------
#--------------------------
class User(db.Model):
    __tablename__='pfsusers'

    pfsusersid = db.Column(db.Integer, primary_key=True)
    pfsuserscedula = db.Column(db.String(80), nullable=False)
    pfsusersnombres = db.Column(db.String(80), nullable=False)
    pfsusersapellidos = db.Column(db.String(80), nullable=False)
    pfsusersusername = db.Column(db.String(30), unique=True, nullable=False)
    pfsusersemail = db.Column(db.String(120), nullable=False)
    pfsuserspassword = db.Column(db.String(250), nullable=True)
    pfsusersdireccion = db.Column(db.String(100), nullable=True)
    pfsuserscellphone = db.Column(db.String(25), nullable=False)
    pfsusersphone = db.Column(db.String(20), nullable=False)
    pfsusersisadmin = db.Column(db.Boolean, default=False)
    pfsusersavatar = db.Column(db.String(250), nullable=True)
    pfsusersestado = db.Column(db.String(1), nullable=True)
    pfsuserscreatedat = db.Column(db.Date, nullable=True) 

    def onGetSetPassword(self, pfsuserspassword):
        self.pfsuserspassword = generate_password_hash(pfsuserspassword)

    def onGetCheckPassword(self, pfsuserspassword):
        return check_password_hash(self.pfsuserspassword, pfsuserspassword)

    def __init__(self, pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername, pfsusersemail, pfsuserspassword, pfsusersdireccion,  pfsuserscellphone, pfsusersphone, pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat):
        self.pfsuserscedula = pfsuserscedula
        self.pfsusersnombres = pfsusersnombres
        self.pfsusersapellidos = pfsusersapellidos
        self.pfsusersusername = pfsusersusername
        self.pfsusersemail = pfsusersemail
        self.pfsuserspassword = pfsuserspassword 
        self.pfsusersdireccion = pfsusersdireccion 
        self.pfsuserscellphone = pfsuserscellphone
        self.pfsusersphone = pfsusersphone
        self.pfsusersisadmin = pfsusersisadmin
        self.pfsusersavatar = pfsusersavatar
        self.pfsusersestado = pfsusersestado
        self.pfsuserscreatedat = pfsuserscreatedat

class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsusersid', 'pfsuserscedula', 'pfsusersnombres', 'pfsusersapellidos', 'pfsusersusername', 'pfsusersemail', 'pfsuserspassword', 'pfsusersdireccion',  'pfsuserscellphone', 'pfsusersphone', 'pfsusersisadmin', 'pfsusersavatar', 'pfsusersestado', 'pfsuserscreatedat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

#-----------------------------------------------------------
#---------------CATEGORIA----------------------------------
#----------------------------------------------------------

class Categoria(db.Model):
    __tablename__='pfsabcategorias'

    pfsabcateid = db.Column(db.Integer, primary_key=True)
    pfsabcatenombre = db.Column(db.String(120), nullable=False)
    pfsabcateimage = db.Column(db.String(300), nullable=False)
    pfsabcatedetalle = db.Column(db.String(300), nullable=False)
    pfsabcateestado = db.Column(db.String(1), nullable=True)
    pfsabcatecreatedat = db.Column(db.String(11), nullable=True) 


    def __init__(self, pfsabcatenombre, pfsabcateimage, pfsabcatedetalle , pfsabcateestado, pfsabcatecreatedat):
        self.pfsabcatenombre = pfsabcatenombre
        self.pfsabcateimage = pfsabcateimage
        self.pfsabcatedetalle = pfsabcatedetalle
        self.pfsabcateestado = pfsabcateestado
        self.pfsabcatecreatedat = pfsabcatecreatedat

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('pfsabcateid','pfsabcatenombre', 'pfsabcateimage', 'pfsabcatedetalle', 'pfsabcateestado', 'pfsabcatecreatedat')

categoriaSchema = CategoriaSchema()
categoriaSchema = CategoriaSchema(many=True)

#----------------------------
#----------PRODUCTO----------
#--------------------------
class Producto(db.Model):
    __tablename__='pfsabproductos'

    pfsabprodid = db.Column(db.Integer, primary_key=True)
    pfsabprodserial = db.Column(db.String(80), nullable=False)
    pfsabprodnombre = db.Column(db.String(80), nullable=False)
    pfsabprodimage = db.Column(db.String(300), nullable=False)
    pfsabproddetalle = db.Column(db.String(300), nullable=False)
    pfsabprodprecio = db.Column(db.String(6), nullable=False) #double
    pfsabprodstock = db.Column(db.String(10), nullable=False) #int
    pfsabprodestado = db.Column(db.String(1), nullable=True)
    pfsabprodcreatedat = db.Column(db.String(11), nullable=True) 
    
    pfsabcategoriaid = db.Column(db.Integer, db.ForeignKey('pfsabcategorias.pfsabcateid',ondelete='CASCADE'), nullable=False)
    pfsabcategoria = db.relationship('Categoria',backref=db.backref('pfsabproductos',lazy=True))


    def __init__(self, pfsabprodserial, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid):
        self.pfsabprodserial = pfsabprodserial
        self.pfsabprodnombre = pfsabprodnombre
        self.pfsabprodimage = pfsabprodimage
        self.pfsabproddetalle = pfsabproddetalle
        self.pfsabprodprecio = pfsabprodprecio
        self.pfsabprodstock = pfsabprodstock
        self.pfsabprodestado = pfsabprodestado
        self.pfsabprodcreatedat = pfsabprodcreatedat
        self.pfsabcategoriaid = pfsabcategoriaid
class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('pfsabprodid', 'pfsabprodserial' ,'pfsabprodnombre', 'pfsabprodimage', 'pfsabproddetalle', 'pfsabprodprecio', 'pfsabprodstock', 'pfsabprodestado', 'pfsabprodcreatedat','pfsabcategoriaid')

productoSchema = ProductoSchema()
productoSchema = ProductoSchema(many=True)