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
##OBJETOS
#PINGUINO
LETRA_MAPA_PINGUINO = "P"
LETRA_INT_PINGUINO = "1"
#MANZANA
LETRA_MAPA_MANZANA = "M"
LETRA_INT_MANZANA = "2"
#CALCULADORA
LETRA_MAPA_CALCULADORA = "C"
LETRA_INT_CALCULADORA = "3"
#BRUJULA
LETRA_MAPA_BRUJULA = "O"
LETRA_INT_BRUJULA = "4"
#BOLA
LETRA_MAPA_BOLA = "B"
LETRA_INT_BOLA = "5"
#GIT
LETRA_MAPA_GIT = "H"
LETRA_INT_GIT = "6"
#LIBRO
LETRA_MAPA_LIBRO = "L"
LETRA_INT_LIBRO = "7"
#SERPIENTE
LETRA_MAPA_SERPIENTE = "Y"
LETRA_INT_SERPIENTE = "8"
#POCION
LETRA_MAPA_POCION = "X"
LETRA_INT_POCION = "9"
#OBJETOS NO INTERACTUANTES
LETRA_MAPA_LIBRO = "B"
LETRA_MAPA_LIBRO2 = "G"
LETRA_MAPA_LLAVE = "K"
