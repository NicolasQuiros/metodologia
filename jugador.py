import pygame
import config
class Player:
    #Constructor por defecto
    def __init__(self,posicion_x,posicion_y,posicion_z):
        print("Jugador creado.")
        self.posicion = [posicion_x,posicion_y]
    def update(self):
        print("Jugador actualizado.")
    def render(self,pantalla):
        pygame.draw.rect(pantalla,config.WHITE,(self.positions[0]*config.SCALE,self.positions[1]*config.SCALE,config.SCALE,config.SCALE),2)
