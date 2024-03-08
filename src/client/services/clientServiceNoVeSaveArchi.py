from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
import datetime
from src.client.model.clientModelNotaVenta import ModelNotaVenta
import pandas as pd

class ClientServiceNotaVentaSaveArchiv:

    @classmethod
    def onGetClientServiceNotaVentaSaveArchiv(self, idCanasta, pfsabcnstsubtotal, pfsabcnstdto, pfsabcnstiva, pfsabcnstotal):
        idCanasta = idCanasta
        pfsabcnstid = 0
        pfsabcnstnumpf = 0
        pfsabcnstestado = 0
        pfsabcnstcreatedat = 0
        pfsusersid = 0

        canasta = Canasta.query.get(idCanasta)
        modelNoVeSavArch = ModelNotaVenta(pfsabcnstid, pfsabcnstnumpf, pfsabcnstsubtotal, pfsabcnstdto, pfsabcnstiva, pfsabcnstotal, pfsabcnstestado, pfsabcnstcreatedat, pfsusersid)

        canasta.pfsabcnstsubtotal = modelNoVeSavArch.getpfsabcnstsubtotal()
        canasta.pfsabcnstdto = modelNoVeSavArch.getpfsabcnstdto()
        canasta.pfsabcnstiva = modelNoVeSavArch.getpfsabcnstiva()
        canasta.pfsabcnstotal = modelNoVeSavArch.getpfsabcnstotal()

        if pfsabcnstsubtotal != '' and pfsabcnstdto != '' and pfsabcnstiva != '' and pfsabcnstotal != '':
            db.session.commit()
            return True
        else:
            return False