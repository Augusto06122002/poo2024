from nodo import nodo

class lista:
    __comienzo:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope =0
        
    def agregar_publicacion(self,publicacion):
        nodo = nodo(publicacion)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    def iter(self):
        return self
    def __next__(self):
        if(self.__indice == self.__tope):# quiere decir que se llego al final de la lista
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice+=1
            publicacion = self.__actual.get_dato()
            self.__actual = self.__actual.get_siguiente()
            return publicacion
    
            
