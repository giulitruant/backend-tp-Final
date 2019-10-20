from Include.Model.model import Proveedor
from Include.Model.model import db
from sqlalchemy import exc

class UIProveedor():
    def Alta(self, cuit, nom, ape, tel, email, direccion):

        try:
            if not cuit is None and not nom is None and not ape is None and not tel is None and not email is None:
                p = Proveedor(cuit=cuit, nombre=nom, apellido=ape, tel=tel, email=email, direccion=direccion)
                existe = Proveedor.query.filter_by(cuit=cuit).first()
                if not p is None:
                    db.session.add(p)
                    db.session.commit()
                    return 'ok'
                else:
                    return 'El Proveedor existe'

        except TypeError as e:
            return 'Error de servicio'

    def Baja(self, cuit):
        try:
            p = Proveedor.query.filter_by(cuit=cuit).first()
            if not p is None:
                db.session.delete(p)
                db.session.commit()
                return 'ok'
            else:
                return 'El proveedor no existe'
        except Exception as e:
            return 'Error de servicio'

    def modificar(self, cuit, nom, ape, tel, email, direccion):
        try:
            prov = Proveedor()
            prov = Proveedor.query.filter_by(cuit=cuit).first()
            if nom != '' and not nom is None:
                prov.nombre = nom
            if ape != '' and not ape is None:
                prov.apellido = ape
            if tel != '' and not tel is None:
                prov.tel = tel
            if email != '' and not email is None:
                prov.email = email
            if direccion != '':
                prov.direccion = direccion

            db.session.commit()
            return 'ok'

        except Exception as e:
            return 'Error de servicio'

    def ObtenerProveedores(self):
        try:
            p = Proveedor.query.all()
            return p
        except exc.SQLAlchemyError as e:
            print(e.args)
            return 'Error de servicio'

    def BuscarProveedor(self, cuit):
        try:
            p = Proveedor.query.filter_by(cuit=cuit).first()
            if not p is None:
                return p
            else:
                return 'No existe el proveedor'
        except ValueError as e:
            print(e)
            return 'Error al buscar el proveedor'