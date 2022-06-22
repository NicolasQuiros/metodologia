import pygame
import config
import math

from jugador import Jugador
from estado_juego import EstadoJuego


class Menu:
    def __init__(self, pantalla, juego):
        self.pantalla = pantalla
        self.juego = juego

    def configurar(self):
        self.imagenMenu= (pygame.image.load("sprites/fondo_menu.png")
        pass

    def actualizar(self):
        rect =pygame.rect(1, 1, 2, 2)
        screen.blit(self.imagenMenu, rect)
