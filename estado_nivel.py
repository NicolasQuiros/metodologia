
from ast import If
import string


class EstadoNivel:
    # Constructor por defecto
    def __init__(self):
        self.uno = False
        self.dos = False
        self.tres = False
    # Metodos
    # Actualizaz el estado del nivel

    def actualizar_nivel(self, dato):
        # Si el dato ingresado es 1 entonces se actualiza como logrado el 1.
        if dato == "1":
            # print(self.uno)
            self.uno = True
            # print(self.uno)
        # Si el dato ingresado es 1 entonces se actualiza como logrado el 2.
        elif dato == "2":
            # print(self.dos)
            self.dos = True
            # print(self.dos)
        # Si el dato ingresado es 1 entonces se actualiza como logrado el 3.
        elif dato == "3":
            # print(self.tres)
            self.tres = True
            # print(self.tres)
    # Le permite al jugador ver el estado actual del nivel.

    def ver_estado_nivel(self):
        print("uno ", self.uno)
        print("dos ", self.dos)
        print("tres ", self.tres)
