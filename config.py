import pygame
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
DORADO = (220, 184, 5)
DORADO2 = (236, 196, 0)
# Imagenes
PRINCESA_DERECHA = "imagenes/pricensa_derecha.png"
PRINCESA_IZQUIERDA = "imagenes/princesa_izquierda.png"
PRINCESA_FRENTE = "imagenes/princesa_frente.png"
PRINCESA_ESPALDA = "imagenes/princesa_espalda.png"
# Dimensiones
ESCALA = 32
ALTO_PANTALLA = 480
LARGO_PANTALLA = 640
# Fuentes y rectangulo
pygame.init()
FUENTE_BASE = pygame.font.Font(None, 32)
RECTANGULO_BASE = pygame.Rect(0, 0, 200, 100)
COLOR_RECTANGULO = pygame.Color((242, 238, 203))
# Letras para traducir el mapa desde la matriz.
LETRA_MAPA_INICIO_FIN = "D"
LETRA_MAPA_PARED = "F"
LETRA_MAPA_PIEDRA = "S"
LETRA_MAPA_CAMINO = "C"
LETRA_MAPA_AGUA = "A"
LETRA_MAPA_PASTO = "P"
LETRA_MAPA_LADRILLO = "T"
LETRA_MAPA_POCION = "X"
LETRA_MAPA_L = "L"
LETRA_MAPA_LIBRO = "B"
LETRA_MAPA_LIBRO2 = "G"
LETRA_MAPA_LLAVE = "K"
LETRA_MAPA_INTERACCION = "I"
