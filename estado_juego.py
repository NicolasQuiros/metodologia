# Esta libreria permite usar enums en python como en C++.
from enum import Enum
# Estos son los estados que puede tener el juego


class EstadoJuego(Enum):
    NULO = 0,
    CORRIENDO = 1,
    TERMINADO = 2
