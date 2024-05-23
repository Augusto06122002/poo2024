from Claselista import lista
from ClaseCD import cd
from ClaseLibroImpreso import libro


def menu():
    op=int(input("""
                 ------Menu De Opciones---------
                 [1]Agregar publicaciones a la colleccion
                 [2]Dada una posicion de la lista mostrar tipo de publicacion
                 [3]Mostrar la cantidad de publicaciones de cada tipo
                 [4]Recorrer la coleccion y mostrar para todas las publicaciones: Titulo,Categoria e importe de venta
                 [0]Para salir del sistema
                 Ingrese la opcion: """))
    return op
def test():
    list=lista()
    cd1=cd("El Principito", "Ficción", 20.00,tiempo=30,nomb='jorge')
    list.agregarPublicacion(cd1)
    cd2=cd("Mindfulness en la vida cotidiana", "Autoayuda", 15.50,tiempo=50,nomb='esteban')
    list.agregarPublicacion(cd2)
    l1=libro("Harry Potter y la piedra filosofal", "Fantasía", 25.00,nombreAutor='flor',fechaEdicion=2019,cantpags=250)
    list.agregarPublicacion(l1)
    l2=libro("Cocina Mediterránea", "Cocina", 18.75,nombreAutor='ventura',fechaEdicion=2012,cantpags=500)
    list.agregarPublicacion(l2)
    #list.recorrer_lista()
    opc=menu()
    while(opc != 0):
        if( opc == 1):
            l3=libro("El Gran Gatsby", "Novela", 25.99, nombreAutor ="F. Scott Fitzgerald", fechaEdicion = 1925, cantpags = 180)
            list.agregarPublicacion(l3)
            list.recorrer_lista()
        elif(opc == 2):
            try:# no es necesario se puede hacer tranquilamente despues del while
                indice=int(input("Igrese el indice de la lista "))
                list.verificaindice(indice)
                list.tipo_de_publicacion(indice)
            except:AssertionError
        elif(opc == 3):
            list.cantidad_de_publicaciones_por_tipo()
        elif(opc == 4):
            list.mostrar_atributos_publicaciones()
        else:
            print("Vuelva a ingresar un opcion vailida")
        opc=menu()
    print("-----Saliendo Del sistema-----")