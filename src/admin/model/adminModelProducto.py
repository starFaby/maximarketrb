class ModelProducto():
    def __init__(self, pfsabprodid, pfsabprodserial,  pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid):

        self.pfsabprodid = pfsabprodid
        self.pfsabprodserial = pfsabprodserial 
        self.pfsabprodnombre = pfsabprodnombre 
        self.pfsabprodimage = pfsabprodimage
        self.pfsabproddetalle = pfsabproddetalle
        self.pfsabprodprecio = pfsabprodprecio
        self.pfsabprodstock = pfsabprodstock
        self.pfsabprodestado = pfsabprodestado
        self.pfsabprodcreatedat = pfsabprodcreatedat
        self.pfsabcategoriaid = pfsabcategoriaid

    # get y set pfsabprodid
    def getpfsabprodid(self):
        return self.pfsabprodid
    
    def setpfsabprodid(self, pfsabprodid):
        self.pfsabprodid = pfsabprodid

    
    #get y set pfsabprodserial
    def getpfsabprodserial(self):
        return self.pfsabprodserial
    
    def setpfsabprodserial(self, pfsabprodserial):
        self.pfsabprodserial = pfsabprodserial


    #get y set pfsabprodnombre
    def getpfsabprodnombre(self):
        return self.pfsabprodnombre
    
    def setpfsabprodnombre(self, pfsabprodnombre):
        self.pfsabprodnombre = pfsabprodnombre

    #get y set pfsabprodimage
    def getpfsabprodimage(self):
        return self.pfsabprodimage
    
    def setpfsabprodimage(self, pfsabprodimage):
        self.pfsabprodimage = pfsabprodimage

    # get y set  pfsabproddetalle
    def getpfsabproddetalle(self):
        return self.pfsabproddetalle
    
    def setpfsabproddetalle(self, pfsabproddetalle):
        self.pfsabproddetalle = pfsabproddetalle


    #get y set pfsabprodprecio
    def getpfsabprodprecio(self):
        return self.pfsabprodprecio
    
    def setpfsabprodprecio(self, pfsabprodprecio):
        self.pfsabprodprecio = pfsabprodprecio

    #get y set pfsabprodstock
    def getpfsabprodstock(self):
        return self.pfsabprodstock
    
    def setpfsabprodstock(self, pfsabprodstock):
        self.pfsabprodstock = pfsabprodstock

    #get y set pfsabprodestado
    def getpfsabprodestado(self):
        return self.pfsabprodestado
    
    def setpfsabprodestado(self, pfsabprodestado):
        self.pfsabprodestado = pfsabprodestado

    #get y set pfsabprodcreatedat
    def getpfsabprodcreatedat(self):
        return self.pfsabprodcreatedat
    
    def setpfsabprodcreatedat(self, pfsabprodcreatedat):
        self.pfsabprodcreatedat = pfsabprodcreatedat

    # get y set pfsabcategoriaid
    def getpfsabcategoriaid(self):
        return self.pfsabcategoriaid
    
    def setpfsabcategoriaid(self , pfsabcategoriaid):
        self.pfsabcategoriaid = pfsabcategoriaid

    def LoginInJason(self):
        return {
            'pfsabprodid' : self.pfsabprodid,
            'pfsabprodnombre' : self.pfsabprodserial,
            'pfsabprodnombre' : self.pfsabprodnombre,
            'pfsabprodimage' : self.pfsabprodimage,
            'pfsabproddetalle' : self.pfsabproddetalle,
            'pfsabprodprecio' : self.pfsabprodprecio,
            'pfsabprodstock' : self.pfsabprodstock,
            'pfsabprodprecio' : self.pfsabprodprecio,
            'pfsabprodestado' : self.pfsabprodestado,
            'pfsabprodcreatedat' : self.pfsabprodcreatedat,
            'pfsabcategoriaid' : self.pfsabcategoriaid
            }