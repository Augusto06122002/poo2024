
from gestor_motos import gestor_motos #¿importo la clase o la funcion test?La clase porque asi invoco el objeto con su respectivo mensaje
from gestor_pedidos import gestor_pedidos
def opcion():
    opc = int(input("""
        ----Menu de Opciones ----
1. Leer los datos de las motos, desde un archivo denominado “datosMotos.csv” y cargarlos
en un Gestor de Motos.
2. Leer los datos de los pedidos, desde un archivo denominado “datosPedidos.csv”, y
cargarlos en el Gestor de Pedidos.
3. Cargar nuevos pedidos, leer los datos por teclado, y asignar a una moto el pedido, al
solicitar la patente de la moto para asignarla, validar que la moto existe.
4. Leer por una patente de una moto, mostrar los datos del conductor y el tiempo promedio
real de entrega de los pedidos que hizo.
5. Generar un listado para cada moto, para el pago de comisiones a los conductores de las
motos: 
0 para salir del sistema
-Ingrese:  """))
    return opc

if __name__ == '__main__':
    op=opcion()
    while op!=0:
        if op == 1:
            moto = gestor_motos()
            moto.test()
            print(f'Se realizo la lectura de los datosmotos.csv')
        elif op == 2:
            pedido =gestor_pedidos()
            pedido.test()
            print(f'Se realizo la lectura de los datospedidos.csv')
        elif op == 3:
            pedido.carga_nuevos_pedidos()
        elif op == 4:
            p=input("ingrese patente del conductor")
            moto=gestor_motos()
            if(moto.muestra_conductor(p)!=None):
                pedido.tiempo_promedio_real(p)
        op=opcion()


        


