from random import randint
from random import seed
import pygame
import config
#Generar un numero aleatorio entre un maximo y minimo.
def generador_numero_aleatorio(min, maximo):
    seed()
    return randint(min, maximo)
def reaccion_tux():
    print("Hola joven princesa, que sistema operativo te parece el mejor?")
    so_eleccion = input("Linux(0)/MacOS(1)/Windows(2)")
    if so_eleccion == "2":
        print("Me das lastima jovencita.")
def reaccion(pantalla,input):
    #fuente = config.FUENTE_BASE
    #rectangulo = config.RECTANGULO_BASE
    #color = config.COLOR_RECTANGULO
    #pygame.draw.rect(pantalla,color,rectangulo)
    #texto_superficial = fuente.render(input,True,(config.NEGRO))
    #pantalla.blit(texto_superficial,(rectangulo.x+5,rectangulo.y+5))
    #rectangulo.w = max(100,texto_superficial.get_width() +10)
    imagen=pygame.image.load("imagenes/dialogo.png")
    imagen=pygame.transform.scale(imagen,(640,200))
    pantalla.blit(imagen,(0,280))
    fuente = pygame.font.Font('alagard.ttf',40)
    imagen2=fuente.render(input,True,config.NEGRO)
    pantalla.blit(imagen2,(40,320))
    fuenteSi=pygame.font.Font('alagard.ttf',35)
    fuenteNo=pygame.font.Font('alagard.ttf',35)
    fuenteSi=fuenteSi.render("Si (Y)",True,config.NEGRO)
    fuenteNo=fuenteNo.render("NO (N)",True,config.NEGRO)
    fuenteSalir=pygame.font.Font('alagard.ttf',35)
    fuenteSalir=fuenteSalir.render("Salir (Q)",True,config.NEGRO)
    pantalla.blit(fuenteSalir,(475,285))
    pantalla.blit(fuenteNo,(450,400))
    pantalla.blit(fuenteSi,(40,400))
