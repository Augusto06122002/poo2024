class edificio:
    __id:int
    __nombre:str
    __direccion:str
    __empresa_costructora:str
    __pisos:int
    __departamentos:int
    __dpto:list
    def __init__(self,id,nomb,dir,ec,cp,cd):
        self.__id = int(id)
        self.__nombre = nomb
        self.__direccion = dir
        self.__empresa_costructora = ec
        self.__pisos =int (cp)
        self.__departamentos= int(cd)
        self.__dpto=[]
    def __str__(self):
        return f"idEdificio: {self.__id}|| nombreEdificio: {self.__nombre}|| direccionEdificio: {self.__direccion} || empresa constructora: {self.__empresa_costructora} || cant de pisos: {self.__pisos} || cant departamentos: {self.__departamentos} "
        
    def agregar_dpto(self,undepto):
        self.__dpto.append(undepto)
    def getlista(self):
        return self.__dpto
    def mostrar_deptos(self):
        for dpto in self.__dpto:
            print(dpto)
    def getnomb(self):
        return self.__nombre
    def get_pisos(self):
        return self.__pisos

   