class ModelNotaVenta():
    def __init__(self, pfsabcnstid, pfsabcnstnumpf, pfsabcnstsubtotal, pfsabcnstdto, pfsabcnstiva, pfsabcnstotal, pfsabcnstestado, pfsabcnstcreatedat, pfsusersid):
        self.pfsabcnstid = pfsabcnstid
        self.pfsabcnstnumpf = pfsabcnstnumpf
        self.pfsabcnstsubtotal = pfsabcnstsubtotal
        self.pfsabcnstdto = pfsabcnstdto
        self.pfsabcnstiva = pfsabcnstiva
        self.pfsabcnstotal = pfsabcnstotal
        self.pfsabcnstestado = pfsabcnstestado
        self.pfsabcnstcreatedat = pfsabcnstcreatedat
        self.pfsusersid = pfsusersid

    #--------------------
    #--------------------
    # get y set pfsabcnstid
    #---------------------
    #---------------------
    def getpfsabcnstid(self):
        return self.pfsabcnstid
    
    def setpfsabcnstid(self, pfsabcnstid):
        self.pfsabcnstid = pfsabcnstid

    #--------------------
    #--------------------
    # get y set pfsabcnstnumpf
    #---------------------
    #---------------------
    def getpfsabcnstnumpf(self):
        return self.pfsabcnstnumpf
    
    def setpfsabcnstnumpf(self, pfsabcnstnumpf):
        self.pfsabcnstnumpf = pfsabcnstnumpf

    #--------------------
    #--------------------
    # get y set pfsabcnstsubtotal
    #---------------------
    #---------------------
    def getpfsabcnstsubtotal(self):
        return self.pfsabcnstsubtotal
    
    def setpfsabcnstsubtotal(self, pfsabcnstsubtotal):
        self.pfsabcnstsubtotal = pfsabcnstsubtotal

    #--------------------
    #--------------------
    # get y set pfsabcnstdto
    #---------------------
    #---------------------
    def getpfsabcnstdto(self):
        return self.pfsabcnstdto
    
    def setpfsabcnstdto(self, pfsabcnstdto):
        self.pfsabcnstdto = pfsabcnstdto

    #--------------------
    #--------------------
    # get y set pfsabcnstiva
    #---------------------
    #---------------------
    def getpfsabcnstiva(self):
        return self.pfsabcnstiva
    
    def setpfsabcnstiva(self, pfsabcnstiva):
        self.pfsabcnstiva = pfsabcnstiva

    #--------------------
    #--------------------
    # get y set pfsabcnstotal
    #---------------------
    #---------------------
    def getpfsabcnstotal(self):
        return self.pfsabcnstotal
    
    def setpfsabcnstotal(self, pfsabcnstotal):
        self.pfsabcnstotal = pfsabcnstotal


    #--------------------
    #--------------------
    # get y set pfsabcnstestado
    #---------------------
    #---------------------
    def getpfsabcnstestado(self):
        return self.pfsabcnstestado
    
    def setpfsabcnstestado(self, pfsabcnstestado):
        self.pfsabcnstestado = pfsabcnstestado

    #--------------------
    #--------------------
    # get y set pfsabcnstcreatedat
    #---------------------
    #---------------------
    def getpfsabcnstcreatedat(self):
        return self.pfsabcnstcreatedat
    
    def setpfsabcnstcreatedat(self, pfsabcnstcreatedat):
        self.pfsabcnstcreatedat = pfsabcnstcreatedat

    #--------------------
    #--------------------
    # get y set pfsusersid
    #---------------------
    #---------------------
    def getpfsusersid(self):
        return self.pfsusersid
    
    def setpfsusersid(self, pfsusersid):
        self.pfsusersid = pfsusersid

    def ModelNotaVentaJason(self):
        return {
            'pfsabcnstid' : self.pfsabcnstid,
            'pfsabcnstnumpf' : self.pfsabcnstnumpf,
            'pfsabcnstsubtotal' : self.pfsabcnstsubtotal,
            'pfsabcnstdto' : self.pfsabcnstdto,
            'pfsabcnstiva' : self.pfsabcnstiva,
            'pfsabcnstotal' : self.pfsabcnstotal,
            'pfsabcnstestado' : self.pfsabcnstestado,
            'pfsabcnstcreatedat' : self.pfsabcnstcreatedat,
            'pfsusersid' : self.pfsusersid
            }
        

