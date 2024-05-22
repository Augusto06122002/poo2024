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
    def get_duracion(self):
        return self.__duracion
    def get_nombre(self):
        return self.__Nombre
    def __str__(self):
        return f"NyA: {self.__Nombre}\n codgo: {self.__codigo} \n Duracion: {self.__duracion} \n "
        
        
        