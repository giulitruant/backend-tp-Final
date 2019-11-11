from Include.config import conexion

db = conexion()

class Proveedor(db.Model):
    cuit = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True)
    apellido = db.Column(db.String(120), unique=True)
    tel = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    direccion = db.Column(db.String(50), unique=True)
    productos = db.relationship("Producto", backref='proveedor', lazy=True)

class Producto(db.Model):
    id_prod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(50))
    precio_uni = db.Column(db.Float)
    cant_stock = db.Column(db.Integer)
    cant_min = db.Column(db.Integer)
    cuit = db.Column(db.Integer, db.ForeignKey('proveedor.cuit'), nullable=False)
    solic = db.relationship("Solicitud_Detalle", backref='producto', lazy=True)


class Solicitud_Detalle(db.Model):
    id_detalle = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nro_solicitud = db.Column(db.Integer, db.ForeignKey('solicitud.nro_solicitud'), primary_key=True, nullable=False)
    cantidad = db.Column(db.Float , nullable=False)
    id_prod = db.Column(db.Integer, db.ForeignKey('producto.id_prod'), nullable=False)

class Solicitud(db.Model):
    nro_solicitud = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dni_cliente = db.Column(db.Integer, db.ForeignKey('cliente.dni'))
    precio_total = db.Column(db.Float, nullable=False )
    fecha_solicitud = db.Column(db.String(20), nullable=False)
    fact = db.relationship('Factura', backref='solicitud', lazy=True)
    sol_det = db.relationship('Solicitud_Detalle', backref='solicitud', lazy=True)

class Cliente(db.Model):
    dni = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True)
    apellido = db.Column(db.String(120), unique=True)
    tel = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    direccion = db.Column(db.String(50), unique=True)
    solic = db.relationship('Solicitud', backref='cliente', lazy=True)

class Factura(db.Model):
    id_factura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    forma_pago = db.Column(db.String(40), nullable=False)
    nom_tarjeta = db.Column(db.String(50))
    cuenta = db.Column(db.String(50))
    num_tarjeta = db.Column(db.String(50))
    cant_cuotas = db.Column(db.Integer)
    nro_solicitud = db.Column(db.Integer, db.ForeignKey('solicitud.nro_solicitud'), nullable=False)
