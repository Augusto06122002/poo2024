

from flask import Flask
app = Flask(__name__) #Creacion de la instancia

@app.route('/')#ruta raiz, cuando es una barra sola
def saludo():
 return 'Mi primera aplicación con Flask!'
if __name__ == '__main__':
    app.run() 
""""El método run, posee argumentos que son opcionales, y permiten configurar el modo de
operación del servidor web. Durante el desarrollo, es conveniente habilitar el modo de
depuración, pasando el argumento de depuración establecido a True como se muestra a
continuación:"""
if __name__ == '__main__':
 app.run(debug=True) 
 #4. Agregando funcionalidades 
""""Por ejemplo, si queremos controlar la ruta ‘/saludo’ el método route se invocará como:
 @app.route('/saludo')
Un ejemplo de aplicación con más de una ruta se muestra en la siguiente imagen."""

@app.route('/saludo_bienvenida')
def saludoBienvenida():
    return 'Bienvenido a mi aplicacion Flask'
@app.route('/saludo_despedida')
def saludoDespedida():
    return 'Gracias por visitar mi aplicacion Flask!'
#Hasta aca es una aplicacion flask

#Ahora para que estas aplicacion flask sean paginas web icorporamos html(en el archivo de html)
"""Para vincular una aplicación Flask con una página web se puede utilizar el método
render_template(), que permite procesar un archivo HTML."""
from flask import render_template
@app.route('/')
def saludo():
 return render_template('inicio.html')#parametro nombre de la pagina que queremos que muestre
"""Flask buscará el archivo HTML en la carpeta templates, la cual debe encontrarse dentro de la
carpeta que contiene la aplicación .py. """ 

from flask import request
def bienvenida():
    if request.method =='POST':#puedo saber si los datos que viene desde la paginan finene con un get o un post()
        c=request.form['nombre_componente']#Accedo al formulario y el subindice es el nombre del componente para obtener el dato que se ingreso en el formulario