



def menu():
    try: 
        op=int(input("""
                 ------Menu De Opciones---------
                 [1]insertarElemento: para insertar un objeto en una posición determinada en una colección, teniendo en cuenta el 
                 manejo de excepciones cuando la posición donde se vaya a insertar no sea válida.
                 [2]agregarElemento: para agregar un elemento al final de una colección.
                 [3]mostrarElemento: dada una posición de la colección, mostrar los datos del elemento
                 almacenado en dicha posición si esa posición es válida, en caso de que no sea válida
                 lanzar una excepción que controle el error. 
                 [0]Para salir del sistema
                 Ingrese la opcion: """))
    except ValueError:
        print("Ingrese un numero valido")
    return op
def test():
    opc=menu()
    while(opc != 0):
        if( opc == 1):
            pass
        elif(opc == 2):
            pass
        elif(opc == 3):
            pass
        elif(opc == 4):
            pass
        else:
            print("Vuelva a ingresar el numero: ")
        opc=menu()
    print("-----Saliendo Del sistema-----")