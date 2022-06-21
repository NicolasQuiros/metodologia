from enum import Enum #Esta libreria permite usar enums en python como en C++.
#Estos son los estados que puede tener el juego
class EstadoJuego(Enum):
    NULO = 0,
    CORRIENDO = 1,
    TERMINADO = 2