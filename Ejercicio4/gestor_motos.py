
import csv
from ClaseMoto import ClaseMoto
class gestor_motos:
    __ListaMotos:list
    def __init__(self):
        self.__ListaMotos = []
    def carga(self,unaMoto):
        self.__ListaMotos.append(unaMoto)
    
    def test(self):
        archivo = open(r'C:\Users\titom\Documents\POO\Unidad2\codigo\Ejercicio4\datosMotos.csv')
        reader = csv.reader(archivo)
        band = True
        for fila in reader:
            if band:
                "Encabezado"
                band = not band
            else:
                patente = fila[0]
                marca  = fila[1]
                conductor  = fila[2]
                kilometro = fila[3]
                unaMoto=ClaseMoto(patente,marca,conductor,kilometro)
                self.carga(unaMoto)
    def valida_moto(self,patente):
        band = True
        result = None
        i=0
        while(len(self.__ListaMotos)>i and band):
            if(self.__ListaMotos[i].obtenterPatente()==patente):
                band = False
                result = i
            else:
                i=i+1
        return result
    def muestra_conductor(self,p):
        i=self.valida_moto(p)
        if(i!=None):
            print(f" los datos del coductor son: {self.__ListaMotos[i].obtenerNyA}")
        return i


            
        