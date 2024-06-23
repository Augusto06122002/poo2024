from datetime import datetime
from ClaseJugador import jugador
class controladorJugadores:
    def __init__(self, repositorio, vista):
        self.repositorio = repositorio
        self.vista = vista
        self.jugador_actual = None

    def agregarJugador(self):#Al momento de iniciar el juego el jugador se agrega el jugador 
        nombre = self.vista.getNomb()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.jugador_actual = jugador(nombre, fecha)
        self.vista.iniciar_juego()
    def ActualizaPuntuacion_GameOver(self,puntaje):#Cada vez que el jugador pierda,Se va a actualizar su puntaje
        self.repositorio.ActualizarPuntaje(self.vista.getNomb(),puntaje)
    def guardarPuntajes(self):
        self.repositorio.grabarDatos()
        