
from RepositorioJugadores import repositorioJugadores

from VistaPrincipal import JuegoSimon
from ControladorJugadores import controladorJugadores
from ObjectEncoder import ObjectEncoder
from ClaseJugador import jugador
def main():
    vista=JuegoSimon()
    conn=ObjectEncoder('pysimonpuntajes.json')
    repositorio=repositorioJugadores(conn)
    
    ctrl=controladorJugadores(repositorio, vista)
    vista.setControlador(ctrl)
 
    
if __name__ == "__main__":
    main()