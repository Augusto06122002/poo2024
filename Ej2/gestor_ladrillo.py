from clase_ladrillo import claseladrillo
from gestor_material import gestormaterial
import csv
class gestorLadrillo:
    __listaL:list
    def __init__(self):
        self.__listaL =[]
    def agregar(self,ladrillo):
        self.__listaL.append(ladrillo)
    def cargaL(self):
        band = True
        archivo = open('ladrillos.csv')
        reader = csv.reader(archivo,delimiter = ';')
        for fila in reader:
            if(band ==True):
                "encabezado"
                band = False
            else:
                unladrillo=claseladrillo(fila[0],fila[1],fila[2],fila[3])
                self.agregar(unladrillo)
        archivo.close()
    def asigna_materiales(self,GM):
        i = 0
        cont = 0
        while(i < len(self.__listaL) and cont <= 4):#A cinco ladrillos se le asigna 2 materiales
            self.__listaL[i].agregamaterial(GM.material())#Se le asigna el 1°material
            #self.__listaL[i].agregamaterial(GM.material())#Se le asigna el 2°material(Puede repetirse el material, pendiente buscar manera de que no se repita el indice del material )
            i+=1
            cont+=1
    def indice(self,id):
        i=0
        band=True
        result=-1
        while(i<len(self.__listaL) and band == True):
            if(self.__listaL[i].getid()==id):
                band= False
                result=i
            else:
                i+=1
        if(result != -1):
            return result
        else:
            print("EL identificador del ladrillo esta mal")
            
    def mostrar_datos(self):
        id=int(input("Ingrese el id del ladrillo"))
        pos=self.indice(id)
        self.__listaL[pos].mostrarcosto_y_caracteristica()
    def costo_fabricacion(self):
        costo=0
        for ladrillo in self.__listaL:
            costo = ladrillo.getc()+ladrillo.costo_adicional()
            if(costo !=ladrillo.getc()):
                print(f"El ladrillo {ladrillo} tiene un costo total de: {costo} (incluye costo del material asociado) ")
            else:
                print(f"El ladrillo {ladrillo} tiene un costo total de: {ladrillo.getc()} (No tiene materiales asociados)")
    def mostrar_detalle_asociado(self):
        print("ID               Material              Costo Asociado")
        for ladrillo in self.__listaL:

            band=ladrillo.verifica_existencia_material()
            if(band):
                for material in ladrillo.get_lista_material():
                    print(f"{ladrillo}                  {material.getmat()}                      {material.getcosto_adic()}")
            else:
                print(f'{ladrillo}               {'ninguno'}                   {0}')
                