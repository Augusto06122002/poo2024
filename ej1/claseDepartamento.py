class departamento:
    __id:int
    __propietario:str
    __nro_piso:int
    __nro_dpto:int
    __chabitacion:int
    __cbanos:int
    __superficie:float
    def __init__(self,id,nombP,nroPiso,nroDepto,cHab,cBan,sup):
        self.__id = int(id)
        self.__propietario = nombP
        self.__nro_piso = int(nroPiso)
        self.__nro_dpto = int(nroDepto)
        self.__chabitacion = int(cHab)
        self.__cbanos = int(cBan)
        self.__superficie = float(sup)
    def __str__(self):
        return f"idDepartamento {self.__id} \n nombrePropietario: {self.__propietario} \n nro_piso: {self.__nro_piso} \n nro_dpto: {self.__nro_dpto} \n cantidad_habitaciones: {self.__chabitacion} \n nro_baños: {self.__cbanos} \n superficie: {self.__superficie} m3 \n"
    def getid(self):
        return self.__id
    def getnomP(self):
        return self.__propietario
    def getsup(self):
        return self.__superficie
    def get_npiso(self):
        return self.__nro_piso
    def get_habitacion(self):
        return self.__chabitacion
    def get_baño(self):
        return self.__cbanos