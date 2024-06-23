from datetime import datetime
from ClaseJugador import jugador
class controladorJugadores:
    def __init__(self, repositorio, vista):
        self.repositorio = repositorio
        self.vista = vista
    def agregarJugador(self):#Al momento de iniciar el juego el jugador se agrega el jugador 
        nombre = self.vista.getNomb()
        fecha = datetime.now()
        formato = "%Y-%m-%d %H:%M:%S"
        fecha_formateada = fecha.strftime(formato)
        print(fecha_formateada)
        jugador_actual = jugador(nombre, fecha_formateada)
        self.repositorio.agregarJugador(jugador_actual)
        self.vista.ComienzaJuego()
    def ActualizaPuntuacion_GameOver(self,puntaje):#Cada vez que el jugador pierda,Se va a actualizar su puntaje
        self.repositorio.actualizarPuntaje(puntaje,self.vista.getNomb())
    def guardarPuntajes(self):
        self.repositorio.grabarDatos()
    def getListaPuntajesOrdenados(self):
        self.repositorio.getListaPuntajesOrdenados()
    def getListaManejador(self):
        return self.repositorio.getListaManejador()
        