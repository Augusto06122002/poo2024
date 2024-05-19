class material:
    __material:int
    __caracteristicas:str
    __cantutilizada:float
    __costoadicional:float
    def __init__(self,mat,carc,cantu,costoa):
        self.__material = int(mat)
        self.__caracteristicas = carc
        self.__cantutilizada = float(cantu)
        self.__costoadicional = float(costoa)
    def get_caracteristica(self):
        return self.__caracteristicas
    def getcosto_adic(self):
        return self.__costoadicional
    def getmat(self):
        return self.__material