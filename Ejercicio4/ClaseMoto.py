class ClaseMoto:
    __patente:str
    __marca:str
    __NyA:str
    __kilometraje:float
    def __init__(self,p,m,nya,k):
        self.__patente = p
        self.__marca = m
        self.__NyA = nya
        self.__kilometraje = k
    def obtenerPatente(self):
        return self.__patente
    def obtenerNyA(self):
        return self.__NyA
