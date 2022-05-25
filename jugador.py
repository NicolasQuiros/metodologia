#Modulos descargados de internet
import pygame
#Modulos propios
import config
class Jugador:
    #Constructor por defecto
    def __init__(self,posicion_x,posicion_y,posicion_z):
        print("Jugador creado.")
        self.posicion = [posicion_x,posicion_y]
    def update(self):
        print("Jugador actualizado.")
    def render(self,pantalla):
        pygame.draw.rect(pantalla, #Dibujar al personaje en la pantalla
                        config.WHITE,#Color del personaje
                        (self.positions[0]*config.SCALE, #tamaños del personaje
                        self.positions[1]*config.SCALE,#tamaños del personaje
                        config.SCALE,#tamaños del personaje
                        config.SCALE),2)#tamaños del personaje
