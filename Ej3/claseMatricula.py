class matricula:
    __fecha:str
    __empleado:object
    __programa:object
    def __init__(self,fecha,Unempleado,Unprograma):
        self.__fecha = fecha
        self.__empleado = Unempleado
        self.__programa = Unprograma
    def get_programaC(self):
        return self.__programa
    def get_empleado(self):
        return self.__empleado
    def __str__(self):
        print("Empleado matriculado:")
        return f"Fecha: {self.__fecha}\n empleado: {self.__empleado}\n capacitacion {self.__programa}\n "