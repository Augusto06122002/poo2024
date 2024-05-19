from clase_material import material
import csv
import random
class gestormaterial:
    __listaM:list
    def __init__(self):
        self.__listaM =[]
    def agregar(self,material):
        self.__listaM.append(material)
    def cargaM(self):
        band = True
        archivo = open('materiales.csv')
        reader = csv.reader(archivo,delimiter = ';')
        for fila in reader:
            if(band ==True):
                "encabezado"
                band = False
            else:
                unmaterial=material(fila[0],fila[1],fila[2],fila[3])
                self.agregar(unmaterial)
        archivo.close()
    def material(self):
        i=random.choice(range(len(self.__listaM)))
        return self.__listaM[i]
