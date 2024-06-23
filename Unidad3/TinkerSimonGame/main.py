
from RepositorioJugadores import repositorioJugadores

from VistaPrincipal import JuegoSimon
from ControladorJugadores import controladorJugadores
from ObjectEncoder import ObjectEncoder
def main():
    conn=ObjectEncoder('pysimonpuntajes.json')
    repositorio=repositorioJugadores(conn)
    vista=JuegoSimon()
    ctrl=controladorJugadores(repositorio, vista)
    vista.setControlador(ctrl)
    vista.root.mainloop()  
if __name__ == "__main__":
    main()