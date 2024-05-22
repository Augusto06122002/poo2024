import csv
 
from claseEdificio import edificio
from claseDepartamento import departamento
class gestor_edificio:
    __lista_edificios:list
    def __init__ (self):
        self.__lista_edificios = []
    def agregar(self,un_edificio):
        self.__lista_edificios.append(un_edificio)
    def carga_edificios(self):
        
        archivo=open('EdificioNorte.csv')
        reader=csv.reader(archivo,delimiter=';')
        aux=0
        for fila in reader:
            if (aux != fila[0]):#controla la logica entre el id de los edificios
                un_edificio=edificio(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.agregar(un_edificio)
                aux=fila[0]
            else:
                undepto = departamento(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
                un_edificio.agregar_dpto(undepto)
        archivo.close()
    def mostrar_datos_edificios(self):
        for ed in self.__lista_edificios:
            print("--------Edificio--------")
            print(ed)
            print("--------Departamentos------")
            for dpto in ed.getlista():
                print(dpto)
    def busca_edificio(self,nomb):
        i=0
        band=False
        pos =-1
        while(i<len(self.__lista_edificios) and band!=True):
            if(self.__lista_edificios[i].getnomb() == nomb):
                band= True
                pos=i
            else:
                i+=1
        assert band == True,"El edificio no fue encontrado." #Si es igual se detiene la ejecucion y se trata la excepcion en el main
        return pos
    def mostrar_propietario(self,nomb):
        pos=self.busca_edificio(nomb)
        for dpto in self.__lista_edificios[pos].getlista():
            print (dpto)
            
    def superficie_total(self,nomb):
        pos=self.busca_edificio(nomb)
        acum=0
        for dpto in self.__lista_edificios[pos].getlista():
            acum+=dpto.getsup()
        print(f"El edificio {nomb} tiene una superficie total de: {acum} m3")
    
    def calculo_supericie(self,nomb):
        band=False
        for edificio in range(len(self.__lista_edificios)):
            acum_sup_dpto=0
            acum_sup_ed=0
            for dpto in self.__lista_edificios[edificio].getlista():
                if(dpto.getnomP() == nomb):
                    band=True
                    acum_sup_dpto+=dpto.getsup()
                else:
                    "No es el propietario"
            if(band == True):
                for dpto in self.__lista_edificios[edificio].getlista():
                    acum_sup_ed+=dpto.getsup()
                total=round(((acum_sup_dpto*100)/acum_sup_ed),2)
                print(f"En el edificio :{self.__lista_edificios[edificio].getnomb()}")
                print(f"El propietario {nomb} con una superficie total cubierta de su departamento/s de:{acum_sup_dpto} m2 y representa el {total} % de la superficie total del edificio  ")
                band=False
            else:
                "No tiene ninguno dpto en el edificio"
    def cantidad_dptos_piso(self,piso):
        
        for ed in range(len(self.__lista_edificios)):
            if(self.__lista_edificios[ed].get_pisos() >= piso):
                i=0
                band = True
                cont=0
                departamentos=self.__lista_edificios[ed].getlista()
                while(i < len(departamentos) and band == True):
                    if(departamentos[i].get_npiso() <= piso): # es para controlar que no se pase de nro de piso
                        if(departamentos[i].get_npiso() == piso):
                            if(departamentos[i].get_habitacion() == 3 and departamentos[i].get_baño() > 1):
                                cont+=1
                                #print(f"El dpto: {departamentos[i].getid()} cumple la condicion(3 hab y mas de 1 baño)")
                        else:
                            "No es el nro de piso"
                    else:
                        "Se recorrieron todos los departamentos del nro de piso buscado"
                        "Ademas controla que no se analize departamentos de pisos superiores"
                        band=False
                    i+=1
                print(f"---La cantidad de departamentos que cumplen con la condicion (3H y +1B) son: {cont} departamentos del edificio: {self.__lista_edificios[ed].getnomb()}---")
            else:
                print(f"El nro de piso {piso} no existe para el edificio {self.__lista_edificios[ed].getnomb()}")
                        
                        
                        
                    
        
        
                
                
            
    
    
        
     