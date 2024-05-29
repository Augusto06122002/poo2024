#---------------------------------------------------------------------Herencia Simple-----------------------------------------------------------------
#tenemos una clase padre que es circulo y la clase hijo que es cilindro
# si tenemos dos metodos con el mismo nombre en la clase hijo y en la clase padre, hay que tener en cuenta cuando utilizar el self o el supe()
import math
class Circulo:
    __radio:float
    def __init__(self,radio):
       self.__radio =radio 
    def getRadio(self):
        return self.__radio
    def superficie(self):
        return math.pi*self.__radio**2
class Cilindro(Circulo):#Indica que la clase cilindro hereda metodos y atributos de la clase circulo
    __altura:float #atributo propios
    def __init__(self,radio,altura):#Inicializa los atributos propios y ademas debe inicializar los atributos de la clase base/padre
        super().__init__(radio)#con super hace referencia a la clase padre/superior, llama al constructor de la clase y pasa el atributo de la misma
        self.__altura =altura
    def superficie(self):
        superficeLateral = math.pi*2*self.getRadio()# como heradada los metodos tambien se podria llamar ya sea con el propio self o con el super()
        superficieCirculo = super().superfice()# si o si con el super() porque si lo hago con el self estaria usando el metodo de la clase cilindro, por tanto quedaria anulado el metodo superficie de circulo y no la de la clase circulo
        return superficeLateral + 2*superficieCirculo
class punto(object):# implicitamente todas las clases heredan de la clase object de python 
    pass
if __name__ =='__main__':
    print(dir(punto))#
#---------------------------------------------------------------------------------Herencia Multiple-------------------------------------------------------------------------------------
#Una subclase se deriva de mas de  una clase base
#problemas que vienen con esta cual clase padre inicializar primero, si tenemos el mismo nombre en ambas clases padres como hago para acceder con super(al metodo de la clase padre que necesito)
#Python soluciona esto atraves de MRO arranca de arriba hacia abajo y si esta en un mismo nivel va de derecha a izquierda
class Persona(object):
    __dni: int
    __apellido: str
    __nombre:str
    def __init__(self, dni, apellido, nombre, codigoCargo=0, agrupamiento=0,
        catedra='', sueldo=0.0, fechaIngreso='', promedio=0.0, carrera=''):# tiene los atributos propios y ademas de docento y los de alumno
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
    def mostrarDatos(self):
        print('Datos Persona')
        print('DNI: {0:9d}'.format(self.__dni))
        print('Apellido: {}, Nombre: {}'.format(self.__apellido, self.__nombre))
class Docente(Persona):# hereda de persona
    __codigoCargo: str
    __agrupamiento: int
    __catedra: str
    __sueldo: float
    def __init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera,
        codigoCargo, agrupamiento, catedra, sueldo):# Atributos de propios de docente y persona
        super().__init__(dni, apellido, nombre, fechaIngreso, promedio,
        carrera, codigoCargo, agrupamiento,catedra, sueldo)# Inicializa los atributos de persona
        self.__codigoCargo=codigoCargo
        self.__agrupamiento=agrupamiento
        self.__catedra=catedra
        self.__sueldo=sueldo
    def mostrarDatos(self):
        super().mostrarDatos()# metodo de la clase persona
        print('Datos del Docente')
        print('Codigo cargo {}/{}'.format(self.__codigoCargo, self.__agrupamiento))
        print('Cátedra: {0}, sueldo ${1:8.2f}'.format(self.__catedra, self.__sueldo))
class Alumno(Persona):# herda de persona
    __fechaIngreso: str
    __promedio: float
    __carrera: str
    def __init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera,
    codigoCargo, agrupamiento,catedra, sueldo):
        super().__init__(dni, apellido, nombre, fechaIngreso, promedio,
        carrera, codigoCargo, agrupamiento,catedra, sueldo)
        self.__fechaIngreso=fechaIngreso
        self.__promedio=promedio
        self.__carrera=carrera
    def mostrarDatos(self):
        super().mostrarDatos()# metodo de clase de persona
        print('Datos del Alumno')
        print('Carrera: {}, fecha de ingreso: {}'.format(self.__carrera, self.__fechaIngreso))
        print('Promedio {0}'.format(self.__promedio))
