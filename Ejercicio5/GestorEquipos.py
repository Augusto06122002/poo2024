import csv
from ClaseEquipo import ClaseEquipo
from GestorFecha import gestorfechas
class gestorEquipos:
    __lista_equipos:list
    def __init__(self):
        self.__lista_equipos=[]
    def agregar(self,unEquipo):
        self.__lista_equipos.append(unEquipo)
  
    def mostrardatos(self):
        print("---los datos son---. ")
        for i in range(len(self.__lista_equipos)):
            print(f"Nombre equipo :{self.__lista_equipos[i].getnombre()}")
            print(f"goles a favor: {self.__lista_equipos[i].getAfavor()}")
            print(f" Puntos: {self.__lista_equipos[i].getptos()}")
    def test_equipos(self):
        archivo= open(r"C:\Users\ventu\Documents\Facultad sisitema\Programacion orientada a objetos\UNIDAD 2\PracticaU2\Ejercicio5\equipos2024.csv")
        reader = csv.reader(archivo,delimiter=(','))
        band= True
        for fila in reader:
            if(band):
                "Evita el encabezado"
                band=False
            else:
                unEquipo=ClaseEquipo(int(fila[0]),fila[1],int(fila[2]),int(fila[3]),int(fila[4]),int(fila[5]))
                self.agregar(unEquipo)
        archivo.close()
    def listado_equipos(self,unaFecha): 
        i=0
        no_encontrado= True
        nomb = input("Ingrese el nombre del equipo")
        while (i < len(self.__lista_equipos) and no_encontrado):#Busca hasta encontrar el identificador del equipo ingresado
            if self.__lista_equipos[i].getnombre() == nomb:
                id = self.__lista_equipos[i].getid()
                print(f"Equipo: {self.__lista_equipos[i].getnombre():^20}")
                unaFecha.recorre_partidos(id)#Aca se va a recorrer todas las fechas y si jugo en alguna de las fechas se muestran los datos
                no_encontrado = False
            else:
                i+=1
        if(no_encontrado):
            print("Ingreso mal el equipo")
    def actualizar_equipos(self,gf):
        for i in range(len(self.__lista_equipos)):
            id = self.__lista_equipos[i].getid()
            if gf.participo_partido(id):
                self.__lista_equipos[i].setAfavor(self.__lista_equipos[i].getAfavor() + gf.obtenergolesF(id))
                self.__lista_equipos[i].set_en_contra(self.__lista_equipos[i].getContra() + gf.obtenergolesC(id))
                self.__lista_equipos[i].setdif(self.__lista_equipos[i].getdif()+(self.__lista_equipos[i].getAfavor()-self.__lista_equipos[i].getContra()))
                self.__lista_equipos[i].setptos(self.__lista_equipos[i].getptos()+gf.obtenerpuntos(id))
        print("Se actualizo la tabla de equipos")
    def ordenar_equipos(self):
        self.__lista_equipos=sorted(self.__lista_equipos,reverse=True)#sobrecarga __gt__ indica como se van a compara los objetos
    def muestra_equipos_ordenados(self):
         for i in range(len(self.__lista_equipos)):
            print(f"Nombre: {self.__lista_equipos[i].getnombre()} ")
            print(f"goles a favor: {self.__lista_equipos[i].getAfavor()} ")
            print(f"goles en contra: {self.__lista_equipos[i].getContra()} ")
            print(f"puntos: {self.__lista_equipos[i].getptos()} ")
    def carga_equipos_ordenados(self):
        ruta=r"C:\Users\ventu\Documents\Facultad sisitema\Programacion orientada a objetos\UNIDAD 2\PracticaU2\Ejercicio5\EquiposOrdenados.csv"
        with open(ruta,'w',newline='') as archivo: #with cierra el archivo
           writer=csv.writer(archivo)#crea un objeto writer que escribe en el archivo
           writer.writerow(['identificadordelequipo','nombredelequipo','golesafavor','golesencontra','diferenciadegoles','puntos'])#Es la primer linea pone el ecabezado
           for equipo in self.__lista_equipos:
               writer.writerow([equipo.getid(),equipo.getnombre(),equipo.getAfavor(),equipo.getContra(),equipo.getdif(),equipo.getptos()])
        print("Se realizo la carga...")