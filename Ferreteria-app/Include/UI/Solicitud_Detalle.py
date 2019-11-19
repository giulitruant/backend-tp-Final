from Include.Model.model import SolicitudDetalle
from Include.Model.model import db
from Include.UI.Solicitud import UISolicitud
from Include.UI.Producto import UIProducto
from sqlalchemy import exc

class UISolicitudDetalle(): 
    def Alta(self,nro_sol,cant,prod):
        try:
            if self.validaSolicitud():
                SolDet = SolicitudDetalle(nro_solicitud = nro_sol , cantidad = cant , id_prod = prod)
                db.session.add(SolDet)
                db.session.commit()
                return SolDet
            else:
                return None
        except TypeError as ex:
            return 'Error de servicio'

    def getListDetalleSolicitud(self, id_sol):
        try:
            listDet = SolicitudDetalle.query.filter_by(nroSolicitud = id_sol).all()
            return listDet
        except exc.SQLAlchemyError as e:
            print(e.args)
            return 'Error de servicio'


    def validaSolicitud(self,nro_sol,cant,prod):
        try:
            if not nro_sol is None:
                sol = UISolicitud()
                validaSol = sol.buscarSolicitud(nro_sol)
                if not cant is None and not prod is None:
                    p = UIProducto()
                    pr = p.buscarProducto(prod)
                    if not p is None:
                        if cant > pr.cant_stock:
                            return True
        except Exception as ex:
            print(ex)
            return False

    def getSolicitudDetalle(self, nroSol):

        try:
            if not nroSol is None and nroSol != '':
                detSolicitud = UISolicitud.query.filter_by(nroSolicitud=nroSol).all()
                if not detSolicitud is None:
                    return detSolicitud
                else:
                    return 'No existe detalles de solicitud con dicho nro de solicitud'
            else:
                return 'Nro solicitud invalida'
        
        except TypeError as e:
            print('Error:'+ e)
            return 'Error de servicio'
                


