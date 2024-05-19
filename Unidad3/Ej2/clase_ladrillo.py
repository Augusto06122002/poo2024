class claseladrillo:
    __Alto:int =7
    __largo:int =25
    __ancho:int = 15
    __cant:int 
    __id:int
    __kgporunidad:float
    __costo:float
    __lista_material:list
    def __init__(self,cant,id,kg,costo):
        self.__cant = int(cant)
        self.__id = int(id)
        self.__kgporunidad = float(kg)
        self.__costo = float(costo)
        self.__lista_material = []
        
    def agregamaterial(self,unmaterial):
        self.__lista_material.append(unmaterial)
    def getid(self):
        return self.__id
    def getc(self):
        return self.__costo
    def mostrarcosto_y_caracteristica(self):
        if(len(self.__lista_material)>0):
            for material in self.__lista_material:
                print(f"El ladrillo {self.__id} tiene un costo del material asociado de: {material.getcosto_adic()}$ cuyas caracteristicas son: {material.get_caracteristica()}")
        else:
            print(f"El ladrillo con id: {self.__id} no tiene materiales asociados")
    def costo_adicional(self):
        costo = 0
        if(len(self.__lista_material)>0): # el ladrillo tiene asociado el objeto material
        
            for m in self.__lista_material:
                costo+=m.getcosto_adic()
        return costo
    def __str__(self):
        return f"{self.__id}"
    def verifica_existencia_material(self):
        band=False
        if(len(self.__lista_material) > 0):
            band=True
        return band
    def get_lista_material(self):
        return self.__lista_material
    