import csv
from ClaseFechaFutbol import fechafutbol

class gestorfechas:
    __lista_fechas:list
    def __init__(self):
        self.__lista_fechas=[]
    def agregar(self,unafecha):
        self.__lista_fechas.append(unafecha)
    def test_fechas(self):
        archivo= open(r"C:\Users\ventu\Documents\Facultad sisitema\Programacion orientada a objetos\UNIDAD 2\PracticaU2\Ejercicio5\fechasFutbol.csv")
        reader = csv.reader(archivo,delimiter=(','))
        band = True
        for fila in reader:
            if(band):
                "Evita el encabezado"
                band=False
            else:
                unaFecha=fechafutbol(fila[0],int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4]))
                self.agregar(unaFecha)
        archivo.close()
    def evalua_puntos(self,diferencia):
        if(diferencia > 0):
            puntos=3#Gano el partido
        elif(diferencia < 0):
            puntos=0 #perdio el partido
        elif(diferencia == 0):
            puntos=1 #empato el partido
        return puntos
   
    def recorre_partidos(self,id):
        print("Fecha          Goles a favor       Goles en contra    Diferencia de goles    Puntos")
        sumF=0
        sumC=0
        sumP=0
        for i in range(len(self.__lista_fechas)):
            if(self.__lista_fechas[i].getidL() == id):
                diferencia = self.__lista_fechas[i].get_GolL() - self.__lista_fechas[i].get_GolV()
                puntos = self.evalua_puntos(diferencia)
                sumF+=self.__lista_fechas[i].get_GolL()
                sumC+=self.__lista_fechas[i].get_GolV()
                sumP+=puntos
                print(f"{self.__lista_fechas[i].getfecha():<12}{self.__lista_fechas[i].get_GolL():>10} {self.__lista_fechas[i].get_GolV():>21} {diferencia:>22} {puntos:>12} ")
            elif self.__lista_fechas[i].getidV() == id:
                diferencia = self.__lista_fechas[i].get_GolV() - self.__lista_fechas[i].get_GolL()
                puntos=self.evalua_puntos(diferencia)
                print(f"{self.__lista_fechas[i].getfecha():<12}{self.__lista_fechas[i].get_GolV():>10} {self.__lista_fechas[i].get_GolL():>21} {diferencia:>22} {puntos:>12} ")
                sumF+=self.__lista_fechas[i].get_GolV()
                sumC+=self.__lista_fechas[i].get_GolL()
                sumP+=puntos
        print("----------------------------------------------------------------------------------------")
        print(f"Total:{sumF:>16}{sumC:>22}{sumF-sumC:>23}{sumP:>13}")
    def participo_partido(self,id):
        no_encontrado = True
        i=0
        while(i<len(self.__lista_fechas)and no_encontrado):
            if(self.__lista_fechas[i].getidL()==id or self.__lista_fechas[i].getidV()==id):
                no_encontrado=False
            else:
                i+=1
        if(no_encontrado):
            print("El equipo no participo")
            band=False
        else:
            band=True
        return band 
    def obtenergolesF(self,id):
        i=0
        sumF=0
        for i in range(len(self.__lista_fechas)):
            if self.__lista_fechas[i].getidL() == id:
                sumF+=self.__lista_fechas[i].get_GolL()
            elif self.__lista_fechas[i].getidV() == id:
                sumF+=self.__lista_fechas[i].get_GolV()
        return sumF
    def obtenergolesC(self,id):
        i=0
        sumC=0
        for i in range(len(self.__lista_fechas)):
            if self.__lista_fechas[i].getidL() == id:
                sumC+=self.__lista_fechas[i].get_GolV()
            elif self.__lista_fechas[i].getidV() == id:
                sumC+=self.__lista_fechas[i].get_GolL()
        return sumC
    def obtenerpuntos(self,id):
        sumP=0
        for i in range(len(self.__lista_fechas)):
            if(self.__lista_fechas[i].getidL() == id):
                diferencia = self.__lista_fechas[i].get_GolL() - self.__lista_fechas[i].get_GolV()
                puntos = self.evalua_puntos(diferencia)
                sumP+=puntos
            elif self.__lista_fechas[i].getidV() == id:
                diferencia = self.__lista_fechas[i].get_GolV() - self.__lista_fechas[i].get_GolL()
                puntos=self.evalua_puntos(diferencia)
                sumP+=puntos
        return sumP
   