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
    solic = db.relationship("Solicitud", backref='producto', lazy=True)
    remit = db.relationship("Remito", backref='producto', lazy=True)
    fact = db.relationship("Factura", backref='producto', lazy=True)

class Factura(db.Model):
    id_factura = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    total = db.Column(db.Float)
    tipo = db.Column(db.String(50))
    nom_tarjeta = db.Column(db.String(50))
    cuenta = db.Column(db.String(50), unique=True)
    num_tarjeta = db.Column(db.String(50), unique=True)
    cant_cuotas = db.Column(db.Integer)
    id_prod = db.Column(db.Integer, db.ForeignKey('producto.id_prod'),  nullable=False)

class Remito(db.Model):
    nro_remito = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), unique=True)
    apellido = db.Column(db.String(50), unique=True)
    telefono = db.Column(db.String(50), unique=True)
    direccion = db.Column(db.String(50), unique=True)
    solicitud = db.relationship("Solicitud", backref='remito', lazy=True)
    id_prod = db.Column(db.Integer, db.ForeignKey('producto.id_prod'),  nullable=False)

class Solicitud(db.Model):
    nro_solicitud = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cant_pedida = db.Column(db.String(20), unique=True)
    id_prod = db.Column(db.Integer, db.ForeignKey('producto.id_prod'),  nullable=False)
    nro_remito = db.Column(db.Integer, db.ForeignKey('remito.nro_remito'),  nullable=False)

class Cliente(db.Model):
    dni = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True)
    apellido = db.Column(db.String(120), unique=True)
    tel = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    direccion = db.Column(db.String(50), unique=True)