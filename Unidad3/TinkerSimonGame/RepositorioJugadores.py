from ClaseJugador import jugador
from gestor_jugadores import GestorJugadores
from ObjectEncoder import ObjectEncoder




class repositorioJugadores:
    __manejador:GestorJugadores
    __conn:ObjectEncoder
    def __init__(self,conn):
        self.__conn=conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificadorArchivo(diccionario)
        
    def agregarJugador(self, Unjugador):
        
        self.__manejador.agregarJugador(Unjugador)
    def getListaManejador(self):
        return self.__manejador.listaJugadores()
    def mostrarPuntajes(self):
        self.__manejador.ordenarJugadores()
    def actualizarPuntaje(self,puntaje,nomb):
        self.__manejador.actualizarPuntaje(puntaje,nomb)
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
    def getListaPuntajesOrdenados(self):
        self.__manejador.PuntajesOrdenados()