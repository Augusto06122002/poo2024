from ClasaPublicacion import publicacion

class cd(publicacion):
    __tiempoReproduccion:int
    __nombre_narrador:str
    def __init__(self, titulo, categoria, precioBase,**kwargs):
        super().__init__(titulo, categoria, precioBase)# inicializa los atributos de la clase base
        self.__tiempoReproduccion = int(kwargs['tiempo'])
        self.__nombre_narrador = kwargs['nomb']
    def get_tr(self):
        return self.__tiempoReproduccion
    def get_nomb(self):
        return self.__nombre_narrador
    def caracteristicas(self):#En este caso el precio de venta se aumenta en un 10%
        return (super().getPreciobase()*10)/100
    def __str__(self):
        return f"Tiempo de reproduccion: {self.__tiempoReproduccion}\n nombre del narrador: {self.__nombre_narrador}\n "