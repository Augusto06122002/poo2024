from gestor_empleado import gestor_empleado
from gestor_programa import gestor_capacitacion
from gestorMatricula import gestor_matricula


def menu():
    op=int(input("""
           [0]Salir del sistema
           [1]
           [2]
           Ingrese la opcion: """))


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
            pass
        else:
            print("opcion incorrecta")
        op=menu()
    print("Saliendo del sistema")
        