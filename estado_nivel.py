from re import T
import utilidades
import string


class EstadoNivel:
    # Constructor por defecto
    def __init__(self):
        self.uno = False
        self.dos = False
        self.tres = False
        self.cuatro = False
        self.cinco = False
        self.seis = False
        self.siete = False
        self.ocho = False
        self.nueve = False
    # Metodos
    # Actualizaz el estado del nivel

    def actualizar_nivel(self, dato):
        # Si el dato ingresado es 1 entonces se actualiza como logrado el 1.
        if dato == "1":
            self.uno = True
        # Si el dato ingresado es 1 entonces se actualiza como logrado el 2.
        elif dato == "2":
            self.dos = True
        # Si el dato ingresado es 1 entonces se actualiza como logrado el 3.
        elif dato == "3":
            self.tres = True
        elif dato == "4":
            self.cuatro = True
        elif dato == "5":
            self.cinco = True
        elif dato == "6":
            self.seis = True
        elif dato == "7":
            self.siete = True
        elif dato == "8":
            self.ocho = True
        elif dato == "9":
            self.nueve = True
    # Le permite al jugador ver el estado actual del nivel.
    def acceder_nivel(self):
        return [self.uno, self.dos, self.tres, self.cuatro, self.cinco,self.seis,self.siete, self.ocho,self.nueve]

