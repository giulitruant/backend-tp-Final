from Include.UI.Producto import UIProducto, UIProveedor
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
        precio_u = request.json['precio_u']
        stock = request.json['stock']
        cantM = request.json['cant_min']
        prov = request.json['proveedor']
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

@app.route('/deleteProducto', methods=['DELETE'])
def EliminarProducto():
    try:
        id = int(request.args['id_producto'])
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

@app.route('/deleteProveedor', methods=['DELETE'])
def EliminarProveedor():
    try:
        id = request.args['cuit']
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

#If we're running in  stand alone mode,run the application
if __name__ == '__main__':
    app.run(debug=True)
