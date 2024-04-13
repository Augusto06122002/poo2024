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
    for i in range(2):
        caja=crea_caja()
        lista.append(caja)
        caja.extraer(100)
        caja.depositar(1000)
        caja.validarCUIL()
        caja.mostrardatos()