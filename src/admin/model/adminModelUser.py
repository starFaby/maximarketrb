class ModelUser():

    def __init__(self, pfsusersid, pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername, pfsusersemail, pfsuserspassword, pfsusersdireccion, pfsuserscellphone, pfsusersphone, pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat):
        
        self.pfsusersid = pfsusersid
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


    
    #--------------------------
    # get y set pfsusersid
    #--------------------------
    def getpfsusersid(self):
        return self.pfsusersid
    
    def setpfsusersid(self, pfsusersid):
        self.pfsusersid = pfsusersid
    #--------------------------
    # get y set pfsuserscedula
    #--------------------------
    def getpfsuserscedula(self):
        return self.pfsuserscedula
    
    def setpfsuserscedula(self, pfsuserscedula):
        self.pfsuserscedula = pfsuserscedula
    
    #--------------------------
    # get y set pfsusersnombres
    #--------------------------
    def getpfsusersnombres(self):
        return self.pfsusersnombres
    
    def setpfsusersnombres(self, pfsusersnombres):
        self.pfsusersnombres = pfsusersnombres

    #--------------------------
    # get y set pfsusersapellidos
    #--------------------------
    def getpfsusersapellidos(self):
        return self.pfsusersapellidos
    
    def setpfsusersapellidos(self, pfsusersapellidos):
        self.pfsusersapellidos = pfsusersapellidos
    #--------------------------
    # get y set pfsusersusername
    #--------------------------
    def getpfsusersusername(self):
        return self.pfsusersusername
    
    def setpfsusersusername(self, pfsusersusername):
        self.pfsusersusername = pfsusersusername

    #--------------------------
    # get y set pfsusersemail
    #--------------------------
    def getpfsusersemail(self):
        return self.pfsusersemail
    
    def setpfsusersemail(self, pfsusersemail):
        self.pfsusersemail = pfsusersemail

    #--------------------------
    # get y set pfsuserspassword
    #--------------------------
    def getpfsuserspassword(self):
        return self.pfsuserspassword
    
    def setpfsuserspassword(self, pfsuserspassword):
        self.pfsuserspassword = pfsuserspassword

    #--------------------------
    # get y set pfsusersdireccion
    #--------------------------
    def getpfsusersdireccion(self):
        return self.pfsusersdireccion
    
    def setpfsusersdireccion(self, pfsusersdireccion):
        self.pfsusersdireccion = pfsusersdireccion
    

    #--------------------------
    # get y set pfsusersdireccion
    #--------------------------
    def getpfsuserscellphone(self):
        return self.pfsuserscellphone
    
    def setpfsuserscellphone(self, pfsuserscellphone):
        self.pfsuserscellphone = pfsuserscellphone

    #--------------------------
    # get y set pfsusersphone
    #--------------------------
    def getpfsusersphone(self):
        return self.pfsusersphone
    
    def setpfsusersphone(self, pfsusersphone):
        self.pfsusersphone = pfsusersphone

    #--------------------------
    # get y set pfsusersisadmin
    #--------------------------
    def getpfsusersisadmin(self):
        return self.pfsusersisadmin
    
    def setpfsusersisadmin(self, pfsusersisadmin):
        self.pfsusersisadmin = pfsusersisadmin

    #--------------------------
    # get y set pfsusersavatar
    #--------------------------
    def getpfsusersavatar(self):
        return self.pfsusersavatar
    
    def setpfsusersavatar(self, pfsusersavatar):
        self.pfsusersavatar = pfsusersavatar

    #--------------------------
    # get y set pfsusersestado
    #--------------------------
    def getpfsusersestado(self):
        return self.pfsusersestado
    
    def setpfsusersestado(self, pfsusersestado):
        self.pfsusersestado = pfsusersestado

    #--------------------------
    # get y set pfsuserscreatedat
    #--------------------------
    def getpfsuserscreatedat(self):
        return self.pfsuserscreatedat
    
    def setpfsuserscreatedat(self, pfsuserscreatedat):
        self.pfsuserscreatedat = pfsuserscreatedat

    def LoginInJason(self):
        return {
            'pfsusersid':self.pfsusersid,
            'pfsuserscedula':self.pfsuserscedula,
            'pfsusersnombres':self.pfsusersnombres,
            'pfsusersapellidos':self.pfsusersapellidos, 
            'pfsusersusername':self.pfsusersusername, 
            'pfsusersemail':self.pfsusersemail, 
            'pfsuserspassword':self.pfsuserspassword, 
            'pfsusersdireccion':self.pfsusersdireccion, 
            'pfsuserscellphone':self.pfsuserscellphone, 
            'pfsusersphone':self.pfsusersphone, 
            'pfsusersisadmin':self.pfsusersisadmin, 
            'pfsusersavatar':self.pfsusersavatar, 
            'pfsusersestado':self.pfsusersestado, 
            'pfsuserscreatedat':self.pfsuserscreatedat 
            }