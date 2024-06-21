from __main__ import app

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column, DateTime,Float,Text,Boolean
from sqlalchemy.orm import relationship



db = SQLAlchemy(app)
class Sucursal(db.Model):
    __tablename__='sucursal'
    id = db.Column(db.Integer,primary_key=True)#El id va ser unico para cada sucursal
    numero = db.Column(db.Integer,unique=True,nullable =False)#El nro sucursal es un entero, unico por cada sucursal y no es nulo
    provincia = db.Column(db.String(80),nullable=False)#La provincia es una cadena y no es nula(Se supone que en una provincia puedena haber mas de 1 sucursal)
    localidad = db.Column(db.String(80),nullable=False)#La localidad es una cadena y no es nula(Se supone que la varias sucursales puede estar en la misma localidad)
    direccion = db.Column(db.String(180),nullable=False,unique=True)#La direccion de la sucursal es unica para cada una 
    Paquete = relationship("Paquete",backref='sucursal',cascade="all,delete-orphan")#Se establece la relacion(1 a muchos) entre la clase Sucursal y Paquete(Primer parametro), backref indica que la relacion es bidireccional, y cascade indica que si se elimina una sucursal, se eliminan consigo los huerfanos(paquetes)
    
class Paquete(db.Model):
    __tablename__='paquete'
    id = db.Column(db.Integer,primary_key=True)#id unico por cada paquete
    numeroEnvio=db.Column(db.Integer,unique=True,nullable=False)#El numero de envio es tipo entero, unico por paquete, y no es nulo
    peso=db.Column(db.Float,nullable=False)#El peso del paquete es tipo real,no es nulo(Se supone que un varios paquetes pueden tener el mismo peso) 
    nomdestinatario=db.Column(db.String(120),nullable=False)
    dirdestinatario = db.Column(db.String(120),nullable=False)
    entregado=db.Column(db.Boolean,default=False)#Por defecto el paquete no esta entregado
    observaciones=db.Column(db.Text,nullable=True)#Las observaciones son opcionales
    idsucursal= db.Column(db.Integer,db.ForeignKey('sucursal.id'))#Se crea una clave foranea con el id de la sucursal con la que se relacionan  los 1..N paquetes
    idtransporte=db.Column(db.Integer,db.ForeignKey('transporte.id'))#duda Se crea una clave foranea con el id del transporte con el que se relaciona los 1..Npaquetes
    idrepartidor = db.Column(db.Integer,db.ForeignKey('repartidor.id'))
    
class Transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key =True)
    numerotransporte = db.Column(db.Integer,unique=True,nullable=False)
    fechahorasalida =db.Column(db.DateTime,nullable=False)#DataTime permite tratar fecha y hora
    fechahorallegada= db.Column(db.DateTime,nullable=True)
    Paquete = relationship("Paquete",backref='transporte',cascade="all,delete-orphan")#duda Se establece la relacion(0 o 1 a muchos) entre la clase Transporte y Paquete(Primer parametro), backref indica que la relacion es bidireccional, y cascade indica que si se elimina un transporte, se eliminan consigo los huerfanos(paquetes)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id')) #Se crea la clave foranea con el id de la sucursal con la que se relaciona los 1...Ntransportes 
    Sucursal = relationship("Sucursal",backref="transporte")#Establece la relacion (1...*transportes  a 1sucursal ) bidireccional entre sucursal y transporte
class Repartidor(db.Model):
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer,primary_key = True)
    numero = db.Column(db.Integer ,unique = True, nullable =False)
    nombre = db.Column(db.String(120),unique = False,nullable = False)
    dni = db.Column(db.String(120), unique = True, nullable = False)
    Paquete = relationship("Paquete",backref='repartidor',cascade="all,delete-orphan")