class Ayudante(Docente, Alumno):# Esta es la que tiene herencia multiple# si se declara si se cambia el orden de las clases padres la salida suoer().mostrardatos() seria primero person, luego docente y al ultimo alumno
    #atributos propios
    __concepto: str
    __horasLIA: int
    def __init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera, codigoCargo, agrupamiento, catedra, sueldo, concepto, horasLIA=0):# todos los atributos de person, alumno, docente y los propios cabe aclara el orden en el que estan dispuesto cada atributo , primero es de arriba hacia abajo es decir en primer lugar python considera a los atributos de person , lugo va de derecha a izquierda es decir a persona le sigue alumnoy a esta docente
        # Docente.__init__(self, dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo)
        # Alumno.__init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera)
        # es poco reusable lo mas conveniente es utilizar super()
        super().__init__(dni, apellido, nombre, fechaIngreso, promedio, carrera, codigoCargo, agrupamiento, catedra, sueldo)# primero inicializa la clase persona ,luego inicializa la clase alumno y por ultimo la clase docente
        self.__concepto=concepto
        self.__horasLIA=horasLIA
        def mostrarDatos(self):
            super().mostrarDatos()# primero imprime persona, despues el de alumno y depues imprime docente
            print('Datos Ayudante')
            print('Horas LIA {}'.format(self.__horasLIA))
            print('Concepto: {}'.format(self.__concepto))
            
"""""Como se vio en el ejemplo anterior, se hizo muy tedioso pasar argumentos a los constructores de las clases intermedias y clase base.
¿Existirá otra forma de resolverlo que oculte esa cantidad de parámetros?"""
class Circulo:
    __radio: float
    def __init__(self, radio):
        self.__radio=radio
    def getRadio(self):
        return self.__radio
class Cilindro(Circulo):
    __altura: float
    def __init__(self, radio, **kwargs):#**kwargs diccionario(los subindices pueden ser cualquiere tipo de dato(reales, enteros, str, etc),se accede al valor de la altura=8 con el subindice que en este caso es kwargs['altura'] )
        super().__init__(radio)
        self.__altura=kwargs['altura']
    def __str__(self):
        return f'Radio: {self.getRadio()}, Altura: {self.__altura}'
if __name__=='__main__':
    cilindro=Cilindro(radio=4,altura=8)# cada valor tiene asociado un nombre (tener en cuenta porque sino no funcionaria el diccionario)
    print(cilindro)
#-----------------------------------------------------------------------------------PORLIMORFISMO---------------------------------------------------
# polimorfismo es la capacidad que tiene  2 objetos de clases distintas de responder a un mismo mensaje de forma distinta
#polimorfismo de subtipo -> se basa en la  herencia y  en la vinculacion dinamica
# ventajas sea mas reusable y mas flexible
# vinculacion dinamica -> cuando tengo un objeto y le envio un mensaje el identificar esa vinculacion entre el objeto y el codigo del mensaje que tiene que ejecutarse, es vinculacion se produce de forma dinamica, es decir durante el tiempo de ejecucion
# Python es un lenguaje con tipado dinamico, la vinculacion de un objeto con un metodo tambien es dinamica
#Todos los metodos se vinculan a las instancias en tiempo de ejecucion
#Para lleavar este tipo de vinculacion, se utiliza una tabla de metodos virtuales por cada clase
#Preguntas de examen ¿Cuantas tablas de metodos virtuales tengo ?Una por clase
import numpy as np
import math
class Cuerpo:# clase abstracta no voy a tener instancias de cuerpo
    __altura: float
    def __init__(self, altura):
        self.__altura=altura
    def superficieBase():
        pass
    def volumen(self):
        return self.superficieBase()*self.__altura #superficieBase() lo busca en su clase, cabe aclarar que no hace nada
    def getAltura(self):
        return self.__altura
class Cilindro(Cuerpo):
    __radio: float
    def __init__(self, altura, radio):
        Cuerpo.__init__(self,altura)# puede ser super()
        self.__radio=radio
    def __str__(self):
        cadena ='Cilindro, altura ={}, radio = {}'.format(self.getAltura(), self.__radio)
        return cadena
    def superficieBase(self):
        return math.pi*self.__radio**2
class ParalelepipedoRectangulo(Cuerpo):
    __lado1: float
    __lado2: float
    def __init__(self, altura, lado1, lado2):
        Cuerpo.__init__(self,altura)# puede ser super()
        self.__lado1=lado1
        self.__lado2=lado2
    def __str__(self):
        cadena = 'Paralelepípedo Rectángulo, altura = {}, lado a={}, lado b={}'.format(self.getAltura(), self.__lado1, self.__lado2)
        return cadena
    def superficieBase(self):
        return self.__lado1*self.__lado2
    #main
    #cilindro.volumen()# este metodo lo hereda de clase cuerpo, pero al momento de hacer self.superficieBase(), es self hara referencia al objeto cilindro por lo tanto ejecutara su metodo propio
