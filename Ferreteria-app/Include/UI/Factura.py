from Include.Model.model import Factura, Solicitud, Producto, SolicitudDetalle
from Include.UI.SolicitudDetalle import UISolicitudDetalle
from Include.UI.Cliente import UICliente
from Include.Model.model import db

class UIFactura():

    def alta(self, nroSolicitud, formaPago, cuenta, nomTarjeta, nro_tarjeta, cant_cuotas, tipo):
        try:
            p = Factura.query.filter_by(nroSolicitud = nroSolicitud).first()
            facturacion = []
            if p is None:
                facturacion = []
                fact = Factura()
                fact.forma_pago = formaPago
                solic = Solicitud()
                solicDet = SolicitudDetalle()
                solic = Solicitud.query.filter_by(nroSolicitud=nroSolicitud).first()
                if solic is None:
                    return None
                dSol = UISolicitudDetalle()
                lstSolicDet = dSol.getListDetalleSolicitud(nroSolicitud)


                if lstSolicDet is None:
                    return None
                uiCliente = UICliente()
                cliente = uiCliente.BuscarCliente(solic.dniCliente)
                if cliente is None:
                    return None

                total=0
                lstProductos = []
                count = 0
                for value in lstSolicDet:
                    detalle = tuple()
                    #idProd = value.idProd
                    cantProd = int(value[3])

                    #Actualizo el stock de los productos a comprar
                    prod = Producto.query.filter_by(idProd=value.idProd).first()
                    prod.cant_stock = (prod.cant_stock - cantProd)
                    db.session.commit()

                    totalProducto = (cantProd * prod.precio_uni)
                    total = total + totalProducto
                    detalle = (cantProd, prod.descripcion, prod.idProd, prod.precio_uni, totalProducto)
                    lstProductos.insert(count, detalle)
                    count = count + 1

                    #asigno datos de la factura
                fact.tipo = tipo
                fact.total = total

                if formaPago == 'cuotas':
                    fact.cant_cuotas = cant_cuotas
                    fact.nom_tarjeta = nomTarjeta
                    fact.num_tarjeta = nro_tarjeta
                    fact.cuenta = cuenta

                # Ingreso la factura
                db.session.add(fact)
                db.session.commit()

                facturacion.insert(0, fact)
                facturacion.insert(1, cliente)
                facturacion.insert(2, lstProductos)

                #retorno los datos para emitir la factura
                return facturacion
            else:
                f = Factura.query.filter_by(nroSolicitud = nroSolicitud)
                solic = Solicitud()
                solicDet = SolicitudDetalle()
                solic = Solicitud.query.filter_by(nroSolicitud=nroSolicitud).first()
                if solic is None:
                    return None
                dSol = UISolicitudDetalle()
                lstSolicDet = dSol.getListDetalleSolicitud(nroSolicitud)


                if lstSolicDet is None:
                    return None
                uiCliente = UICliente()
                cliente = uiCliente.BuscarCliente(solic.dniCliente)
                if cliente is None:
                    return None

                total=0
                lstProductos = []
                count = 0
                for value in lstSolicDet:
                    detalle = tuple()
                    #idProd = value.idProd
                    cantProd = int(value[3])

                    #Actualizo el stock de los productos a comprar
                    prod = Producto.query.filter_by(idProd=value.idProd).first()
                    prod.cant_stock = (prod.cant_stock - cantProd)
                    db.session.commit()

                    totalProducto = (cantProd * prod.precio_uni)
                    total = total + totalProducto
                    detalle = (cantProd, prod.descripcion, prod.idProd, prod.precio_uni, totalProducto)
                    lstProductos.insert(count, detalle)
                    count = count + 1

                facturacion.insert(0, f)
                facturacion.insert(1, cliente)
                facturacion.insert(2, lstProductos)
                return facturacion



        except ValueError as e:
            print(e.args)
            return 'Hubo un error al agregar el producto'
