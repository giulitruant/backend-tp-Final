from Include.Model.model import Solicitud_Detalle
from Include.Model.model import db
from Include.UI.Solicitud import UISolicitud
from Include.UI.Producto import UIProducto
from sqlalchemy import exc

class UISolicitudDetalle(): 
    def Alta(self,nro_sol,cant,prod):
        try:
            if self.validaSolicitud():
                SolDet = Solicitud_Detalle(nro_solicitud = nro_sol , cantidad = cant , id_prod = prod)
                db.session.add(SolDet)
                db.session.commit()
                return 'ok'
            else:
                return 'Error en generar la solicitud'
        except TypeError as ex:
            return 'Error de servicio'


    def validaSolicitud(self,nro_sol,cant,prod):
        try:
            if not nro_sol is None:
                sol = UISolicitud()
                validaSol = sol.buscarSolicitud(id_sol=nro_sol)
                if not cant is None and not prod is None:
                    p = UIProducto()
                    pr = p.buscarProducto(prod)
                    if not p is None:
                        if cant > pr.cant_stock:
                            return True
        except Exception as ex:
            print(ex)
            return False



                

