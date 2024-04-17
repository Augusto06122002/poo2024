import re
class caja_ahorro:
    __nrocuenta: str 
    __cuil:str
    __apellido:str
    __saldo:float   
    __nombre:str
    def __init__(self,nrocuenta,cuil,nombre,apellido,saldo):
        self.__nrocuenta = nrocuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__saldo = saldo
        self.__nombre = nombre
    def mostrardatos(self):
        print(f'numero de cuenta:  {self.__nrocuenta}')
        print(f'cuil: {self.__cuil}')
        print(f'apellido: {self.__apellido}')
        print(f'nombre : {self.__nombre}')
        print(f'saldo: {self.__saldo}')
    def extraer(self,importe):
        if self.__saldo >importe:
            self.__saldo -= importe
            print(f'saldo total con la extraccion:$ {self.__saldo}')
        else:
            return -1
    def depositar(self,valorD):
        if valorD > 0:
            self.__saldo += valorD
        else:
            print('ingrese un numero positivo: ')
    def validarCUIL(self):
        pattern = r'^\d{2}-\d{8}-\d$'
        if re.match(pattern, self.__cuil):#re.match(evalua si el cuil ingresado cumple el patron que deberia tener XY – 12345678 – Z)coinciden=true
            print("CUIL válido.")
            return True
        else:
            print("CUIL inválido.")
            return False
        