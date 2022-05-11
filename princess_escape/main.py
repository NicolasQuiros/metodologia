import pygame
import math
import random

# Iniciar pygame
pygame.init()
# Crear la pantalla
screen = pygame.display.set_mode((800, 600))

# Fondo
imagen_fondo = pygame.image.load('fondo.png')

# Título e ícono
pygame.display.set_caption("Antartic Invaders")
icono = pygame.image.load('linux.png')
pygame.display.set_icon(icono)

# Personaje del jugador
Jugador = pygame.image.load('pinguino1.png')
pinguX = 280
pinguY = 350
pinguX_cambio = 0

# Enemigo
Enemigo1 = pygame.image.load('enemigo1.png')
enemigoX = random.randint(0, 735)
enemigoY = random.randint(50, 150)
enemigoX_cambio = 4
enemigoY_cambio = 30

# Proyectil
# Listo: no se puede ver el proyectil en pantalla
# Fuego: el proyectil se está moviendo
Bala1 = pygame.image.load('proyectil1.png')
balaX = 0
balaY = 450
balaY_cambio = 12
bala_estado = "listo"

puntaje = 0


def pingu(x, y):
    screen.blit(Jugador, (pinguX, pinguY))


def enemigo(x, y):
    screen.blit(Enemigo1, (enemigoX, enemigoY))


def disparo(x, y):
    global bala_estado
    bala_estado = "fuego"
    screen.blit(Bala1, (x + 90, y + -15))


def esColision(enemigoX, enemigoY, balaX, balaY):
    distancia = math.sqrt(math.pow(enemigoX - balaX, 2) + (math.pow(enemigoY - balaY, 2)))
    if distancia < 27:
        return True
    else:
        return False


# Bucle de juego
running = True
while running:

    # Valores RGB
    screen.fill((47, 17, 57))
    # Imagen de fondo
    screen.blit(imagen_fondo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # si se presiona una tecla, revisar si es izq. o der.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pinguX_cambio = -5
            if event.key == pygame.K_RIGHT:
                pinguX_cambio = +5
            if event.key == pygame.K_SPACE:
                if bala_estado == "listo":
                    balaX = pinguX
                    disparo(balaX, balaY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pinguX_cambio = 0
                # print(pinguX)
    # Revision de posición para evitar salir de la pantalla
    pinguX += pinguX_cambio
    if pinguX <= -91:
        pinguX = -91
    elif pinguX >= 639:
        pinguX = 639
    # Movimiento del enemigo
    enemigoX += enemigoX_cambio
    if enemigoX <= 0:
        enemigoX_cambio = 4
        enemigoX = 0
        enemigoY += enemigoY_cambio
    elif enemigoX >= 735:
        enemigoX_cambio = -4
        enemigoX = 734
        enemigoY += enemigoY_cambio
    # Movimiento del proyectil
    if bala_estado == "fuego":
        disparo(balaX, balaY)
        balaY -= balaY_cambio
    if balaY <= 0:
        balaY = 450
        bala_estado = ("listo")
    # Colisión
    colision = esColision(enemigoX, enemigoY, balaX, balaY)
    if colision:
        balaY = 450
        bala_estado = "listo"
        puntaje += 1
        print(puntaje)
        enemigoX = random.randint(-50, 639)
        enemigoY = random.randint(50, 150)

    pingu(pinguX, pinguY)
    enemigo(enemigoX, enemigoY)

    pygame.display.update()