class Arreglo:
    __dimension: int
    __actual: int
    __cuerpos: object# object tambien es del np.array
    def __init__(self, dimension=10):
        self.__cuerpos = np.empty(dimension, dtype=Cuerpo)# Se pone cuerpo porque es la clase base para poder guardar tanto cilindros como paraledepipedos, pero en realidad va a tener instancias de paraledepipedo o cilindro
        self.__dimension=dimension
        self.__cantidad=0
    def agregarCuerpo(self, unCuerpo):
        self.__cuerpos[self.__actual]=unCuerpo
        self.__actual+=1
    def calcularVolumenCuerpos(self):
        for i in range(self.__actual):
            cuerpo=self.__cuerpos[i]
            print(str(cuerpo)+', Volumen = {0:7.2f}'.format(cuerpo.volumen()))#El cuerpo podria ser un cilindro o un paraledepipedo dependiendo del objeto que sea, responderan de distintas maneras al mismo mensaje
def testPolimorfismo():
    arreglo = Arreglo()
    p = ParalelepipedoRectangulo(3,5,4)
    arreglo.agregarCuerpo(p)
    c = Cilindro(5,6)
    arreglo.agregarCuerpo(c)
    p = ParalelepipedoRectangulo(11,6,4)
    arreglo.agregarCuerpo(p)
    c = Cilindro(8,7)
    arreglo.agregarCuerpo(c)
    arreglo.calcularVolumenCuerpos()
if __name__=='__main__':
    testPolimorfismo()
# como se la clase de un objeto en particular con type() o con isinstance()->preferentemente este
def determinarClaseDeObjetos(self):
    cantidadP = 0
    cantidadC = 0
    for i in range(self.__actual):
        if isinstance(self.__cuerpos[i], ParalelepipedoRectangulo):#Devuelve true si el objeto es instancia de la clase
            cantidadP+=1
    else:
        if isinstance(self.__cuerpos[i], Cilindro):
            cantidadC+=1
            print('Cantidad de Paralelepidedos Rectángulo: ', cantidadP)
            print('Cantidad de Cilindros: ', cantidadC)
def determinarClaseDeObjetos(self):
    cuenta=0
    cantidadP = 0
    cantidadC = 0
    for i in range(self.__actual):
        if isinstance(self.__cuerpos[i], Cuerpo):# Siempre va entrar en este if porque todas las instancias de la clases(cilindro y paraledepipedo) que herandan cuerpo , son justamente instancias de cuerpo(CUALQUIER OBJETO DE LA CLASE PADRE/BASE ES INSTANCIA DE LA MISMA)
            cuenta+=1
        else:
            if isinstance(self.__cuerpos[i], ParalelepipedoRectangulo):
                cantidadP+=1
            else:
                if isinstance(self.__cuerpos[i], Cilindro):
                        cantidadC+=1
                        print('Cuenta: ', cuenta)
                        print('Cantidad de Paralelepidedos Rectángulo: ', cantidadP)
                        print('Cantidad de Cilindros: ', cantidadC)
"------------------------------------------------------Clase Base Abstracta-----------------"
#Una clase abstracta no puede ser instanciada
# Una clase en python, es abstracta si tiene un metodo abstracto
#Python define e implementa la abstraccion de clases, mediante meta clases y decoradores
#El decorador para establecer que un metodo es abstracto es, @abc.abstractmethod
#Una meta clase, es una clase que sirve de instancia a otras clases
"Se sigue el ejemplo de polimorfismo"
import abc
from abc import ABC
import numpy as np
import math
class Cuerpo(ABC):# con esto indico que la clase es abstracto, por lo tanto no va a permitir crear una instancia de la misma
    __altura: int
    def __init__(self, altura):
        self.__altura=altura
    @abc.abstractmethod
    def superficieBase():
        pass
    def volumen(self):
        return self.superficieBase()*self.__altura
    def getAltura(self):
        return self.__altura
"A partir de esta definición de la clase Cuerpo, las clases ParalelepipedoRectangulo y Cilindro, se ven obligadas a reescribir el método superficieBase(), de lo contrario, lo heredan como método abstracto, y automáticamente se convierten en clases abstractas. "
