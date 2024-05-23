from ClasaPublicacion import publicacion

class libro(publicacion):
    __nombreAutor:str
    __fechaEdicion:int
    __cantidadPaginas:int
    def __init__(self, titulo, categoria, precioBase,**kwargs):
        super().__init__(titulo, categoria, precioBase)# inicializa los atributos de la clase base
        self.__nombreAutor = kwargs['nombreAutor']
        self.__fechaEdicion = int(kwargs['fechaEdicion'])
        self.__cantidadPaginas = int(kwargs['cantpags'])
    def get_NombA(self):
        return self.__nombreAutor
    def get_fechaed(self):
        return self.__fechaEdicion
    def get_cantpag(self):
        return self.__cantidadPaginas
    def años_antiguedad(self):
        return 2024-self.__fechaEdicion
    def caracteristicas(self):# en este caso el precio de venta disminuye segun los años de antiguedad
        return (-1*((super().getPreciobase()*self.años_antiguedad())/100))
    def __str__(self):
        return f"nombre del autor {self.__nombreAutor} \n fecha de edicion: {self.__fechaEdicion} \n cantidad de paginas: {self.__cantidadPaginas}\n "