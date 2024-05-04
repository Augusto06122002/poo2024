""""De cada Fecha de fútbol se registran: fecha del partido, identificador de equipo local, identificador 
de equipo visitante, cantidad de goles que hizo el equipo local, cantidad de goles que hizo el equipo 
visitante. """
class fechafutbol:
    __fechaP:str
    __idLocal:int
    __idVistante:int
    __golesLocal:int
    __golesVisitante:int
    def __init__(self,fecha,idL,idV,golesl,golesv):
        self.__fechaP = fecha
        self.__idLocal = idL
        self.__idVistante = idV
        self.__golesLocal = golesl
        self.__golesVisitante = golesv
    def getfecha(self):
        return self.__fechaP
    def getidL(self):
        return self.__idLocal
    def getidV(self):
        return self.__idVistante
    def get_GolV(self):
        return self.__golesVisitante
    def get_GolL(self):
        return self.__golesLocal
    
    
    
    
