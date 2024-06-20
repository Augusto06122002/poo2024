from flask import Flask,request,render_template,url_for,redirect,flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timedelta
app=Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Paquete,Transporte,Sucursal
   

@app.route('/')
def inicio():
    return render_template('inicio.html')
@app.route('/Despachador/')
def FuncionesDelDespachador():#Para mostrar las funciones del despachador
    dir = session.get('sucursal_direccion')
    nro =session.get('sucursal_numero')
    return render_template('FuncionesDelDespachador.html',sucursal_direccion=dir, sucursal_numero=nro)
@app.route('/Repartidor')
def FuncionesDelRepartidor():#Para mostrar las funciones del repartidpr
    return render_template('FuncionesDelRepartidor.html')

@app.route('/lista_sucursales', methods=['GET', 'POST'])#Para listar sucursales una vez que toca la funcion de despachador
def lista_sucursales():
    if request.method == 'POST':#Una vez que el usuario selecciona la opcion
        sucursal_numero = request.form['sucursal_numero']#Solicita del formulario el numero de la sucursal para ver que sucursal se elegio y en base a eso buscar su id
        sucursal = Sucursal.query.filter_by(numero=sucursal_numero).first()#como los numero son unicos por sucursal una vez que encuentre el numero de sucursal va  a devolver el objeto sucursal
        if sucursal is not None:#Si se selecciono una sucursal
            session['sucursal_numero'] = sucursal.numero
            session['sucursal_direccion'] = sucursal.direccion
            session['sucursal_id'] = sucursal.id
            session['sucursal_provincia'] = sucursal.provincia
            session['sucursal_localidad'] = sucursal.localidad
            return redirect(url_for('FuncionesDelDespachador'))#Va al metodo funciones del despachador de La funciones del despachador
        else:
            flash('Por favor, selecciona una sucursal primero.')
            # Manejar el caso en que la sucursal no se encuentra
            return redirect(url_for('lista_sucursales'))
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()# lista de sucursales, consultando a la base de datos, ordenado por numero sucursales
    return render_template('lista_sucursales.html', sucursales=sucursales)# pasa la sucursales al html para que se muestre en forma de lista

@app.route('/registrar-paquete', methods=['GET', 'POST'])#Para registrar paquetes
def registrar_paquete():
    if request.method == 'POST':
        sucursal_receptora = session.get('sucursal_id')
        if sucursal_receptora is None:
            flash('Por favor selecciona una sucursal primero.')
            return redirect(url_for('lista_sucursales'))
        
        mensajes = []

        # Validación de campos
        peso = request.form['peso']
        nombre_destinatario = request.form['nombre_destinatario']
        dir_destinatario = request.form['dir_destinatario']

        if not peso or float(peso) <= 0:
            mensajes.append('Ingrese un peso válido mayor a 0')
        if not nombre_destinatario:
            mensajes.append('No ingresó el nombre del destinatario')
        if not dir_destinatario:
            mensajes.append('No ingresó la dirección del destinatario')

        if mensajes:  # Si hay mensajes de error, renderiza el template de error
            return render_template('ErrorRegistroPaquete.html', mensajes=mensajes)
        else:
            # Si no hay errores, procede con el registro del paquete
            try:
                UltimoEnvio = Paquete.query.order_by(Paquete.numeroEnvio.desc()).first()
                if UltimoEnvio:
                    nro_envio = UltimoEnvio.numeroEnvio + 20
                else:
                    nro_envio = 0
                
                # Crea un nuevo objeto Paquete y guárdalo en la base de datos
                paquete = Paquete(
                    numeroEnvio=nro_envio,
                    peso=float(peso),
                    nomdestinatario=nombre_destinatario,
                    dirdestinatario=dir_destinatario,
                    entregado=False,
                    idsucursal=sucursal_receptora
                )
                
                db.session.add(paquete)
                db.session.commit()

                # Renderiza el template de éxito con el número de envío
                return render_template('PaqueteRegistroExito.html', mensaje='El número de envío del paquete es:', nro=nro_envio)
            
            except Exception as e:
                # Maneja cualquier error de base de datos u otro tipo de error aquí
                flash(f'Error al registrar el paquete: {str(e)}')
                return redirect(url_for('registrar_paquete'))
    return render_template('registrar_paquete.html',sucursal_numero = session['sucursal_numero'], sucursal_provincia = session['sucursal_provincia'],sucursal_localidad = session['sucursal_localidad'])

