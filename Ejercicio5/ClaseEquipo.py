"""De  cada  Equipo  se  registran:  identificador  del  equipo,  nombre  del  equipo,  goles  a  favor,  goles  en 
contra, diferencia de goles, y puntos"""
class ClaseEquipo:
    __id:str
    __nombre:str
    __golesF:int
    __golesC:int
    __difgoles:int
    __puntos:int
    def __init__(self,id,nomb,gf,gc,difg,pts):
        self.__id = id
        self.__nombre = nomb
        self.__golesF = gf
        self.__golesC = gc
        self.__difgoles = difg
        self.__puntos = pts
    def getnombre(self):
        return self.__nombre
    def getAfavor(self):
        return self.__golesF
    def getContra(self):
        return self.__golesC
    def getptos(self):
        return self.__puntos
    def getdif(self):
        return self.__difgoles
    def getid(self):
        return self.__id
    def setAfavor(self,result):
        self.__golesF =result
    def set_en_contra(self,result):
        self.__golesC=result
    def setdif(self,result):
        self.__difgoles=result
    def setptos(self,result):
        self.__puntos=result
    def __gt__(self,otro):
        if(self.__puntos == otro.__puntos):
            if(self.__difgoles == otro.__difgoles):
                return self.__golesF > otro.__golesF
            else:
                return self.__difgoles > otro.__difgoles
        else:
            return self.__puntos > otro.__puntos
                
            
        
    
    
