import csv
import numpy as np
from ClaseMovimiento import movimiento
class gestormovimiento:
    __movimientos:np.ndarray
    __cantidad:int
    __dimension:int
    __incremento:int
    def __init__(self,cantidad=0,dimension=0,incremento=5):
        self.__cantidad=cantidad
        self.__dimension=dimension
        self.__incremento=incremento
        self.__movimientos=np.empty(cantidad,dtype=movimiento)
    def agregar(self,unmov): #corregido
        if(self.__cantidad==self.__dimension):
            self.__dimension+=self.__incremento
            self.__movimientos.resize(self.__dimension)# habia puesto self.__cantidad+=1 dentro del if...
        self.__movimientos[self.__cantidad]=unmov
        self.__cantidad+=1
    def carga_movimiento(self):
        band=True
        archivo=open(r"C:\Users\ventu\Documents\Facultad sisitema\Programacion orientada a objetos\UNIDAD 2\PracticaU2\PracticaOperativa(tema 2 2024)\MovimientosAbril2024.csv")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            if(band):
                "encabezado"
                band=False
            else:
                unmov=movimiento(int(fila[0]),fila[1],fila[2],fila[3],fila[4])
                self.agregar(unmov)
        archivo.close()
    def ordena_movimiento(self):# corregido 
        self.__movimientos = np.sort(self.__movimientos)#self.__movimientos.sort() no funcionaba
        
    def listado_movimiento(self,nr_cuenta):
        credito=0
        pago=0
        for i in range(self.__cantidad):
            print(f" {self.__movimientos[i]}") 
            if(self.__movimientos[i].getnr() == nr_cuenta):
              
                print(f"{self.__movimientos[i]}")
                if(self.__movimientos[i].get_tipo()=='C'):
                    credito+=self.__movimientos[i].get_imp()
                else:
                    pago+=self.__movimientos[i].get_imp()
        actualizado=credito-pago
        return actualizado    
    def buscar_movimiento(self,nr):
        band=True
        for i in range(self.__cantidad):
            if(self.__movimientos[i].getnr()==nr):
                band=False
        return band
                
        