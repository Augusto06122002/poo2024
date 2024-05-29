from collections import defaultdict
class ListaEstadistica(list):
    def mediaAritmetica(self):
        return sum(self) / len(self)
    def mediana(self):
        retorno=0.0
        if len(self) % 2:
            retorno = self[int(len(self) / 2)]
        else:
            idx = int(len(self) / 2)
            retorno = (self[idx] + self[idx-1]) / 2
        return retorno
    def moda(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1
            moda_freq = max(freqs.values())
            modas = []
        for item, valor in freqs.items():
            if valor == moda_freq:
                modas.append(item)
        return modas
#deberio ir en otro modulo
import unittest
class TestValidInputs(unittest.TestCase):
    __listaEstadistica: list
    def setUp(self):# inicializa el atributo lista
        self.__listaEstadistica = ListaEstadistica([1,2,2,3,3,4])
    def test_media(self):
        self.assertEqual(self.__listaEstadistica.mediaAritmetica(),2.5)
    def test_mediana(self):
        self.assertEqual(self.__listaEstadistica.mediana(), 2.5)    
        self.__listaEstadistica.append(4)
        self.assertEqual(self.__listaEstadistica.mediana(), 3)
    def test_moda(self):
        self.assertEqual(self.__listaEstadistica.moda(), [2,3])
        self.__listaEstadistica.remove(2)
        self.assertEqual(self.__listaEstadistica.moda(), [3])
if __name__=='__main__':
    unittest.main()
# Hace que se ejecuten todos los metodos test, media, moda y mediana, todos usaran cada lista inicializada por setup() se inicializa tantas veces como test existan
"""""Diseñar el método setUp que crea la lista y agrega elementos• Diseñar los test para: 
 Verificar que agregó elementos a la lista. 
 Verificar que la lista no está vacía 
 Eliminar un elemento intermedio de la lista, 
 verificar que lo eliminó. 
 Eliminar el primer elemento, verificar que lo eliminó. 
Eliminar último elemento de la lista, verificar que lo eliminó. 
 Vaciar la lista, verificar que está vacía.
"""