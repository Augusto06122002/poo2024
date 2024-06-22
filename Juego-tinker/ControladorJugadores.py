
class controladorJugadores:
    def __init__(self,vista,repo):
        self.vista = vista
        self.repo = repo
    def start(self):
        for jugador in self.repo.getListaManejador():
            self.vista.AgregarJugador(jugador)
        self.vista.mainloop()
    def SalirGrabarDatos(self):
        self.repo.grabarDatos()
        