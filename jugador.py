# Modulos descargados de internet
import pygame
# Modulos propios
import config


class Jugador:
    # Constructor por defecto
    def __init__(self, posicion_x, posicion_y):
        print("Jugador creado.")
        # Creamos al jugador en su posicion inicial
        self.posicion = [posicion_x, posicion_y]
        self.imagen = pygame.image.load("imagenes/princesa_frente.png")

        self.imagen = pygame.transform.scale(self.imagen,(config.ESCALA, config.ESCALA))
        self.rectangulo = pygame.Rect(self.posicion[0] * config.ESCALA, self.posicion[1] * config.ESCALA, config.ESCALA, config.ESCALA)


    def actualizar(self):
        print("Jugador actualizado.")

    def actualizarPosicion(self,nueva_posicion): #nueva_posicion es una tupla
        #Actualizamos la posicion sumandole los cambios hechos en la dimension x e y.
        self.posicion[0] = nueva_posicion[0]
        self.posicion[1] = nueva_posicion[1]
        

    def render(self, pantalla, camara):
        self.rectangulo = pygame.Rect(self.posicion[0] * config.ESCALA, self.posicion[1] * config.ESCALA - (camara[1] * config.ESCALA) , config.ESCALA , config.ESCALA)
        pantalla.blit(self.imagen, self.rectangulo)