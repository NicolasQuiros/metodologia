# Importamos las librerias que usaremos
import pygame  # Libreria especifica para juegos
# Nuestros modulos de codigo van aca
import config
from juego import Juego
from estado_juego import EstadoJuego
# Aca arranca el codigo del main, aca se manejan todos los modulos
# Inicializamos el constructor de la clase pygame
pygame.init()
# Creamos una variable pantalla donde guardamos
# las dimensiones del display donde vamos a ver el juego.
# Facilmente configurable
# Seteamos la pantalla Largo,Ancho
pantalla = pygame.display.set_mode(
    (config.ALTO_PANTALLA, config.LARGO_PANTALLA))
# Colocamos un nombre para la ventana que va aparecer.
pygame.display.set_caption('Proyecto Princesa')
# reloj = pygame.time.Clock() #Pygame incluye una funcion time para setear el tiempo
juego = Juego(pantalla)
# Lo metemos en un while para mantenerlo andando hasta que lo cerremos.
juego.configurar()
while juego.estado_juego == EstadoJuego.CORRIENDO:
    # reloj.tick(50) #Seteamos el tiempo de juego en 50.
    juego.actualizar()  # hacemos la configuracion inicial
    # Actualizamos el contenido de la pantalla con flip.
    pygame.display.flip()