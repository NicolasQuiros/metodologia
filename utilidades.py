from random import randint
from random import seed
import pygame
import config
# Generar un numero aleatorio entre un maximo y minimo.


def generador_numero_aleatorio(min, maximo):
    seed()
    return randint(min, maximo)


def reaccion_tux():
    print("Hola joven princesa, que sistema operativo te parece el mejor?")
    so_eleccion = input("Linux(0)/MacOS(1)/Windows(2)")
    if so_eleccion == "2":
        print("Me das lastima jovencita.")
    elif so_eleccion == "0":
        print("Excelente eleccion")


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
