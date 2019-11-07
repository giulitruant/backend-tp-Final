from Include.Model.model import Cliente
from Include.Model.model import db
from sqlalchemy import exc

class UICliente():
    def Alta(self, dni, nom, ape, tel, email, direccion):

        try:
            if not dni is None and not nom is None and not ape is None and not tel is None and not email is None:
                c = Cliente(dni=dni, nombre=nom, apellido=ape, tel=tel, email=email, direccion=direccion)
                existe = Cliente.query.filter_by(dni=dni).first()
                if not c is None:
                    db.session.add(c)
                    db.session.commit()
                    return 'ok'
                else:
                    return 'El cliente existe'

        except TypeError as e:
            return 'Error de servicio'

    def Baja(self, dni):
        try:
            dni = int(dni)
            c = Cliente.query.filter_by(dni=dni).first()
            if not c is None:
                db.session.delete(c)
                db.session.commit()
                return 'ok'
            else:
                return 'El cliente no existe'
        except Exception as e:
            return 'Error de servicio'

    def modificar(self, dni, nom, ape, tel, email, direccion):
        try:
            cli = Cliente()
            cli = Cliente.query.filter_by(dni=dni).first()
            if nom != '' and not nom is None:
                cli.nombre = nom
            if ape != '' and not ape is None:
                cli.apellido = ape
            if tel != '' and not tel is None:
                cli.tel = tel
            if email != '' and not email is None:
                cli.email = email
            if direccion != '':
                cli.direccion = direccion

            db.session.commit()
            return 'ok'

        except Exception as e:
            return 'Error de servicio'

    def ObtenerClientes(self):
        try:
            c = Cliente.query.all()
            return c
        except exc.SQLAlchemyError as e:
            print(e.args)
            return 'Error de servicio'

    def BuscarCliente(self, dni):
        try:
            c = Cliente.query.filter_by(dni=dni).first()
            if not c is None:
                return c
            else:
                return 'No existe el cliente'
        except ValueError as e:
            print(e)
            return 'Error al buscar el cliente'
