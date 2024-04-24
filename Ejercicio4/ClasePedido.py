class ClasePedido:
    __patente_asignada:str
    __identificador:int
    __comidas_pedidas:str
    __tiempo_estimado:int
    __tiempo_real:int
    __precio:int

    def __init__(self,pt,id,cp,te,pr,tr=0):
        self.__patente_asignada = pt
        self.__identificador = id
        self.__comidas_pedidas= cp
        self.__tiempo_estimado = te
        self.__tiempo_real = tr
        self.__precio = pr
    def obtener_Tr(self):
        return self.__tiempo_real
    def obtener_Patente_Asignada(self):
        return self.__patente_asignada
    def obtener_tiempoReal(self):
        return self.__tiempo_real

