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
# Establecemos el nombre del juego en la barra de título
pygame.display.set_caption('La Princesa y El Pingüino')
# Damos tamaño a la pantalla
pantalla = pygame.display.set_mode((640, 480), 0, 32)

# Dfinimos el fondo para el menú
imagenFondo = pygame.image.load("imagenes/fondo_menu.jpg")

# Asignamos la fuente y el tamaño de letra para los textos
fuente = pygame.font.Font("alagard.ttf", 25)
# Cargamos la pista de audio para la música de fondo
mixer.music.load("musica/Music Box - Brian Bolger.mp3")
# Damos valor -1 a la reproducción para reproducir en bucle
mixer.music.play(-1)

# Pygame incluye una funcion time para setear el tiempo
reloj = pygame.time.Clock()
juego = Juego(pantalla)
# definimos una variable booleana para pausar la música
pausa = False


# creamos una función para alternar el estado de la variable pausa
def pausar_musica(pausa):
    if pausa == False:
        pygame.mixer.music.unpause()
    elif pausa == True:
        pygame.mixer.music.pause()
    pausa = False


# definimos una variable booleana para almacenar el click
click = False


# Creamos una función que reciba  fuente, color y posición del texto de lo botones
def escribirTexto(texto, fuente, color, superficie, x, y):
    textoObjeto = fuente.render(texto, 1, color)
    textoRectangulo = textoObjeto.get_rect()
    textoRectangulo.topleft = (x, y)
    superficie.blit(textoObjeto, textoRectangulo)

#Función del menú princial
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
                #al hacer click dentro de los límites del botón, el juego llama a la función configurar de la clase juego
                juego.configurar()
                while juego.estado_juego == EstadoJuego.CORRIENDO:
                    reloj.tick(7)  # Seteamos el tiempo de juego en 7.
                    juego.actualizar()  # hacemos la configuracion inicial
                    # Actualizamos el contenido de la pantalla con flip.
                    pygame.display.flip()
                if EstadoJuego.TERMINADO:
                    break
        if boton2.collidepoint((mx, my)):
            if click:
                #al hacer click en el segundo botón invertimos el valor para pausar la música
                pausarMusica = not pausarMusica
                pausar_musica(pausarMusica)
        #dibujamos los dos botones
        pygame.draw.rect(pantalla, (233, 196, 0), boton1, 0, 10)
        pygame.draw.rect(pantalla, (233, 196, 0), boton2, 0, 10)
        #introducimos el texto de cada botón y su posición
        escribirTexto('Iniciar Juego', fuente, (185, 155, 8), pantalla, 425, 305)
        escribirTexto('Musica ON/OFF', fuente, (185, 155, 8), pantalla, 407, 380)
        #reestablecemos la variable click a falso
        click = False
        #si el usuario clickea en cerrar ventana o presiona escape, la ventana de juego se cierra
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            #registramos el clickeo en la variable click
            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    click = True

        pygame.display.update()
        relojPrincipal.tick(60)


menuPrincipal(pausa)
