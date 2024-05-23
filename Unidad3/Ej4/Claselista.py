from clasenodo import Nodo
from ClaseLibroImpreso import libro
from ClaseCD import cd
class lista:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice =0
        self.__tope = 0
    def agregarPublicacion(self,publicacion):
        nodo=Nodo(publicacion)# Se crea el nuevo nodo
        nodo.set_siguiente(self.__comienzo)#El nodo debe apuntar al nodo anterior o a null si es que no se cargo ningun otro nodo
        self.__comienzo =nodo# la cabeza apunta al nuevo nodo
        self.__actual= nodo
        self.__tope+=1
    def __iter__(self):
        return self
    def __next__(self): # esto permite recorrer la lista con un iterador
        if(self.__indice == self.__tope):
            self.__actual=self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            publicacion = self.__actual.get_publicacion()      
            self.__actual=self.__actual.get_siguiente()
            self.__indice += 1
            return publicacion
    def recorrer_lista(self):
        for publicacion in self:
            print(publicacion)
    def verificaindice(self,indice):
        assert indice <= self.__tope,print(f"Debe ser menor a {self.__tope}")
    def tipo_de_publicacion(self,indice):
        band =False
        while not band and self.__indice <= self.__tope:
            if(self.__indice == indice):
                band=True
                if(isinstance(self.__actual.get_publicacion(),libro)):
                    print("El tipo de publicacion es: libros impresos")
                    print(f"sus datos son: {self.__actual.get_publicacion()}")
                else:
                    print("El tipo de publicacion es: audio libros")
                    print(f"sus datos son: {self.__actual.get_publicacion()}")
            else:
                self.__indice += 1
                self.__actual = self.__actual.get_siguiente()
    def cantidad_de_publicaciones_por_tipo(self):
        cont_L=0
        cont_Cd=0
        for publicacion in self:
            if(isinstance(publicacion,libro)):
                cont_L+=1
            else:
                cont_Cd+=1
        print(f" Para la publicaciones de libros impresos, hay una cantidad de:{cont_L}")
        print(f" Para la publicaciones de audio libros, hay una cantidad de: {cont_Cd}")
    def mostrar_atributos_publicaciones(self):
        for publicacion in self:
            publicacion.mostrar_publicaciones()