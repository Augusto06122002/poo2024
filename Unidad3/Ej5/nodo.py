from ClasaPublicacion import publicacion
class nodo:
    __publicacion:publicacion
    __siguente:object
    def __init__(self,publicacion):
        self.__publicacion = publicacion
        self.__siguente = None
    def get_siguiente(self):
        return self.__siguente
    def set_siguiente(self,siguiente):
        self.__siguente = siguiente
    def get_dato(self):
        return self.__publicacion