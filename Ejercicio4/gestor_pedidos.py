import csv
from ClasePedido import ClasePedido
from gestor_motos import gestor_motos 

class gestor_pedidos:
    __ListaPedidos:list
    def __init__ (self):
        self.__ListaPedidos = []
    def agrega(self,unPedido):
        self.__ListaPedidos.append(unPedido)
    def testPedidos(self):
        archivo = open(r"C:\Users\ventu\Documents\Facultad sisitema\Programacion orientada a objetos\UNIDAD 2\PracticaU2\Ejercicio4\datosPedidos.csv")
        reader = csv.reader(archivo)
        band = True
        for fila in reader:
            if (band):
                "encabezado"
                band = not band
            else:
                pt = fila[0]
                id = int(fila[1])
                cp = fila[2]
                te = int(fila[3])
                tr = int(fila[4])
                pr = float(fila[5])
                unPedido=ClasePedido(pt,id,cp,te,pr,tr)
                self.agrega(unPedido)
        archivo.close()
    def ordena_pedidos(self):
        """print("Lista de pedidos antes de ordenar:")
            for pedido in self.__ListaPedidos:
            print(f"La patente es: {pedido.obtener_Patente_Asignada()}")
            print(f"El id es: {pedido.obtener_identificador()}")
            print(f"La comida es: {pedido.obtener_comidas_pedidas()}")
            print(f"el tiempo estimado es: {pedido.obtener_tiempo_estimado()}")
            print(f"el tiempo real es: {pedido.obtener_tiempoReal()}")
            print(f"su precio es de: {pedido.obtener_precio()}")"""
        self.__ListaPedidos=sorted(self.__ListaPedidos)
       #print (depues de ordenar, funciona bien)
            
    def carga_nuevos_pedidos(self):
        lista=[]
        id=int(input("ingrese identificador del pedido"))
        cp=(input("ingrese comida pedida"))
        te=int(input("ingrese tiempo estimado del pedido"))
        tr = int(input("ingrese el timepo real del pedido"))
        pr = float(input("Ingrese el precio del pedido"))
        patente=input("Ingrese patente para asignarla al repartidor ")
        gestorMoto=gestor_motos()
        if(gestorMoto.valida_moto(patente) is not None):
            print("Se agrego con exito...")
            nuevo=ClasePedido(patente,id,cp,te,pr,tr)
            lista.append(nuevo)
            self.__ListaPedidos.extend(lista)
        else:
            print("La moto no existe")
    
    def tiempo_promedio_real(self,p):
        sum=0
        cant=0

        for pedido in self.__ListaPedidos:
            if(pedido.obtener_Patente_Asignada()==p):
                cant+=1
                sum+=pedido.obtener_tiempoReal()
        if(cant != 0):
            prom=sum//cant
            print(f"El tiempo promedio real en que realizo la entrega de sus pedidos fue de: {prom} minutos")
        else:
            print("El conductor no realizo entregas")