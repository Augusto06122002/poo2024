from gestor_empleado import gestor_empleado
from gestor_programa import gestor_capacitacion
from gestorMatricula import gestor_matricula


def menu():
    op=int(input("""
           [0]Salir del sistema
           [1]Iforma duracion de todos los programas de capacitacion en los que esta matriculado x empleado
           [2]Muestra el/los empleados matriculados de x programa de capcitacion
           [3]Informa empleados que no estan matriculados en los programas de capacitacion
           Ingrese la opcion: """))
    return op
def test():
    GE=gestor_empleado()
    GE.cargaE()
    GC=gestor_capacitacion()
    GC.cargaP()
    GM=gestor_matricula()
    GM.Asigna_Matriculas(GE,GC)
    
    
    op=menu()
    while(op != 0):
        if(op == 1):
            id=int(input("Ingrese el id del empleado"))
            GE.informa_duracion(id)
        elif op==2:
            nomb=input("Ingrese el nombre del programa de capacitacion")
            GM.empleados_matriculados(nomb)
        elif op==3:
            #GM.muestra_matriculas()
            GE.iforma_empleados_sinMatriculacion()
        else:
            print("opcion incorrecta")
        op=menu()
    print("Saliendo del sistema")
        