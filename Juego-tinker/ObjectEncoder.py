from ClaseJugador import jugador
from gestor_jugadores import GestorJugadores

from pathlib import Path
import json
class ObjectEncoder:
    __pathArchivo:object#Amacena la ruta del archivo JSON
    def __init__(self,path_archivo):
        self.__pathArchivo = path_archivo
    def decodificadorArchivo(self,d):#Basicamente convierte el diccionario jugador en un objeto de la clase jugador
        if '__class__'not in d:#Si la clase no tiene el diccionario
            return d
        else:
            class_name = d['__class__']#Le asigna el nombre de la clase
            class_=eval(class_name)#Convertir el nombre de la clase (una cadena) en una referencia a la clase real en el código Python
            if class_name == 'GestorJugadores':
                jugadores=d['jugadores']#lista de jugadores del diccionario
                gestor=class_()#Instancia de la clase gestor jugadores
                for i in range(len(jugadores)):#recorre la lista de jugadores
                    dJugador=jugadores[i]#obtiene el diccionario de cada jugadro
                    class_name=dJugador.pop('__class__')#elimina y obtiene el valora asociado a la clase jugador
                    class_ = eval(class_name)#referencia a la clase jugador
                    atributos = dJugador['__atributos__']#atributos de la clase jugador
                    unJugador = class_(**atributos)#Se le asignan todos los atributos al objeto
                    gestor.agregarJugador(unJugador)#Se agrega a la lista
            return gestor
        
    def guardarJSONArchivo(self,diccionario):
        with Path(self.__pathArchivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()
            
    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario