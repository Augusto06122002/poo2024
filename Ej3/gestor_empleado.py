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
                Unempleado=empleado(fila[0],fila[1],fila[2])
                self.agregar_empleado(Unempleado)
        archivo.close()
    def informa_duracion(self,id):
        i=0
        band = True
        while( i< len(self.__listaE) and band == True):
            if(self.__listaE[i].get_id() == id):
                band= False
                print(f"El empleado {self.__listaE[i].get_NyA()} registra una duracion total de {self.__listaE[i].matricula_empleado_duracion()} minutos en los programas de capcitacion")
            else:
                i+=1
    def iforma_empleados_sinMatriculacion(self):
        for empleado in self.__listaE:
            if(empleado.verifica_matriculacion()):
                "El empleado esta matriculado"
                pass
            else:
                print("El empleado no esta matriculado: ")
                print(empleado)
                