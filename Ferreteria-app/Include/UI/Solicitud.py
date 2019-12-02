from Include.Model.model import Solicitud
from Include.Model.model import db
from Include.UI.Cliente import UICliente
from sqlalchemy import exc


class UISolicitud():
    def Alta(self,dni,total, fecha):
        try:
            if not dni is None and not fecha is None:
                c = UICliente()
                existecli= c.BuscarCliente(dni)
                if existecli:
                            sol = Solicitud(dniCliente = dni ,precio_total = total, fecha_solicitud = fecha)
                            db.session.add(sol)
                            db.session.commit()
                            return sol
                else:
                    return 'cliente inexistente'
        except TypeError as ex:
            return 'Error de servicio'
    
    def buscarSolicitud(self, id_sol):
        try:
            sol = Solicitud.query.filter_by(nroSolicitud=id_sol).first()
            if sol:
                return sol
            else:
                return None
        except TypeError as ex:
            return 'Error al buscar la solicitud'

    def getSolicitud(self, nroSolic):
        try:
            p = Solicitud.query.filter_by(nroSolicitud = nroSolic).first()
            if p is None:
                return 'No se encontro el nro de solicitud'
            else:
                return p
        except TypeError as e:
            print(e.args)
            return('Error de servicio')

