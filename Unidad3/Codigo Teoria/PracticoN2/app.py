from flask import Flask,request,render_template,url_for,redirect
from werkzeug.security import generate_password_hash, check_password_hash
from models import Paquete,Transporte,Sucursal,db


app=Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/registrar-paquete', methods=['GET', 'POST'])
def registrar_paquete():
    if request.method == 'POST':
        # Lógica para registrar el paquete
        # ...
        return redirect(url_for('inicio'))
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    return render_template('registrar_paquete.html', sucursales=sucursales)

@app.route('/salida-transporte', methods=['GET', 'POST'])
def registrar_salida_transporte():
    if request.method == 'POST':
        # Lógica para registrar la salida del transporte
        # ...
        return redirect(url_for('inicio'))
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    paquetes = Paquete.query.filter_by(entregado=False, transporte_id=None).all()
    return render_template('registrar_salida_transporte.html', sucursales=sucursales, paquetes=paquetes)

@app.route('/llegada-transporte', methods=['GET', 'POST'])
def registrar_llegada_transporte():
    if request.method == 'POST':
        # Lógica para registrar la llegada del transporte
        # ...
        return redirect(url_for('inicio'))
    transportes = Transporte.query.filter_by(fechaHoraLLegada=None).all()
    return render_template('registrar_llegada_transporte.html', transportes=transportes)

if __name__ == '__main__':
    app.run(debug=True)