@app.route('/SalidaTransporte' ,methods=['GET', 'POST'])
def salida_transporte():
    if request.method == 'POST':
        paquetes_seleccionados = request.form.getlist('paquetes_seleccionados')
        if not paquetes_seleccionados:
            
            mensaje ='No se seleccionaron paquetes.'
            return render_template('errorSalidaTransporte.html',mensaje=mensaje)
        else:
            try:
                fecha_hora_llegada=None
                fecha_hora_salida = datetime.now()
                nro_transporte = Transporte.query.order_by(Transporte.numerotransporte.desc()).first()
                if not nro_transporte:
                    nro_transporte=100
                else:
                    nro_transporte=nro_transporte.numerotransporte+20
                transporte = Transporte(numerotransporte=nro_transporte,
                                        fechahorasalida=fecha_hora_salida,
                                        fechahorallegada = fecha_hora_llegada,
                                        idsucursal=session.get('sucursal_destino'))
                db.session.add(transporte)
                db.session.commit()
                
                for nro_envio in paquetes_seleccionados:
                    if nro_envio:
                        paquete_a_modificar=Paquete.query.filter(Paquete.numeroEnvio == nro_envio).first()
                        paquete_a_modificar.idtransporte = transporte.id
                        
                        
                print(f"Objetos modificados: {db.session.dirty}")
                db.session.commit()
                return render_template('ExitoSalidaTransporte.html',mensaje='Los paquetes se encuentran en camino, llegada estimada:',fecha_de_llegada=fecha_hora_llegada)
            except Exception as e:
                print(f"Capturo excepción: {str(e)}")
                db.session.rollback()#permite revertir lo cambios realizados en la base de datos expulsando a transporte
                mensaje = 'Error al registrar el transporte de paquetes: {e}'
                return render_template('errorSalidaTransporte.html',mensaje=mensaje)
    sucursal_actual = session.get('sucursal_id')
    paquetes = Paquete.query.filter_by(idsucursal=sucursal_actual,entregado=False,idrepartidor=None).all()#Buscamos los paquetes de la sucursal (elegida en el listado de sucursal) que no hayan sido entregado y que no tengan repartidor asignado
    return render_template('MostrarPaquetes.html',paquetes = paquetes)
@app.route('/RegistrarSalidaTransporte', methods=['GET', 'POST'])
def RegistrarSalidaTransporte():
    if request.method == 'POST':
        
        sucursal = request.form['sucursal_destino']
        if sucursal:
            session['sucursal_destino']=sucursal
            return redirect(url_for('salida_transporte'))
        else:
            flash('Seleccione una sucursal')
            return redirect(url_for('RegistrarSalidaTransporte'))
    sucursales = Sucursal.query.filter(Sucursal.id != session.get('sucursal_id')).order_by(Sucursal.numero).all()#Trae de la bases de datos las sucursales destinos ordenadas por numero de sucursal descartando la sucursal actual en una lista
    return render_template('RegistrarSalidaTransporte.html', sucursales=sucursales)




@app.route('/LLegada_transporte', methods=['GET', 'POST'])
def LLegada_transporte():
    if request.method == 'POST':
        if not request.form['transporte']:
            return render_template('ErrorLLegadaTransporte.html',mensaje='Debe ingresar un transporte!')
        else:
            try:
                idtransporte = request.form.get('transporte.id') 
                llegada_del_transporte=datetime.now()
                paquetes = Paquete.query.filter(Paquete.idtransporte == idtransporte).all()
                if not paquetes:
                    mensaje='El transporte no tenia asignados paquetes...'
                    return render_template('ErrorLLegadaTransporte.html',mensaje = mensaje)
                else:
                    for paquete in paquetes:
                        paquete.idsucursal=session.get('sucursal_destino')
                    print(f"Objetos modificados: {db.session.dirty}")
                    db.session.commit()
                    sucursal_destino=Sucursal.query.filter(Sucursal.id ==session.get('sucursal_destino')).first()
                    return render_template('ExitoLLegadaTransporte.html',mensaje = 'Se registro con exito la llegada del transporte, en la sucursal',sucursal = sucursal_destino)
            except Exception as e:
                print(f"Capturo excepción: {str(e)}")
                db.session.rollback()
                mensaje='Error al registrar la llegada del transporte...'
                return render_template('ErrorLLegadaTransporte.html',mensaje = mensaje)
        
    transportes = Transporte.query.filter(Transporte.fechahorallegada == None,Transporte.idsucursal==session.get('sucursal_destino')).all()#Analizar si la sucursal que se elije es la que ingreso el despachador en el listado de sucursales o es la sucursal destino cuando se registro la salida del transporte
    return render_template('LLegada_transporte.html', transportes=transportes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



