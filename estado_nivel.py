
from ast import If
import string


class EstadoNivel:
    def __init__(self):
        self.uno=False
        self.dos=False
        self.tres=False
    
    def actualizar_nivel(self, data):
        if data == "1":
            #print(self.uno)
            self.uno = True
            #print(self.uno)
        elif data == "2":
            #print(self.dos)
            self.dos = True
            #print(self.dos)
        elif data == "3":
            #print(self.tres)
            self.tres = True
            #print(self.tres)

    def ver_estado_nivel(self):
        print("uno ",self.uno)
        print("dos ",self.dos)
        print("tres ",self.tres)

