
class publicacion:
    __titulo:str
    __categoria:str
    __precioBase:float
    def __init__(self,titulo,categoria,precioBase):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precioBase = precioBase
    def getTitulo(self):
        return self.__titulo
    def getCateg(self):
        return self.__categoria
    def getPreciobase(self):
        return self.__precioBase
    def caracteristicas(self):
        pass
    def importe_venta(self):
        return round(self.__precioBase + self.caracteristicas(),2)
    def mostrar_publicaciones(self):
        print(f" Titulo: {self.__titulo} \n categoria: {self.__categoria}\n importe de venta: {self.importe_venta()}")
        