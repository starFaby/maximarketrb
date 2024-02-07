class ModelCategoria():
    def __init__(self, pfsabcateid, pfsabcatenombre, pfsabcateimage, pfsabcatedetalle, pfsabcateestado, pfsabcatecreatedat) -> None:

        self.pfsabcateid = pfsabcateid
        self.pfsabcatenombre = pfsabcatenombre
        self.pfsabcateimage = pfsabcateimage
        self.pfsabcatedetalle = pfsabcatedetalle
        self.pfsabcateestado = pfsabcateestado
        self.pfsabcatecreatedat = pfsabcatecreatedat

    # get y set id
    def getpfsabcateid(self):
        return self.pfsabcateid
    
    def setpfsabcateid(self, pfsabcateid):
        self.pfsabcateid = pfsabcateid

    # get y set pfspcrcatenombre
    def getpfsabcatenombre(self):
        return self.pfsabcatenombre
    
    def setpfsabcatenombre(self, pfsabcatenombre):
        self.pfsabcatenombre = pfsabcatenombre

    # get y set pfsabcateimage
    def getpfsabcateimage(self):
        return self.pfsabcateimage
    
    def setpfsabcateimage(self, pfsabcateimage):
        self.pfsabcateimage = pfsabcateimage

    # get y set pfsabcatedetalle
    def getpfsabcatedetalle(self):
        return self.pfsabcatedetalle
    
    def setpfsabcatedetalle(self, pfsabcatedetalle):
        self.pfsabcatedetalle = pfsabcatedetalle

    # get y set pfspcrcateestado
    def getpfsabcateestado(self):
        return self.pfsabcateestado
    
    def setpfsabcateestado(self, pfsabcateestado):
        self.pfsabcateestado = pfsabcateestado

    
    # get y set pfsabcatecreatedat
    def getpfsabcatecreatedat(self):
        return self.pfsabcatecreatedat
    
    def setpfsabcatecreatedat(self, pfsabcatecreatedat):
        self.pfsabcatecreatedat = pfsabcatecreatedat



    def LoginInJason(self):
        return {
            'pfsabcateid' : self.pfsabcateid,
            'pfsabcatenombre' : self.pfsabcatenombre,
            'pfsabcateimage' : self.pfsabcateimage,
            'pfsabcatedetalle' : self.pfsabcatedetalle,
            'pfsabcateestado' : self.pfsabcateestado,
            'pfsabcatecreatedat' : self.pfsabcatecreatedat,
            }