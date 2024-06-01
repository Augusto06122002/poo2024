import _sqlite3
"---------Archivo config.py------------------"
SECRET_KET="CLAVE"
SQLALCHEMY_DATABASE_URL='sqlite://datos.sqlite3'#dIRECCION DE LA BASE DE DATOS SE PONE EL NOMBRE DE LA BASE DE DATOS
SQLALCHEMY_TRACK_MODIFICATIONS=False#Para que no muestre en cosola cada vez que hacemos una modificacion
"---------------Modelo..................."
#consiste en hacer la vinculacion entre clases y tabla por cada clase habra una tabla respectivamente
from __main__ import app #Se importa la instancia de la aplicacion (instancia del flask)
from flask_sqlalchemy import SQLAlchemy#clase se sql

db = SQLAlchemy(app)#Instancia de la base de datos que pasa como parametros la instancia del flask

class Usuario(db.Model):#hereda de de esa clase
    __tablename___ = 'usuario'#Ponemos como se va a llamar en la base de datos  la tabla
    id= db.Column(db.Integrer,primary_key=True)#Digo de que tipo es y en este caso el id va ser primary_key 
    nombre = db.Column(db.String(80),nullable =False)#string longitud maximo, nullable dice que el valor no puede ser nulo
    correo = db.Column(db.string(120),unique=True,nullable=False)#unique dice que el dato corre no se puede repetir
    clave=db.Column(db.String(120),nullable=False)
    comentario=db.relationship('Comentario',backref='usuario',cascade="all,delete-orphan")#Aca esta la relacion entre las clases
    #Es una relacion con la tabla comentario por el primer parametro y luego backref='usuario' indica la tabla con la que se va a relacionar
    #Si borro un usuario pierden la relacion con los comentarios entonces los comentarios pasan a ser huerfanos
    #con el cascade indica que si yo borro un usuario que tambien borre los comentarios que hzio ese usuario
"----------------EnLaAplicacion--------------------"
from datetime import datetime
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash,check_password_hash

app =Flask(__name__)
app.config.from_pyfile('confing.py')
from models import db
from models import Usuario,Comentario

if __name__ =='__main__':
    db.create_all()
    app.run(debug=True)