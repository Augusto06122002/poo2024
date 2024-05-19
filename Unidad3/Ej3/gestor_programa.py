import csv

from claseProgamaCapacitacion import capacitacion
class gestor_capacitacion:
    __listaE:list
    def __init__(self):
        self.__listaP =[]
    def agregar_programa(self,programa):
        self.__listaP.append(programa)
    def get_listaP(self):
        return self.__listaP
    def get_programa(self,pos):
        return self.__listaE[pos]
    def cargaP(self):
        band= True
        archivo =open('programas.csv')
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if(band):
                band=False
            else:
                Unprograma=capacitacion(fila[0],fila[1],fila[3])
                self.agregar_programa(Unprograma)
    