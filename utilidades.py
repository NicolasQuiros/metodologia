from random import randint
from random import seed
import pygame
import config
# Generar un numero aleatorio entre un maximo y minimo.


def generador_numero_aleatorio(min, maximo):
    seed()
    return randint(min, maximo)


def reaccion_tux():
    ("Hola joven princesa, que sistema operativo te parece el mejor?")
    so_eleccion = input("Linux(0)/MacOS(1)/Windows(2)")
    if so_eleccion == "2":
        ("Me das lastima jovencita.")
    elif so_eleccion == "0":
        ("Excelente eleccion")


def generar_burbuja_texto2(pantalla, texto, texto2, opcion1, opcion2):
    # Cargamos la imagen del fondo.
    imagen = pygame.image.load("imagenes/dialogo.png")
    # La escalamos para que quede bien en nuestro juego
    imagen = pygame.transform.scale(imagen, (640, 200))
    # Superponemos la imagen con el fondo del juego.
    pantalla.blit(imagen, (0, 280))
    # Definimos una fuente comun
    fuente = pygame.font.Font('alagard.ttf', 40)
    # Renderizamos el texto ingresado
    imagen2 = fuente.render(texto, True, config.NEGRO)
    imagen3 = fuente.render(texto2, True, config.NEGRO)
    # Superponemos el texto a la imagen ya superpuesta antes.
    pantalla.blit(imagen2, (40, 320))
    pantalla.blit(imagen3, (40,360))
    # Definimos una fuente comun para el si y el no.
    fuenteSi = pygame.font.Font('alagard.ttf', 35)
    fuenteNo = pygame.font.Font('alagard.ttf', 35)
    # Renderizamos el texto en la imagen ya superpuesta antes
    fuenteSi = fuenteSi.render(str(opcion1)+"(Y)", True, config.NEGRO)
    fuenteNo = fuenteNo.render(str(opcion2)+"(N)", True, config.NEGRO)
    fuenteSalir = pygame.font.Font('alagard.ttf', 35)
    fuenteSalir = fuenteSalir.render("Salir (Q)", True, config.NEGRO)
    # Superponemos el texto salir,si,no.
    pantalla.blit(fuenteSalir, (475, 285))
    pantalla.blit(fuenteNo, (450, 420))
    pantalla.blit(fuenteSi, (40, 420))

def generar_burbuja_texto(pantalla, texto, opcion1, opcion2):
    # Cargamos la imagen del fondo.
    imagen = pygame.image.load("imagenes/dialogo.png")
    # La escalamos para que quede bien en nuestro juego
    imagen = pygame.transform.scale(imagen, (640, 200))
    # Superponemos la imagen con el fondo del juego.
    pantalla.blit(imagen, (0, 280))
    # Definimos una fuente comun
    fuente = pygame.font.Font('alagard.ttf', 40)
    # Renderizamos el texto ingresado
    imagen2 = fuente.render(texto, True, config.NEGRO)
    # Superponemos el texto a la imagen ya superpuesta antes.
    pantalla.blit(imagen2, (40, 320))
    # Definimos una fuente comun para el si y el no.
    fuenteSi = pygame.font.Font('alagard.ttf', 35)
    fuenteNo = pygame.font.Font('alagard.ttf', 35)
    # Renderizamos el texto en la imagen ya superpuesta antes
    fuenteSi = fuenteSi.render(str(opcion1)+"(Y)", True, config.NEGRO)
    fuenteNo = fuenteNo.render(str(opcion2)+"(N)", True, config.NEGRO)
    fuenteSalir = pygame.font.Font('alagard.ttf', 35)
    fuenteSalir = fuenteSalir.render("Salir (Q)", True, config.NEGRO)
    # Superponemos el texto salir,si,no.
    pantalla.blit(fuenteSalir, (475, 285))
    pantalla.blit(fuenteNo, (450, 400))
    pantalla.blit(fuenteSi, (40, 400))

