import csv
from ClasePedido import ClasePedido
from gestor_motos import gestor_motos 

class gestor_pedidos:
    __ListaPedidos:list
    def __init__ (self):
        self.__ListaPedidos = []
    def agrega(self,unPedido):
        self.__ListaPedidos.append(unPedido)
    def test(self):
        archivo = open(r"C:\Users\titom\Documents\POO\Unidad2\codigo\Ejercicio4\datosPedidos.csv")
        reader = csv.reader(archivo)
        band = True
        for fila in reader:
            if (band):
                "encabezado"
                band = not band
            else:
                pt = fila[0]
                id = fila[1]
                cp = fila[2]
                te = fila[3]
                tr = fila[4]
                pr = fila[5]
                unPedido=ClasePedido(pt,id,cp,te,pr,tr)
                self.agrega(unPedido)
    def carga_nuevos_pedidos(self):
        lista=[]
        id=int(input("ingrese identificador del pedido"))
        cp=(input("ingrese comida pedida"))
        te=int(input("ingrese tiempo estimado del pedido"))
        tr = int(input("ingrese el timepo real del pedido"))
        pr = float(input("Ingrese el precio del pedido"))
        patente=(input("Ingrese patente para asignarla al repartidor "))
        gestorMoto=gestor_motos()
        if(gestorMoto.valida_moto(patente)!=None):
            print("la moto existe")
            nuevo=ClasePedido(patente,id,cp,te,pr,tr)
            lista.append(nuevo)
            self.__ListaPedidos.extend(lista)
        else:
            print("La moto no existe")    
    def tiempo_promedio_real(self,p):
        sum=0
        cant=0

        for i in range(self.__ListaPedidos):
            if(self.__ListaPedidos[i].obtener_Patente_Asignada()==p):
                cant+=1
                sum+=self.__ListaPedidos[i].obtener_tiempoReal()
        prom=sum//cant
        print(f"El tiempo promedio real en que realizo la entrega de sus pedidos fue de: {prom} minutos")
        