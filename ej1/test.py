from gestor_edificios import gestor_edificio
def opc():
    op=int(input("""
            [0]Salir del sistema
            [1]Mostrar NyA propietarios del departamento segun nombre del edificio
            [2]Mostrar superficie total cubierta de un edificio
            [3]Mostrar superficie total del dpto y porcentaje del total que ocupa el edifcio 
            [4]Indicar cantidad de departamentos con 3 habitaciones y mas de 1 baño
            ingrese opcion: """))
    return op
def test():
    GE=gestor_edificio()
    GE.carga_edificios()
    #GE.mostrar_datos_edificios()
    op=opc()
    while(op!=0):
        if(op == 1):
            try:
                nomb=input("Ingrese el nombre edificio")
                GE.mostrar_propietario(nomb)
            except AssertionError:
                print("Ingreso mal el nombre del edificio ")
        elif(op == 2):
            try:
                nomb=input("Ingreso mal el nombre del edificio ")
                GE.superficie_total(nomb)
            except AssertionError:
                "Ingreso mal el nombre del edficio"
        elif(op == 3):
            nomb=input("Ingrese el nombre del propietario")
            GE.calculo_supericie(nomb)
        elif op== 4:
            piso=int(input("Ingrese el nro del piso"))
            GE.cantidad_dptos_piso(piso)
        else:
            print("Ingreso la opcion incorrecta")
        op=opc()
        

#Consultar La funcion calculo de superficie y cantidad_dptos_piso
#Pendiente:Usar excepciones