################################################################################################
def generar_burbuja_text_nivel(pantalla, vector):
    POS_X = 105
    # Cargamos la imagen del fondo.
    imagen = pygame.image.load("imagenes/papiro.png")
    # La escalamos para que quede bien en nuestro juego
    imagen = pygame.transform.scale(imagen, (250, 320))
    # Superponemos la imagen con el fondo del juego.
    pantalla.blit(imagen, (390, 20))
    # Definimos una fuente comun
    fuente = pygame.font.Font('alagard.ttf', 22)
   # Renderizamos el texto ingresado
    textos = []
    for mision in vector:
        textos.append("Completo" if mision == True else "Incompleto")

    imagen1 = fuente.render(textos[0], True, config.NEGRO)
    imagen2 = fuente.render(textos[1], True, config.NEGRO)
    imagen3 = fuente.render(textos[2], True, config.NEGRO)
    imagen4 = fuente.render(textos[3], True, config.NEGRO)
    imagen5 = fuente.render(textos[4], True, config.NEGRO)
    imagen6 = fuente.render(textos[5], True, config.NEGRO)
    imagen7 = fuente.render(textos[6], True, config.NEGRO)
    imagen8 = fuente.render(textos[7], True, config.NEGRO)
    imagen9 = fuente.render(textos[8], True, config.NEGRO)
    # Superponemos el texto a la imagen ya superpuesta antes.
    pantalla.blit(imagen1, (460, POS_X-20))
    pantalla.blit(imagen2, (460,POS_X+2))
    pantalla.blit(imagen3, (460,POS_X+22))
    pantalla.blit(imagen4, (460,POS_X+42))
    pantalla.blit(imagen5, (460,POS_X+62))
    pantalla.blit(imagen6, (460,POS_X+82))
    pantalla.blit(imagen7, (460,POS_X+102))
    pantalla.blit(imagen8, (460,POS_X+122))
    pantalla.blit(imagen9, (460,POS_X+142))
    # Renderizamos el texto en la imagen ya superpuesta antes
    fuenteSalir = pygame.font.Font('alagard.ttf', 20)
    fuenteSalir = fuenteSalir.render("Salir (Q)", True, config.NEGRO)
    # Superponemos el texto salir,si,no.
    pantalla.blit(fuenteSalir, (480, 42))
def generar_burbuja_ganar(pantalla):
    # Cargamos la imagen del fondo.
    imagen = pygame.image.load("imagenes/dialogo.png")
    # La escalamos para que quede bien en nuestro juego
    imagen = pygame.transform.scale(imagen, (640, 200))
    # Superponemos la imagen con el fondo del juego.
    pantalla.blit(imagen, (0, 280))
    # Definimos una fuente comun
    fuente = pygame.font.Font('alagard.ttf', 40)
    # Renderizamos el texto ingresado
    imagen2 = fuente.render("Has completado todos", True, config.NEGRO)
    imagen3 = fuente.render("los objetivos, ganaste!", True, config.NEGRO)
    # Superponemos el texto a la imagen ya superpuesta antes.
    pantalla.blit(imagen2, (40, 320))
    pantalla.blit(imagen3, (40,360))
    # Renderizamos el texto en la imagen ya superpuesta antes
    fuenteSalir = pygame.font.Font('alagard.ttf', 35)
    fuenteSalir = fuenteSalir.render("Salir (Q)", True, config.NEGRO)
    # Superponemos el texto salir,si,no.
    pantalla.blit(fuenteSalir, (475, 285))
def generar_burbuja_no_ganar(pantalla):
    # Cargamos la imagen del fondo.
    imagen = pygame.image.load("imagenes/dialogo.png")
    # La escalamos para que quede bien en nuestro juego
    imagen = pygame.transform.scale(imagen, (640, 200))
    # Superponemos la imagen con el fondo del juego.
    pantalla.blit(imagen, (0, 280))
    # Definimos una fuente comun
    fuente = pygame.font.Font('alagard.ttf', 40)
    # Renderizamos el texto ingresado
    imagen2 = fuente.render("Todavia no completaste", True, config.NEGRO)
    imagen3 = fuente.render("los objetivos, pulsa 'V'", True, config.NEGRO)
    # Superponemos el texto a la imagen ya superpuesta antes.
    pantalla.blit(imagen2, (40, 320))
    pantalla.blit(imagen3, (40,360))
    # Renderizamos el texto en la imagen ya superpuesta antes
    fuenteSalir = pygame.font.Font('alagard.ttf', 35)
    fuenteSalir = fuenteSalir.render("Salir (Q)", True, config.NEGRO)
    # Superponemos el texto salir,si,no.
    pantalla.blit(fuenteSalir, (475, 285))