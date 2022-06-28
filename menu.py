import pygame
import sys
from estado_juego import EstadoJuego
from juego import Juego
import config
relojPrincipal = pygame.time.Clock()
# Importamos el mezclador de música de la biblioteca Pygame
from pygame.locals import *
from pygame import mixer

# Inicializamos pygame
pygame.init()
pygame.display.set_caption('La Princesa y El Pingüino')
pantalla = pygame.display.set_mode((640, 480), 0, 32)

# Dfinimos el fondo para el menú
imagenFondo = pygame.image.load("imagenes/fondo_menu.jpg")

# Asignamos la fuente y el tamaño de letra para los textos
fuente = pygame.font.Font("alagard.ttf", 25)
# Cargamos la pista de audio para la música de fondo
mixer.music.load("musica/Music Box - Brian Bolger.mp3")

mixer.music.play(-1)
pantalla = pygame.display.set_mode(
    (config.LARGO_PANTALLA, config.ALTO_PANTALLA))
# Colocamos un nombre para la ventana que va aparecer.
pygame.display.set_caption('La Princesa y el Pingüino')
reloj = pygame.time.Clock()  # Pygame incluye una funcion time para setear el tiempo
juego = Juego(pantalla)

pausarMusica = False
def pausar_musica(pausarMusica):
    if pausarMusica == False:
        pygame.mixer.music.unpause()
    elif pausarMusica == True:
        pygame.mixer.music.pause()
    pausarMusica = False
click = False

# Definimos una función para
def escribirTexto(texto, fuente, color, superficie, x, y):
    textoObjeto = fuente.render(texto, 1, color)
    textoRectangulo = textoObjeto.get_rect()
    textoRectangulo.topleft = (x, y)
    superficie.blit(textoObjeto, textoRectangulo)


def menuPrincipal(pausarMusica):
    while True:
        # Cargamos el fondo del menú
        pantalla.fill((0, 0, 0))
        pantalla.blit(imagenFondo, (0, 0))
        # El programa recibe la posición del mouse
        mx, my = pygame.mouse.get_pos()
        # Creamos los dos botones
        boton1 = pygame.Rect(400, 290, 200, 50)
        boton2 = pygame.Rect(400, 365, 200, 50)
        # Asignamos los puntos de colisión del mouse respecto de cada botón
        if boton1.collidepoint((mx, my)):
            if click:
                juego.configurar()
                while juego.estado_juego == EstadoJuego.CORRIENDO:
                    reloj.tick(7)  # Seteamos el tiempo de juego en 50.
                    juego.actualizar()  # hacemos la configuracion inicial
                    # Actsualizamos el contenido de la pantalla con flip.
                    pygame.display.flip()
                if EstadoJuego.TERMINADO:
                    break
        if boton2.collidepoint((mx, my)):
            if click:
                pausarMusica = not  pausarMusica
                pausar_musica(pausarMusica)
        pygame.draw.rect(pantalla, (233, 196, 0), boton1, 0, 10)
        pygame.draw.rect(pantalla, (233, 196, 0), boton2, 0, 10)
        escribirTexto('Iniciar Juego', fuente, (185, 155, 8), pantalla, 425, 305)
        escribirTexto('Musica ON/OFF', fuente, (185, 155, 8), pantalla, 407, 380)
        click = False
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    click = True

        pygame.display.update()
        relojPrincipal.tick(60)

menuPrincipal(pausarMusica)
