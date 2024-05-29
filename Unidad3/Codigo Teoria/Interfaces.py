"-----------------------------Interfaces----------------------------"
#Permiten definir metodos(lo mas comun) son por defecto publicos,atributos o propiedades(pero no son comunes)
#Las clases van a implementar el codigo de los metodos que las interfaces tengan definidas
#La herencia multiple en lenguajes que no lo soporta se simula utilizando interfaces
#No pueden crearse objetos directamente de ellas
#En poo se dice que las interfaces son funcionalidades(comportamientos)
# La libreria que se usara para mostrar el uso de las interfaces como forma de restriccion de metodos, es la libreria Zope
#Hay que importar la libreria Zope
#Buena practica que el nombre de la interfaz empiece con I

from zope.interface import Interface
from zope.interface import implementer
'''Declaración de interface ICajero
El Cajero solo puede buscar productos por descripción
el método declarado es
buscarProductoPorDescripcion(descripcion)
'''
class ICajero(Interface):# Se dice que es una interfaz
    def buscarProductoPorDescripcion(descripcion):# firma del metodo
        pass
    '''Declaración de interface ISupervisor
    El Supervisor modificar el precio de un producto, que busca por código
    Los métodos que declara la intereface es
    buscarProductoPorCodigo(codigo)
    modificarPrecioProducto(codigo, precio)
    '''
class ISupervisor(Interface):
    def buscarProductoPorCodigo(codigo):
            pass
    def modificarPrecioProducto(codigo, precio):
            pass
class Producto(object):
    __codigo: int
    __descripcion: str
    __precio: float
    def __init__(self, codigo, descripcion, precio):
        self.__codigo=codigo
        self.__descripcion=descripcion
        self.__precio=precio
    def __str__(self):
        cadena = 'Codigo Descripcion Precio \n'
        cadena += '{0:6d} {1:15s} {2:6.2f}'.format(self.__codigo, self.__descripcion,self.__precio)
        return cadena
    def getDescripcion(self):
        return self.__descripcion
    def getCodigo(self):
        return self.__codigo
    def modificarPrecio(self, precio):
        self.__precio=precio
"---------------------Aca esta la clase que implementa las interfeces anteriormente definidas-------"
@implementer(ICajero)
@implementer(ISupervisor)
class ManejadorProductos:#Es la clase que implementa las interfaces se indica con los decoradores de arriba
    __productos: list
    def __init__(self):
        self.__productos=[]
    def agregarProducto(self, producto):
        self.__productos.append(producto)
    '''Método de la interface ICajero'''
    def buscarProductoPorDescripcion(self, descripcion):#
        i=0
        bandera=False
        retorno=None
        while not bandera and i<len(self.__productos):
            unProducto=self.__productos[i]
        if unProducto.getDescripcion()==descripcion:
            bandera=True
        else:
            i+=1
        if bandera:
            retorno = self.__productos[i]
        return retorno       

    def buscarProductoPorCodigo(self, codigo):
        i=0
        bandera=False
        retorno=None
        while not bandera and i<len(self.__productos):unProducto=self.__productos[i]
        if unProducto.getCodigo()==codigo:
            bandera=True
        else:
            i+=1
        if bandera:
            retorno = self.__productos[i]
        return retorno
    def modificarPrecio(self, codigo, precio):
        producto = self.buscarProductoPorCodigo(codigo)
        if producto == None:
            print('Producto código {}, no encontrado'.format(codigo))
        else:
            producto.modificarPrecio(precio)
    def cajero(manejarVendedor: ICajero):
        descripcion=input('Descripcion de producto a buscar: ')
        producto = manejarVendedor.buscarProductoPorDescripcion(descripcion)
        if producto == None:
            print('Producto {}, no encontrado'.format(descripcion))
        else:
            print(producto)
    def supervisor(manejarSupervisor: ISupervisor):
        codigo=int(input('Código del producto a cambiar precio: '))
        producto = manejarSupervisor.buscarProductoPorCodigo(codigo)
        if producto == None:
            print('No hay un Producto con código {}'.format(codigo))
        else:
            print(producto)
            precio=float(input('Nuevo precio: '))
            manejarSupervisor.modificarPrecio(codigo, precio)
            print(producto)
    def testInterfaces():
            manejadorProductos = ManejadorProductos()
            unProducto=Producto(1,'Arroz 1kg',52)
            manejadorProductos.agregarProducto(unProducto)
            unProducto=Producto(2,'Yerba 1/2kg',120)
            manejadorProductos.agregarProducto(unProducto)
            usuario=input('Usuario (Admin/Cajero): ')
            clave=input('Clave:')
            if usuario.lower() == 'Admin'.lower() and clave =='a54321':
                "Testeando cajero"
                #supervisor(ISupervisor(manejadorProductos))# el objeto manejador productos es de tipo Isupervisor
            else:
                if usuario.lower() == 'Cajero'.lower() and clave == 'c12345':
                    '''testeado cajero'''
                    #cajero(ICajero(manejadorProductos))#es uncast, ahora es una instancia de icajero
    if __name__=='__main__':
        testInterfaces()