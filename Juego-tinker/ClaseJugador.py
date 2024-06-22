from datetime import datetime



class jugador:
    __puntaje:int
    __nombre:str
    __fecha_y_hora:datetime
    def __init__(self,nombre,fecha,puntaje = 0):
        self.__puntaje = int(puntaje)
        self.__nombre= self.requerido(nombre,'El nombre es necesario')
        self.__fecha_y_hora = datetime(fecha)
   
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    
    def getPuntaje(self):
        return self.__puntaje
    
    def getNombre(self):
        return self.__nombre
    
    def fechaHora(self):
        return self.__fecha_y_hora
    
    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                puntaje = self.__puntaje,
                nombre = self.__nombre,
                fecha_hora = self.__fecha_y_hora
            )
        )
        return d
    