class movimiento:
    __numero_cuenta:int
    __fecha:str
    __descripcion:str
    __tipo_movimiento:str
    __importe:int
    def __init__(self,nc,fh,d,tipo,imp):
        self.__numero_cuenta = int(nc)
        self.__fecha = fh
        self.__descripcion = d
        self.__tipo_movimiento = tipo
        self.__importe = int(imp)
    def __lt__(self,other):
        #print(f"{self.__numero_cuenta} < {other.__numero_cuenta}")
        return self.__numero_cuenta < other.__numero_cuenta
    def getnr(self):
        return self.__numero_cuenta
    def get_tipo(self):
        return self.__tipo_movimiento
    def get_imp(self):
        return self.__importe
    def __str__(self):
        return f"|{self.__fecha}|{self.__descripcion}|{self.__importe}|{self.__tipo_movimiento}"# agregue tipo movimiento