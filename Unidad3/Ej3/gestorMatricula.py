import csv
import random

from claseMatricula import matricula
class gestor_matricula:
    __listaE:list
    def __init__(self):
        self.__listaM =[]
    def agregar_matricula(self,Unamatricula):
        self.__listaM.append(Unamatricula)
    
    def Asigna_Matriculas(self,GE,GC):
        listaF=[05-06-2024,15-07-2024,20-08-2024,10-09-2024,25-10-2024]
        for i in range(4): #A 4 empleados se le asigna 2 capcitaciones
            indE=random.choice(len(GE.get_listaE()))
            indC=random.choice(len(GE.get_listaP()))
            inF=random.choice(len(listaF))
            unaMatricula = matricula(listaF(inF),GE.get_empleado(indE),GC.get_programa(indC))
            GE.inscribir_emp(unaMatricula)
            GC.capacitacion_matricula(unaMatricula)
            self.agregar_matricula(unaMatricula)
            