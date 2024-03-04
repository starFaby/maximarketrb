class ModelDetalleNotaVenta():
    def __init__(self, pfsabdcid, pfsabdcnumpf, pfsabdcantidad, pfsabdcprecio, pfsabdctotal, pfsabdcestado, pfsabdcreatedat, pfsabproductoid, pfsabcanastaid):
        self.pfsabdcid = pfsabdcid
        self.pfsabdcnumpf = pfsabdcnumpf
        self.pfsabdcantidad = pfsabdcantidad
        self.pfsabdcprecio = pfsabdcprecio
        self.pfsabdctotal = pfsabdctotal
        self.pfsabdcestado = pfsabdcestado
        self.pfsabdcreatedat = pfsabdcreatedat
        self.pfsabproductoid = pfsabproductoid
        self.pfsabcanastaid = pfsabcanastaid
    #--------------------
    #--------------------
    # get y set pfsabdcid
    #---------------------
    #---------------------
    def getpfsabdcid(self):
        return self.pfsabdcid
    
    def setpfsabdcid(self, pfsabdcid):
        self.pfsabdcid = pfsabdcid

    #--------------------
    #--------------------
    # get y set pfsabdcnumpf
    #---------------------
    #---------------------
    def getpfsabdcnumpf(self):
        return self.pfsabdcnumpf
    
    def setpfsabdcnumpf(self, pfsabdcnumpf):
        self.pfsabdcnumpf = pfsabdcnumpf

    #--------------------
    #--------------------
    # get y set pfsabdcantidad
    #---------------------
    #---------------------
    def getpfsabdcantidad(self):
        return self.pfsabdcantidad
    
    def setpfsabdcantidad(self, pfsabdcantidad):
        self.pfsabdcantidad = pfsabdcantidad


    #--------------------
    #--------------------
    # get y set pfsabdcprecio
    #---------------------
    #---------------------
    def getpfsabdcprecio(self):
        return self.pfsabdcprecio
    
    def setpfsabdcprecio(self, pfsabdcprecio):
        self.pfsabdcprecio = pfsabdcprecio

    #--------------------
    #--------------------
    # get y set pfsabdctotal
    #---------------------
    #---------------------
    def getpfsabdctotal(self):
        return self.pfsabdctotal
    
    def setpfsabdctotal(self, pfsabdctotal):
        self.pfsabdctotal = pfsabdctotal

    #--------------------
    #--------------------
    # get y set pfsabdcestado
    #---------------------
    #---------------------
    def getpfsabdcestado(self):
        return self.pfsabdcestado
    
    def setpfsabdcestado(self, pfsabdcestado):
        self.pfsabdcestado = pfsabdcestado

    
    #--------------------
    #--------------------
    # get y set pfsabdcreatedat
    #---------------------
    #---------------------
    def getpfsabdcreatedat(self):
        return self.pfsabdcreatedat
    
    def setpfsabdcreatedat(self, pfsabdcreatedat):
        self.pfsabdcreatedat = pfsabdcreatedat

    #--------------------
    #--------------------
    # get y set pfsabproductoid
    #---------------------
    #---------------------
    def getpfsabproductoid(self):
        return self.pfsabproductoid
    
    def setpfsabproductoid(self, pfsabproductoid):
        self.pfsabproductoid = pfsabproductoid   

    #--------------------
    #--------------------
    # get y set pfsabcanastaid
    #---------------------
    #---------------------
    def getpfsabcanastaid(self):
        return self.pfsabcanastaid
    
    def setpfsabcanastaid(self, pfsabcanastaid):
        self.pfsabcanastaid = pfsabcanastaid  


    def LoginInJason(self):
        return {
            'pfsabdcid' : self.pfsabdcid,
            'pfsabdcnumpf' : self.pfsabdcnumpf,
            'pfsabdcantidad' : self.pfsabdcantidad,
            'pfsabdcprecio' : self.pfsabdcprecio,
            'pfsabdctotal' : self.pfsabdctotal,
            'pfsabdcestado' : self.pfsabdcestado,
            'pfsabdcreatedat' : self.pfsabdcreatedat,
            'pfsabproductoid' : self.pfsabproductoid,
            'pfsabcanastaid' : self.pfsabcanastaid
            }
