from ClaseJugador import jugador


class GestorJugadores:
    __jugadores:list
    def __init__(self):
        self.__jugadores = []
    def ordenarJugadores(self):
        self.__jugadores.sort()
    def agregarJugador(self,Unjugador):
        self.__jugadores.append(Unjugador)
    def listaJugadores(self):
        for fila in self.__jugadores:
            print(f"jugadores: {fila}")
        return self.__jugadores
    def actualizarPuntaje(self,puntaje,nomb):
        i=0
        band=False
        while i<len(self.__jugadores) and not band:
            if self.__jugadores[i].getNombre() == nomb:
                self.__jugadores[i].actualizarPuntaje(puntaje)
                band=True
            else:
                i+=1
    def toJSON(self):
        d=dict(
            __class__ =self.__class__.__name__,
            jugadores=[jugador.toJSON() for jugador in self.__jugadores]
        )
        return d
    def PuntajesOrdenados(self):
        self.__jugadores.sort(reverse=True)
        for fila in self.__jugadores:
            print(f"jugadores: {fila}")
        return self.__jugadores