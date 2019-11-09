from Include.Model.model import Producto
from Include.UI.Proveedor import UIProveedor
from Include.Model.model import db



class UIProducto():

    def alta(self, desc, prec_u, stock, cantM, prov):
        try:
            #p = Proveedor.query.filter_by(cuit=prov).first()
            p = UIProveedor()
            p = p.BuscarProveedor(prov)
            if p != 'No existe el proveedor' and p != 'Error al buscar el proveedor':
                p = Producto.query.filter_by(descripcion=desc).first()
                if p is None:
                    p = Producto()
                    p.descripcion = desc
                    p.precio_uni = prec_u
                    p.cant_stock = stock
                    p.cant_min = cantM
                    p.cuit = prov
                    db.session.add(p)
                    db.session.commit()
                else:
                    return 'Ya existe el producto'
            else:
                return 'No existe el proveedor'
            return 'ok'
        except ValueError:
            return 'Hubo un error al agregar el producto'

    def getProductos(self, cuit):
        try:
            if not cuit is None and cuit != '':
                listaProductos = Producto.query.filter_by(cuit=cuit).all()
                if listaProductos.__len__() > 0:
                    return listaProductos
                else:
                    'No tiene productos cargados'
            else:
                listaProductos = Producto.query.filter_by().all()
                if listaProductos.__len__() > 0:
                    return listaProductos
                else:
                    'No tiene productos cargados'

        except ValueError as e:
            return 'Hubo un error al recuperar la lista de productos'

    def deleteProducto(self, id_prod):
        try:
            p =  Producto.query.filter_by(id_prod=id_prod).first()
            if not p is None:
                db.session.delete(p)
                db.session.commit()
                return 'ok'
            else:
                return 'El producto no existe'
        except ValueError as v:
            print(v.args)
            return 'Error al eliminar el producto'

    def updateProducto(self, id, desc, precio_u, stock, cant_m, prov):
        try:
            p = Producto.query.filter_by(id_prod=id).first()
            if not p is None:
                p.descripcion = str(desc)
                p.precio_uni = float(precio_u)
                p.cant_stock = int(stock)
                p.cant_min = int(cant_m)
                p.cuit = str(prov)
                db.session.commit()
                p = Producto.query.filter_by(id_prod=id).first()
                if not p is None:
                    return p
                else:
                    return 'El producto no se actualizo'
            else:
                return None
        except ValueError as e:
            print(e.args)
            return None

