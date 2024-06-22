from ClaseJugador import jugador
from gestor_jugadores import GestorJugadores
from ObjectEncoder import ObjectEncoder




class repositorioJugadores:
    __manejador:object
    __conn:object
    def __init__(self,conn):
        self.__conn=conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificadorArchivo(diccionario)
        
    def agregarJugador(self, contacto):
        self.__manejador.agregarJugador(contacto)
    def getListaManejador(self):
        return self.__manejador.listaJugadores()
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
