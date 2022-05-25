#Importamos las librerias que usaremos
import pygame #Libreria especifica para juegos
import config
from juego import Juego
from estado_juego import EstadoJuego
#Inicializamos el contrusctor de la clase pygame 
pygame.init()
#Creamos una variable pantalla donde guardamos 
# las dimensiones del display donde vamos a ver el juego.
#Facilmente configurable
pantalla =  pygame.display.set_mode((600,400)) #Largo,Ancho
pygame.display.set_caption('Projecto Princesa.') #Colocamos un nombre para la ventana que va aparecer.
reloj = pygame.time.Clock()
juego = Juego(pantalla)
#Lo metemos en un while para mantenerlo andando hasta que lo cerremos.
bandera = True
juego.set_up()
while juego.estado_juego == EstadoJuego.CORRIENDO:
    reloj.tick(1)
    juego.update()
    #Actualizamos el contenido de la pantalla con flip.
    pygame.display.flip()
