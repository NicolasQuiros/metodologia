#Importamos las librerias que usaremos
import pygame #Libreria especifica para juegos 
#Nuestros modulos de codigo van aca
import config
from juego import Juego
from estado_juego import EstadoJuego
#Aca arranca el codigo del main, aca se manejan todos los modulos
#Inicializamos el constructor de la clase pygame 
pygame.init()
#Creamos una variable pantalla donde guardamos 
# las dimensiones del display donde vamos a ver el juego.
#Facilmente configurable
pantalla =  pygame.display.set_mode((600,400)) #Seteamos la pantalla Largo,Ancho
pygame.display.set_caption('Projecto Princesa.') #Colocamos un nombre para la ventana que va aparecer.
reloj = pygame.time.Clock() #Pygame incluye una funcion time para setear el tiempo
juego = Juego(pantalla)
#Lo metemos en un while para mantenerlo andando hasta que lo cerremos.
bandera = True
juego.set_up()
while juego.estado_juego == EstadoJuego.CORRIENDO:
    reloj.tick(1) #Seteamos el tiempo de juego en 1.
    juego.configurar() #hacemos la configuracion inicial
    #Actualizamos el contenido de la pantalla con flip.
    pygame.display.flip()
