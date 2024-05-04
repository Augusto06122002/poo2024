class cliente:
    __nombre:str
    __apellido:str
    __dni:int
    __numero_cuenta:int
    __saldo_anterior:int
    def __init__(self,nomb,ape,dni,nc,sa):
        self.__nombre=nomb
        self.__apellido=ape
        self.__dni = int(dni)
        self.__numero_cuenta= int(nc)
        self.__saldo_anterior=int(sa)
    def getdni(self):
        return self.__dni
    def get_cuenta(self):
        return self.__numero_cuenta
    def get_apell(self):
        return self.__apellido
    def get_nom(self):
        return self.__nombre
    def get_saldo(self):
        return self.__saldo_anterior
    def actualiza_saldo(self,saldo):
        self.__saldo_anterior = saldo