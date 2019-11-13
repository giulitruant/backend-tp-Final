from Include.Model.model import Factura, Solicitud, Producto, Solicitud_Detalle
from Include.UI.Proveedor import UIProveedor
from Include.UI.Cliente import UICliente
from Include.Model.model import db

class UIFactura():

    def alta(self, nroSolicitud, formaPago, cuenta, nomTarjeta, num_tarjeta, cant_cuotas):
        try:
            facturacion = []
            fact = Factura()
            fact.forma_pago = formaPago
            solic = Solicitud()
            solicDet = Solicitud_Detalle()
            solic = Solicitud.query.filter_by(nro_solicitud=nroSolicitud)
            if solic is None:
                return None
            lstSolicDet = Solicitud_Detalle.query.filter_by(nro_solicitud=nroSolicitud)
            if lstSolicDet is None:
                return None
            uiCliente = UICliente
            cliente = uiCliente.BuscarCliente(solic.dni_cliente)
            if cliente is None:
                return None

            total=0
            lstProductos = []
            for value in lstSolicDet:
                detalle = []
                cantProd = int(value.cantidad)
                detalle.insert(cantProd)

                #Actualizo el stock de los productos a comprar
                prod = Producto.query.filter_by(id_prod=value.id_prod)
                prod.cant_stock = (prod.cant_stock - value.cantidad)
                db.session.commit()
                id_Prod = value.id_prod
                detalle.insert(id_Prod)

                total = total + (cantProd * prod.precio_uni)
                detalle.insert(cantProd * prod.precio_uni)

                # Asigno los detalles de los productos a la lista
                lstProductos.insert(detalle)

            #asigno el total de la factura
            fact.total = total

            if formaPago == 'cuotas':
                fact.cant_cuotas = cant_cuotas
                fact.nom_tarjeta = nomTarjeta
                fact.num_tarjeta = num_tarjeta
                fact.cuenta = cuenta

            # Ingreso la factura
            db.session.add(fact)
            db.session.commit()

            facturacion.insert(fact)
            facturacion.insert(cliente)
            facturacion.insert(lstSolicDet)

            #retorno los datos para emitir la factura
            return facturacion

        except ValueError:
            return 'Hubo un error al agregar el producto'
