from Include.Model.model import Factura, Solicitud, Producto, Solicitud_Detalle
from Include.UI.Proveedor import UIProveedor
from Include.Model.model import db

class UIFactura():

    def alta(self, nroSolicitud, formaPago, nomTarjeta, cuenta, num_tarjeta, cant_cuotas, tipo):
        try:
            fact = Factura()
            fact.tipo = tipo
            fact.forma_pago = formaPago
            solic = Solicitud()
            #solicDet = Solicitud_Detalle()
            solic = Solicitud.query.filter_by(nro_solicitud=nroSolicitud)
            lstSolicDet = Solicitud_Detalle.query.filter_by(nro_solicitud=nroSolicitud)
            total = 0
            for value in lstSolicDet:
                cantProd = int(value.cantidad)
                prod = Producto.query.filter_by(id_prod=value.id_prod)
                total = total + (cantProd * prod.precio_uni)
                prod.cant_stock = (prod.cant_stock - value.cantidad)
                db.session.commit()
            fact.total = total

            if formaPago == 'cuotas':
                fact.cant_cuotas = cant_cuotas
                fact.nom_tarjeta = nomTarjeta
                fact.num_tarjeta = num_tarjeta
                fact.cuenta = cuenta

            db.session.add(fact)
            db.session.commit()



        except ValueError:
            return 'Hubo un error al agregar el producto'
