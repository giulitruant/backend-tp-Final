from Include.Model.model import SolicitudDetalle
from Include.Model.model import db
from Include.UI.Solicitud import UISolicitud
from Include.UI.Producto import UIProducto
from sqlalchemy import exc, func

class UISolicitudDetalle(): 
    def Alta(self,nro_sol, detalles):
        try:
            for x in detalles:
                if self.validaSolicitud(nro_sol, 1, x['id']):
                    SolDet = SolicitudDetalle(nroSolicitud = nro_sol , cantidad = 1 , idProd = x['id'])
                    db.session.add(SolDet)
                    db.session.commit()
                else:
                    return None
            return SolDet
        except TypeError as ex:
            return 'Error de servicio'

    def getListDetalleSolicitud(self, id_sol):
        try:
            #listDet = SolicitudDetalle.query.filter_by(nroSolicitud = id_sol).all()
            listDet = SolicitudDetalle.query.with_entities(SolicitudDetalle.idDetalle,
                                                           SolicitudDetalle.nroSolicitud,
                                                           SolicitudDetalle.idProd,
                                                           func.count(SolicitudDetalle.idProd))\
                .filter_by(nroSolicitud = id_sol)\
                .group_by(SolicitudDetalle.idProd).all()

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
                        if cant < pr.cant_stock:
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
            print('Error:' + e)
            return 'Error de servicio'
