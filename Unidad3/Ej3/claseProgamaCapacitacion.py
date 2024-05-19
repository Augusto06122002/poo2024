class capacitacion:
    __Nombre:str
    __codigo:str
    __duracion:int
    __matricula:list
    def __init__(self,nombre,codigo,duracion):
        self.__Nombre = nombre
        self.__codigo = codigo
        self.__duracion = int(duracion)
        self.__matricula =[]
    def capacitacion_matricula(self,Unamatricula):
        self.__matricula.append(Unamatricula)
        
        