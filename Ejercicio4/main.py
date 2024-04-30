
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
5. Leer por teclado número de patente, identificador de pedido, y tiempo real de entrega,
modificar en el Gestor de Pedidos, el tiempo real de entrega para ese pedido.
6. Generar un listado para cada moto, para el pago de comisiones a los conductores de las
motos: 
0 para salir del sistema
-Ingrese:  """))
    return opc

if __name__ == '__main__':
    moto = gestor_motos()
    moto.testMotos()
    pedido =gestor_pedidos()
    pedido.testPedidos()
    op=opcion()
    print(f'Se realizo la lectura de los datosmotos.csv')
    while op!=0:
        if op == 1:
            pass
        elif op == 2:
            pedido.ordena_pedidos()
            print(f'Se ordenaron lo pedidos ascendentemente de los datospedidos.csv')
        elif op == 3:
            pedido.carga_nuevos_pedidos(moto)
        elif op == 4:
            p=input("ingrese patente del conductor")
            if(moto.muestra_conductor(p)!=None):
                pedido.tiempo_promedio_real(p)
            else:
                print("La moto no se encontro")
        elif op ==5:
            patente=(input("Ingrese la patente del conductor"))
            id=int(input("Ingrese el identificador del pedido"))
            tr=int(input("Ingrese el tiempo real por el cual se modificara"))
            pedido.modifica_tiempo_real(patente,id,tr,moto)
        elif op ==6:
            moto.genera_listado(pedido)
        op=opcion()
        
        
        """Lote de prueba
3
2
3
31
asado
20
30
560
BCD890
4
BCD890
4
ABC123
16
100
        """


        


