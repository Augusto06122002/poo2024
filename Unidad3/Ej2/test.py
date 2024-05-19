from gestor_ladrillo import gestorLadrillo
from gestor_material import gestormaterial

def menu():
    op=int(input("""
        [1]Para  un  identificador  de  ladrillo  ingresado  por  teclado:  Detallar  costo  y 
        característica del material solicitado
        [2]Mostrar para cada ladrillo el costo total de fabricación del pedido.
        [3]Para cada uno de los ladrillos fabricados mostrar el detalle asociado con el x formato
        [0]Para salir
                 """))
    return op
def test():
    GL=gestorLadrillo()
    GM=gestormaterial()
    GM.cargaM()
    GL.cargaL()
    GL.asigna_materiales(GM)
    
    op=menu()
    while(op!=0):
        if op == 1:
            GL.mostrar_datos()
            pass
        elif op == 2:
            GL.costo_fabricacion()
            pass
        elif op == 3:
            GL.mostrar_detalle_asociado()
            pass
        else:
            print(" vuelva a ingresar una opcion entre 0 a 3")
        op=menu()
    print("Saliendo del sistema")