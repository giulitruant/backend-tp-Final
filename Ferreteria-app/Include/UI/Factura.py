from Include.Model.model import Factura, Solicitud, Producto, Solicitud_Detalle
from Include.UI.Proveedor import UIProveedor
from Include.Model.model import db

class UIFactura():

    def alta(self, nroSolicitud, formaPago, nomTarjeta, cuenta, num_tarjeta, cant_cuotas):
        try:
            fact = Factura()
            solic = Solicitud()
            solicDet = Solicitud_Detalle()
            solic = Solicitud.query.filter_by(nro_solicitud=nroSolicitud)
            solicDet = Solicitud_Detalle.query.filter_by(nro_solicitud=nroSolicitud)
            total = 0
            for value in solicDet:
                cantProd = int(value.cantidad)
                precioU = Producto.query.filter_by(id_prod=value.id_prod)
                total = total + (cantProd * precioU)
            fact.total = total

        except ValueError:
            return 'Hubo un error al agregar el producto'
