class empleado:
    __NyA:str
    __id:int
    __puesto:str
    __matriculas:list
    def __init__(self,NyA,id,puesto):
        self.__NyA = NyA
        self.__id = int(id)
        self.__puesto = puesto
        self.__progamas =[]
    def inscribir_emp(self,UnaMatricula):
        self.__empleados.append(UnaMatricula)
        