#Modulos descargados de internet
import pygame
#Modulos propios
import config
class Jugador:
    #Constructor por defecto
    def __init__(self,posicion_x,posicion_y):
        print("Jugador creado.")
        #Creamos al jugador en su posicion inicial
        self.posicion = [posicion_x,posicion_y]
        self.imagen = pygame.image.load("imagenes/princesa_frente.png")
        self.imagen = pygame.transform.scale(self.imagen,(config.ESCALA, config.ESCALA))
        self.rectangulo = pygame.Rect(self.posicion[0] * config.ESCALA, self.posicion[1] * config.ESCALA, config.ESCALA, config.ESCALA)
    def actualizar(self):
        print("Jugador actualizado.")
    def actualizarPosicion(self,x_cambio,y_cambio):
        #Actualizamos la posicion sumandole los cambios hechos en la dimension x e y.
        self.posicion[0] += x_cambio
        self.posicion[1] += y_cambio
        self.rectangulo = pygame.Rect(self.posicion[0] * config.ESCALA, self.posicion[1] * config.ESCALA, config.ESCALA, config.ESCALA)

    def render(self,pantalla):
        pantalla.blit(self.imagen,self.rectangulo)