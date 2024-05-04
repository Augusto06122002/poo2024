import csv

from Clasecliente import cliente
class gestorcliente:
    __lista_clientes:list
    def __init__(self):
        self.__lista_clientes=[]
    def carga_cliente(self):
        band=True
        archivo=open(r"C:\Users\ventu\Documents\Facultad sisitema\Programacion orientada a objetos\UNIDAD 2\PracticaU2\PracticaOperativa(tema 2 2024)\ClientesFarmaCiudad.csv")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            if(band):
                "encabezado"
                band=False
            else:
                uncliente=cliente(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista_clientes.append(uncliente)
        archivo.close()
    def busca_cuenta(self,dni):
        i=0
        band=True
        cuenta=-1
        while(i<len(self.__lista_clientes) and band):
            if(self.__lista_clientes[i].getdni()==dni):
                cuenta =i
                band=False
            else:
                i+=1
        return cuenta
    def listado_cliente(self,gm):
        dni=int(input("Ingrese el dni del cliente"))#20555678
        pos=self.busca_cuenta(dni)
        if(pos!=-1):
            print(f"Cliente: {self.__lista_clientes[pos].get_apell()} {self.__lista_clientes[pos].get_nom()}numero de cuenta:{self.__lista_clientes[pos].get_cuenta():>20}")
            print(f"saldo actual: {self.__lista_clientes[pos].get_saldo()}")
            print("Fecha    descripcion    importe   tipo de movimiento")# agregado
            monto=gm.listado_movimiento(self.__lista_clientes[pos].get_cuenta())# correccion le falto ()
            saldo=self.__lista_clientes[pos].get_saldo()+monto
            self.__lista_clientes[pos].actualiza_saldo(saldo)
            print(f"saldo actual: {self.__lista_clientes[pos].get_saldo()}")
    def informa_movimiento(self,gm):
        dni=int(input("ingrese dni del cliente"))
        pos=self.busca_cuenta(dni)
        cuenta=self.__lista_clientes[pos].get_cuenta()
        if(gm.buscar_movimiento(cuenta)):
            print(f"cliente que no tuvo movimiento:{self.__lista_clientes[pos].get_apell()} {self.__lista_clientes[pos].get_nom()}")