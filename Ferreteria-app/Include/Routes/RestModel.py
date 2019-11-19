from Include.UI.Producto import UIProducto
from Include.UI.Proveedor import UIProveedor
from Include.UI.Cliente import UICliente
from Include.UI.Factura import UIFactura
from Include.UI.Solicitud import UISolicitud
from Include.UI.Solicitud_Detalle import UISolicitudDetalle
from datetime import date

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#Create the application instance
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/bdferreteria'
db = SQLAlchemy(app)

#Create a URL route in our applcation for "/"
@app.route('/addProducto', methods=['POST'])
def AgregarProducto():
    try:
        desc = request.json['descripcion']
        precio_u = request.json['precioU']
        stock = request.json['stock']
        cantM = request.json['cantMin']
        prov = request.json['cuit']
        np = UIProducto()
        msj = np.alta(desc, precio_u, stock, cantM, prov)
        response = jsonify(
            {
                'msj':'msj'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        print(e.args)
        response = jsonify({
                'msj': 'Error de servicio'
            })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/getProductosPorProveedor', methods=['GET'])
def ObtenerProductosPorProveedor():
    try:
        prov = str(request.args['proveedor'])
        if len(prov) == 11:
            np = UIProducto()
            lista = np.getProductos(prov)
            response = jsonify({
                "producto": [{"id": x.id_prod,
                              "descripcion": x.descripcion,
                              "precioUnitario" : x.precio_uni,
                              "stock" : x.cant_stock,
                            "cantidad_minima_stock": x.cant_min,
                            "proveedor": x.cuit
                            } for x in lista],
                'msj':''
            })
        else:
            response = jsonify({
                'msj': 'El cuit debe contener 11 numeros'
            })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except ValueError as ve:
        response = jsonify({
            'msj': 'El campo no es correcto'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        print(e.args)
        response = jsonify({
                'msj':'Error al objetener el producto'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#sin uso por el momento
@app.route('/getProductos', methods=['GET'])
def ObtenerProductos():
    try:
        #prov = str(request.args['proveedor'])
        #if len(prov) == 11:
        np = UIProducto()
        lista = np.getProductos()
        response = jsonify({
            "producto": [{"id": x.id_prod,
                          "descripcion": x.descripcion,
                          "precioU" : x.precio_uni,
                          "stock" : x.cant_stock,
                        "cantMin": x.cant_min,
                        "cuit": x.cuit
                        } for x in lista],
            'msj':''
            })
        #else:
         #   response = jsonify({
          #      'msj': 'El cuit debe contener 11 numeros'
           # })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except ValueError as ve:
        response = jsonify({
            'msj': 'El campo no es correcto'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        print(e.args)
        response = jsonify({
                'msj':'Error al objetener el producto'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/deleteProducto/<string:id>', methods=['DELETE'])
def EliminarProductoid(id):
    try:
        id = id #int(request.args['id_producto'])
        p = UIProducto()
        msj = p.deleteProducto(id)

        if msj == 'ok':
            response = jsonify({
                'msj': msj
            })
        else:
            response = jsonify({
                'msj': msj
            })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except ValueError as ve:
        response = jsonify({
            'msj': 'El campo no es correcto'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        print(e.args)
        response =  jsonify({
            msj: 'Ocurrio un error al eliminar el producto'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/updateProducto', methods=['PUT'])
def ActualizarProducto():
    try:
        id = int(request.args['id'])
        desc = str(request.args['desc'])
        precioU = float(request.args['precio_u'])
        stock = int(request.args['stock'])
        cantM = int(request.args['cant_m'])
        cuit = str(request.args['prov'])
        p = UIProducto()
        prod = p.updateProducto(id, desc, precioU, stock, cantM, cuit)
        if not prod is None:
            response = jsonify({
                'producto': [{
                "id": prod.id_prod,
                "descripcion": prod.descripcion,
                "precioUnitario": prod.precio_uni,
                "stock": prod.cant_stock,
                "cantidad_minima_stock": prod.cant_min,
                "proveedor": prod.cuit
                }],
                'msj': ''
            })
        else:
            if prod is None:
                response = jsonify({
                    'msj':'Ocurrio un error al actualizar el producto'
                })
            else:
                response = jsonify({
                    'msj':prod
                })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except ValueError as ve:
        response =  jsonify({
            'msj': 'Los campos no son correctos'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        print(e.args)
        return jsonify({
            'msj': 'Ocurrio un error al modificar el producto'
        })

@app.route('/addProveedor', methods=['POST'])
def addProveedor():
    try:
        #file = json.loads(request.data)
        #js = request.get_json()
        #jso = jsonify(js)
        cuit = request.json['cuit']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        tel = request.json['telefono']
        email = request.json['email']
        direccion = request.json['direccion']
        p = UIProveedor()
        rta = p.Alta(cuit, nombre, apellido, tel, email, direccion)
        if rta == 'ok':
            response = jsonify({
                "msj": rta
            })
        else:
            response = jsonify({
                "msj": rta
            })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        response = jsonify({
            'msj': 'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/deleteProveedor/<string:cuit>', methods=['DELETE'])
def EliminarProveedor(cuit):
    try:
        id = cuit #request.args['cuit']
        p = UIProveedor()
        rta = p.Baja(id)

        if rta == 'ok':
            response = jsonify({
                'msj' : rta
            })
        else:
            response = jsonify({
                'msj': rta
            })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        response = jsonify({
            'msj':'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/updateProveedor', methods=['PUT'])
def ActualizarProveedor():
    try:
        cuit = request.args['cuit']
        nombre = request.args['nombre']
        apellido = request.args['apellido']
        tel = request.args['tel']
        email = request.args['email']
        dire = request.args['direccion']

        p = UIProveedor()
        rta = p.modificar(cuit, nombre, apellido, tel, email, dire)

        if rta == 'ok':
            response = jsonify({
                'msj': rta
            })
        else:
            response = jsonify({
                'msj': rta
            })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        response = jsonify({
            'msj': 'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/getProveedor')
def ObtenerProveedor():
    try:
        prov = request.args['cuit']
        p = UIProveedor()
        obj = p.BuscarProveedor(prov)
        if not obj.cuit is None:
            response = jsonify({
                'cuit': obj.cuit,
                'nombre': obj.nombre,
                'apellido': obj.apellido,
                'telefono':obj.tel,
                'email':obj.email,
                'direccion':obj.direccion
            })
        else:
            response = jsonify({
                'msj':obj
            })
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

    except Exception as e:
        response = jsonify({
            'msj': 'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/getProveedores')
def ObtenerProveedores():
    try:
        p = UIProveedor()
        listaProve = p.ObtenerProveedores()
        response = jsonify({
            "proveedor": [{"cuit": x.cuit,
                          "nombre": x.nombre,
                          "apellido": x.apellido,
                          "telefono": x.tel,
                          "email": x.email,
                          "direccion": x.direccion
                          } for x in listaProve],
            'msj': ''
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        """
        return jsonify(
            [{
                       "cuit": x.cuit,
                          "nombre": x.nombre,
                          "apellido": x.apellido,
                          "telefono": x.tel,
                          "email": x.email,
                          "direccion": x.direccion
                          } for x in listaProve]
        )
        """
    except Exception as e:
        response = jsonify({
            'msj':'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/addCliente', methods=['POST'])
def addCliente():
    try:
        dni = request.json['dni']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        tel = request.json['tel']
        email = request.json['email']
        direccion = request.json['direccion']
        c = UICliente()
        rta = c.Alta(dni, nombre, apellido, tel, email, direccion)
        if rta == 'ok':
            response = jsonify({
                "msj" : rta
            })
        else:
            response = jsonify({
                "msj" : rta
            })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        response = jsonify({
            'msj': 'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/deleteCliente/<string:id>', methods=['DELETE'])
def EliminarCliente(id):
    try:
        id = id #request.args['dni']
        c = UICliente()
        rta = c.Baja(id)

        if rta == 'ok':
            response = jsonify({
                'msj' : rta
            })
        else:
            response = jsonify({
                'msj': rta
            })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        response = jsonify({
            'msj':'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/updateCliente', methods=['PUT'])
def ActualizarCliente():
    try:
        dni = request.args['dni']
        nombre = request.args['nombre']
        apellido = request.args['apellido']
        tel = request.args['tel']
        email = request.args['email']
        dire = request.args['direccion']

        c = UICliente()
        rta = c.modificar(dni, nombre, apellido, tel, email, dire)

        if rta == 'ok':
            response = jsonify({
                'msj': rta
            })
        else:
            response = jsonify({
                'msj': rta
            })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        response = jsonify({
            'msj': 'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/getCliente')
def ObtenerCliente():
    try:
        dni = request.args['dni']
        c = UICliente()
        obj = c.BuscarProveedor(dni)
        if not obj.dni is None:
            response = jsonify({
                'dni': obj.dni,
                'nombre': obj.nombre,
                'apellido': obj.apellido,
                'telefono':obj.tel,
                'email':obj.email,
                'direccion':obj.direccion
            })
        else:
            response = jsonify({
                'msj':obj
            })
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

    except Exception as e:
        response = jsonify({
            'msj': 'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/getClientes')
def ObtenerClientes():
    try:
        c = UICliente()
        listaClientes = c.ObtenerClientes()
        response = jsonify({
            "cliente": [{"dni": x.dni,
                          "nombre": x.nombre,
                          "apellido": x.apellido,
                          "tel": x.tel,
                          "email": x.email,
                          "direccion": x.direccion
                          } for x in listaClientes],
            'msj': ''
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        response = jsonify({
            'msj':'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/addSolicitud' , methods=['POST'])
def addSolicitud():
    try:
        dni = request.args['dni_cliente']
        precio = request.args['precio_total']
        fecha_sol = request.args['fecha_solicitud']
        #Agregar fecha_vto_solicitud
        sol_details = request.args['solicitud']
        s = UISolicitud()
        sol = s.Alta(dni = dni, precio = precio,fecha = fecha_sol)
        if sol:
            for det in sol_details:
                sd = UISolicitudDetalle()
                nuevo_detalle = sd.Alta(sol.nro_solicitud,det.cantidad,det.prod)
        response = jsonify({
            'msj': 'ok'
        })
    except Exception as ex:
        response = jsonify({
            'msj': 'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/getSolicitud')
def getSolicitud():
    try:
        nro_sol= request.args['nro_solicitud']
        sol = UISolicitud()
        obj = sol.buscarSolicitud(nro_sol)
        if obj :
            #si encuentro el objeto busco los detalles de la solicitud
            det = UISolicitudDetalle()
            #ahora genero la lista a devolver con el detalle de las solicitudes
            listDet = det.getListDetalleSolicitud(obj.nro_solicutd)
            if listDet:
                response = jsonify({
                    'nro_solicitud' : obj.nro_solicitud,
                    'dni_cliente': obj.dni_cliente,
                    'fecha_solicitud':obj.fecha_solicitud,
                    'sol_det':listDet

                })
            else:
                response = jsonify({
                    'msj':'Error al obtener los detalles de la Solicitud'
                })
        else:
            response = jsonify({
                        'msj': 'Error al obtener los detalles de la Solicitud'
            })
    except Exception as e:
        response = jsonify({
            'msj': 'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
            
@app.route('/EmitirFactura', methods=['POST'])
def EmitirFactura():
    try:
        nroSolicitudCompra = request.json['solicitud']
        pago = request.json['tipo_pago']
        nom_tarjeta = ''
        nro_tarjeta = ''
        cuenta = ''
        cuotas = ''
        if pago == 'tarjeta':
            nom_tarjeta = request.json['nom_tarjeta']
            nro_tarjeta = request.json['nro_tarjeta']
            cuenta = request.json['cuenta']
            cuotas = request.json['cuotas']

        uiFactura = UIFactura()
        facturacion = uiFactura.alta(nroSolicitudCompra, pago, cuenta, nom_tarjeta, nro_tarjeta, cuotas)
        if facturacion is None:
            response = jsonify({
                'msj':'Error de servicio'
            })
            return response

        response = jsonify({
            'nroFactura': facturacion.factura.id,
            'fecha': date.today(),
            'tipoFactura': facturacion.factura.tipo,
            'razonSocialCli': facturacion.cliente.nombre + facturacion.cliente.apellido,
            'domicilioCli': facturacion.cliente.direccion,
            'telefonoCli': facturacion.cliente.tel,
            'dni': facturacion.cliente.dni,
            "producto": [{"cant": x.cantidad,
                          "Descripcion": x.descripcion,
                          "codigo": x.id_prod,
                          "precioU": x.precio_uni,
                          "importe": x.cant_stock,
                          } for x in facturacion.detSolic],
            'importeTotal': facturacion.total
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as ex:
        print(ex)
        response = jsonify({
            'msj':'Error de servicio'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#If we're running in  stand alone mode,run the application
if __name__ == '__main__':
    app.run(debug=True)
