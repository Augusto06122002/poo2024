import csv

from claseEmpleado import empleado

class gestor_empleado:
    __listaE:list
    def __init__(self):
        self.__listaE=[]
    def agregar_empleado(self,emp):
        self.__listaE.append(emp)
    def get_listaE(self):
        return self.__listaE
    def get_empleado(self,pos):
        return self.__listaE[pos]
    def cargaE(self):
        band= True
        archivo =open('empleado.csv')
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if(band):
                band=False
            else:
                Unempleado=empleado(fila[0],fila[1],fila[3])
                self.agregar_empleado(Unempleado)
                
    