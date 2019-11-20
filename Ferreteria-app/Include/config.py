from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def conexion():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/bdferreteria'
    db = SQLAlchemy(app)
    return db
