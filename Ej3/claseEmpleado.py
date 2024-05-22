class empleado:
    __NyA:str
    __id:int
    __puesto:str
    __matriculas:list
    def __init__(self,NyA,id,puesto):
        self.__NyA = NyA
        self.__id = int(id)
        self.__puesto = puesto
        self.__matriculas =[]
    def inscribir_emp(self,UnaMatricula):
        self.__matriculas.append(UnaMatricula)
    def get_id(self):
        return self.__id
    def get_NyA(self):
        return self.__NyA
    def matricula_empleado_duracion(self):
        total = 0
        if(len(self.__matriculas) > 0):
            for matricula in self.__matriculas:
                Capacitacion = matricula.get_programaC()
                total+=Capacitacion.get_duracion()
        return total
    def __str__(self):
        return f"NyA: {self.__NyA}\n Id: {self.__id} \n Puesto: {self.__puesto} \n "
    def verifica_matriculacion(self):
        band=False
        if(len(self.__matriculas) >0):
            band = True
        return band