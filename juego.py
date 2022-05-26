import pygame
#Modulos creados 
from jugador import Jugador
from estado_juego import EstadoJuego
import config

class Juego:
    #Constructor por defecto.
    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.objetos = []
        self.estado_juego = EstadoJuego.NULO #Establecemos el juego como en el constructor por defecto.
        self.mapa = [] #Creamos un arreglo donde almacenar la matriz del mapa
    def configurar(self): #Esta funcion hace una configuracion inicial del juego, creando un Jugador localizado en el 1,1
        jugador = Jugador(1,1)
        self.jugador = jugador
        #Cargamos al jugador dentro de la lista de objetos
        self.objetos.append(jugador)
        self.estado_juego = EstadoJuego.CORRIENDO
        self.cargar_mapa("01")
    def actualizar(self):
        self.pantalla.fill(config.NEGRO)
        print("actualizado")
        self.manipular_eventos()
        self.render_mapa(self.pantalla)
        #Este es el constante actualizador
        #Ctemente esta fijandose si se actualizaron los datos del juego
        #Y luego renderizandolos
        for objeto in self.objetos:
            objeto.render(self.pantalla) #Aca asumimos que todos los objetos 
                                #de esta lista tiene el metodo render()
    def manipular_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.estado_juego = EstadoJuego.TERMINADO
            elif evento.type == pygame.KEYDOWN:
                #Si el jugador toca "Esc" el estado del juego cambia a termina.
                if evento.key == pygame.K_ESCAPE:
                    self.estado_juego = EstadoJuego.TERMINADO
                elif evento.key == pygame.K_w: #arriba
                    self.jugador.actualizarPosicion(0,-1)
                elif evento.key == pygame.K_s: #abajo
                    self.jugador.actualizarPosicion(0,1)
                elif evento.key == pygame.K_a: #izquierda
                    self.jugador.actualizarPosicion(-1,0)
                elif evento.key == pygame.K_d: #derecha
                    self.jugador.actualizarPosicion(1,0)
    def cargar_mapa(self, nombre_archivo):
        with open('mapas/' + nombre_archivo + ".txt") as map_archivo:
            for linea in map_archivo:
                letras = [] #Creamos una lista de letras observadas
                            #Esto permite determinar que tipo de fondo lleva 
                            # cada elemento de la matriz mapa
                for i in range(0, len(linea), 2):
                    letras.append(linea[i]) #Guardamos todos los valores de las letras
                self.mapa.append(letras) #Ahora guardamos esa lista de letras en la matriz mapa
            print(self.mapa)

    def render_mapa(self, pantalla):
        y_pos = 0
        for linea in self.mapa: #Recorremos cada fila de la matriz
            x_pos = 0
            for letra in linea: #Recorremos cada columna de esa fila
                imagen = mapa_letras_imagen[letra] 
                rectangulo = pygame.Rect(x_pos * config.ESCALA, y_pos * config.ESCALA, config.ESCALA, config.ESCALA)
                pantalla.blit(imagen, rectangulo)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

mapa_letras_imagen = {
    "G" : pygame.transform.scale(pygame.image.load("imagenes/grass1.png"), (config.ESCALA, config.ESCALA)),
    "W": pygame.transform.scale(pygame.image.load("imagenes/water.png"), (config.ESCALA, config.ESCALA))
}
