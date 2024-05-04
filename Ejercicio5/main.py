from GestorEquipos import gestorEquipos
from GestorFecha import gestorfechas
import os
def menu():
    print("-----Menu de opciones-----")
    op=int(input("""
[1] Leer los datos de los equipos del archivo y almacenarlos en el Gestor de Equipos
[2] Leer los datos de las Fechas de Fútbol, y almacenarlos en el Gestor de Fechas.
[3] Leer el nombre de un equipo y obtener un listado con el siguiente formato.
[4]Actualiza tabla de todos lo equpos (por fechas jugadas)
[5]Ordenar  la  tabla  de  posiciones  de  mayor  a  menor
[6]Almacenar la tabla de posiciones ordenada en el punto anterior en un archivo .csv.
[7]directorio
[0] Para Salir del sitema ]
Ingrese Opcion:  """))
    return op
    
    
if __name__ =='__main__':
    opc=menu()
    while(opc!=0):
        if( opc == 1):
            GE=gestorEquipos()
            GE.test_equipos()
            print("----Se cargo con exito el gestor equipos----")
        elif opc == 2:
            GF=gestorfechas()
            GF.test_fechas()
            print("---Se cargo con exito el gestor de fechas de futbol---")
        elif opc ==3:
            GE.listado_equipos(GF)
        elif opc ==4:
            GE.actualizar_equipos(GF)
        elif opc ==5:
            GE.ordenar_equipos()
            GE.muestra_equipos_ordenados()
        elif opc ==6:
            GE.carga_equipos_ordenados()
        elif(opc ==7):
            print(os.getcwd())
        else:
            print("opcion incorrecta")
        opc=menu()
    print("--Se salio con exito del sistema---")
    
    
    
"""Lote de prueba
1
2
3
EquipoA
4
5

"""