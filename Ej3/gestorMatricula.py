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
        listaF=["5/6/2024","15/7/2024","20/8/2024","10/9/2024","25/10/2024"]
        indices_empleados = random.sample(range(len(GE.get_listaE())),4)#Es una lista con 4 indices distintos de la lista empleados
        
        indices_fechas = random.sample(range(len(listaF)),2)
        for i in range(len(indices_empleados)):# 4 empleados estaran matriculados en 2 cursos de capacitacion
            indices_capacitaciones = random.sample(range(len(GC.get_listaP())),2)#Es una lista 2 indices distintos de la lista programas de capacitacion
            indices_fechas = random.sample(range(len(listaF)),2)#lista de dos fechas distintas para 2 cursos de cpacitacion realizado por 1 empleado
            for j in range(len(indices_capacitaciones)):
                unaMatricula = matricula(listaF[(indices_fechas[j])],GE.get_empleado(indices_empleados[i]),GC.get_programa(indices_capacitaciones[j]))
                GE.get_empleado(indices_empleados[i]).inscribir_emp(unaMatricula)
                GC.get_programa(indices_capacitaciones[j]).capacitacion_matricula(unaMatricula)
                self.agregar_matricula(unaMatricula)
    def empleados_matriculados(self,nomb):
        band=False
     
        for matricula in self.__listaM:
            if(matricula.get_programaC().get_nombre() == nomb):
                print(matricula.get_empleado())
                band= True
        if(band !=True ):
            print("Ningun empleado registra matriculacion en el curso")
    #def muestra_matriculas(self):
        #for matricula in self.__listaM:
            #print(matricula)