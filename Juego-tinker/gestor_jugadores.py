from ClaseJugador import jugador


class GestorJugadores:
    __jugadores:list
    def __init__(self):
        self.__jugadores = []
        
    def agregarJugador(self,Unjugador):
        self.__jugadores.append(Unjugador)
    def listaJugadores(self):
        return self.__jugadores
    def toJSON(self):
        d=dict(
            __class__ =self.__class__.__name__,
            jugadores=[jugador.toJSON() for jugador in self.__jugadores]
        )
        return d