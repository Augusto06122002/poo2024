from GestorCliente import gestorcliente
from GestorMovimiento import gestormovimiento
#falla la carga del numpy siempre falla en el gestor de movimiento, no encontre el error
def menu():
    op=int(input("""
        [1]Lista cliente y actualiza su saldo en funcion de movimientos
        [2]Informa si el cliente no tuvo movimiento
        [3]Ordenar movimientos(antes de la opcion 1)
        [0]salir del sistema       
                 
                 
                 
                 """))
    return op

if __name__=='__main__':
    GC=gestorcliente()
    GC.carga_cliente()
    GM=gestormovimiento()
    GM.carga_movimiento()
    
    op=menu()
    while(op!=0):
        if(op == 1):
            GC.listado_cliente(GM)# funciona bien
        elif(op == 2):
            GC.informa_movimiento(GM) # funciona bien
        elif(op == 3):
            GM.ordena_movimiento()# errror: TypeError: '<' not supported between instances of 'int' and 'movimiento'
        
        
        else:
            print("ingreso mal")
        op=menu()