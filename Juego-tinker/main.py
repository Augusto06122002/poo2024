
from RepositorioJugadores import repositorioJugadores

from vista import VistaSimon
from ControladorJugadores import controladorJugadores
from ObjectEncoder import ObjectEncoder
def main():
    vista=VistaSimon()
    conn=ObjectEncoder('pysimonpuntajes.json')
    repositorio=repositorioJugadores(conn)
    
    ctrl=controladorJugadores(repositorio, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
    
if __name__ == "__main__":
    main()