#Clase nodo
class Profesor:
    pass
class Nodo:
    __profesor: Profesor 
    __siguiente: object 
    def __init__(self, profesor):
        self.__profesor=profesor
        self.__siguiente=None
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__profesor
#Clase lista
class Lista:
    __comienzo: Nodo
    def __init__(self):
        self.__comienzo=None
    def agregarProfesor(self, profesor):
        nodo = Nodo(profesor)# se crea un objeto nodo con el objeto que quiero agregar
        nodo.setSiguiente(self.__comienzo)# Se pasa el objecto al cual apunta el comienzo
        self.__comienzo=nodo# se acutaliza el comienzo con el nuevo nodo agregado
    def listarDatosProfesores(self):
        aux = self.__comienzo# se guarda la cabeza
        while aux!=None:
            print(aux.getDato())# dato que tiene el nodo
            aux=aux.getSiguiente()# direccion del nodo al que apunto el nodo posicionado
    def eliminarPorDNI(self, dni):
        aux=self.__comienzo
        encontrado = False
        if aux.getDato().getDNI()==dni: # si el dni es el primero de la lista
            encontrado=True
            print('Encontrado:'+str(aux.getDato()))
            self.__comienzo = aux.getSiguiente() # el comienzo entonces sera el nodo siguiente 
            del aux # elimina el nodo
        else:
            ant = aux #nodo anterior
            aux = aux.getSiguiente() # nodo siguiente
        while not encontrado and aux != None:
            if aux.getDato().getDNI()==dni:
                encontrado=True
            else:
                ant = aux
                aux=aux.getSiguiente()
            if encontrado:
                print('Encontrado:'+str(aux.getDato()))
                ant.setSiguiente(aux.getSiguiente())# se modfica la cabeza
                del aux # se elimina el nodo que contenia el dato de interes
            else:
                print('El DNI {}, no está en la lista'.format(dni))
#Cómo hacer para que la lista responda al código siguiente???
#for dato in lista:
#print('Datos del',dato)
"""""Para que la clase Lista definida anteriormente, o cualquier otra clase definida por el programador, seaiterable, la clase debe proveer los métodos:
__iter__(self), que devuelve un iterador de Python, en general se deja que devuelva el iterador deobject
__next__(self), que devuelve el siguiente elemento de la secuencia, y cuando no hay más elementoslanza la excepción StopIteration
En el caso de la clase Lista, se deberán agregar tres nuevos atributos:
__actual: para saber cual es el elemento actual, y poder devolverlo al iterar.
__index: lleva la cuenta de los pasos de iteración, se actualiza en uno para pasar el siguienteelemento.
__tope: lleva la cuenta total de elementos de la lista, se actualiza sumando uno cuando se agreganelementos a la lista, y se decrementa cuando se eliminan elementos de la lista."""
class Lista:
    __comienzo: Nodo # simepre apunta al primer nodo
    __actual: Nodo #apunta al nodo actual
    __indice: int# para manejar la posicion
    __tope: int # para la cantidad de nodos
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__tope=0
    def __iter__(self): #retorna el propio objeto
        return self
    def __next__(self):# rtorna el nodo siguiente
        if self.__indice==self.__tope: # si el indice actual esta en el ultimo nodo entonces setea el indice en 0 y actual vuelve al principio
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration #indica que ya recorri toda la lista
        else: #va reecorriendo la lista
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()#lo acutaliza con el siguiente nodo
            return dato
    def agregarProfesor(self, profesor):
            nodo = Nodo(profesor)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=nodo
            self.__tope+=1
    def eliminarPorDNI(self, dni):
        aux=self.__comienzo
        encontrado = False
        if aux.getDato().getDNI()==dni:
            encontrado=True
            print('Encontrado y eliminado:\n'+str(aux.getDato()))
            self.__comienzo = aux.getSiguiente()
            self.__tope-=1#las unicas modificaciones
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
        while not encontrado and aux != None:
            if aux.getDato().getDNI()==dni:
                encontrado=True
            else:
                ant = aux
                aux=aux.getSiguiente()
            if encontrado:
                print('Encontrado y eliminado:\n'+str(aux.getDato()))
                ant.setSiguiente(aux.getSiguiente())
                self.__tope-=1# las unicas modificaciones
                del aux
            else:
                print('El DNI {}, no está en la lista'.format(dni))
#for dato in lista: next retorna el dato
# print('datos del':dato)    
