#testcajas.py
from CajaAhorro import caja_ahorro 
def crea_caja():
    print('ingese los siguiente datos:')
    nrocuenta = input('nrocuenta: ')
    cuil = input('cuil: ')
    apellido = input('apellidio: ')
    nombre = input('nombre')
    saldo = float(input('saldo :'))
    caja = caja_ahorro(nrocuenta,cuil,apellido,nombre,saldo)# caja instancia de la clase?

    return caja
def cargar_caja(lista):
    for i in range(3):
        caja=crea_caja()
        lista.append(caja)
    while True:
        for caja in lista:
            valor = int(input("""
    ---Solicite la operacion a realizar---
        1: Validar cuit
        2: Extraer saldo
        3: Depositar monto
        4: Mostrar el estado de la cuenta
        5: Para salir del sistema
        """))
            if(valor == 1):
                caja.validarCUIL()
            elif(valor == 2):    
                caja.extraer(100)
            elif(valor ==3):
                caja.depositar(1000)
            elif(valor == 4):
                caja.mostrardatos()
            else:
                break