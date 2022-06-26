import math
import pygame
# Modulos creados
from jugador import Jugador
from estado_juego import EstadoJuego
import config


class Juego:
    # Constructor por defecto.
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.objetos = []
        # Establecemos el juego como en el constructor por defecto.
        self.estado_juego = EstadoJuego.NULO
        self.mapa = []  # Creamos un arreglo donde almacenar la matriz del mapa
        # Por defecto sino se ha movido aun, no ha desenlazado todos los enventos
        self.jugador_se_movio = False
        # Creamos un objeto camara para seguimiento_camara en el mapa
        self.camara = [0, 0]

    def configurar(self):  # Esta funcion hace una configuracion inicial del juego, creando un Jugador localizado en el 1,1
        jugador = Jugador(1, 1)
        self.jugador = jugador
        # Cargamos al jugador dentro de la lista de objetos
        self.objetos.append(jugador)
        self.estado_juego = EstadoJuego.CORRIENDO
        self.cargar_mapa("03")

    def actualizar(self):
        self.pantalla.fill(config.NEGRO)
        #print("actualizado")
        self.manipular_eventos()
        self.render_mapa(self.pantalla)
        # Este es el constante actualizador
        # Ctemente esta fijandose si se actualizaron los datos del juego
        # Y luego renderizandolos
        for objeto in self.objetos:
            # Aca asumimos que todos los objetos
            objeto.render(self.pantalla, self.camara)
            # de esta lista tiene el metodo render()
        if self.jugador_se_movio:
            self.determinar_eventos_jugador()

    def determinar_eventos_jugador(self):
        # TRADUCIME
        letra_mapa = self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]]

        if letra_mapa == config.LETRA_MAPA_CAMINO:
            return

    def manipular_eventos(self):
        presionado = pygame.key.get_pressed() 

        if presionado[pygame.K_w]:
            self.mover_unidad(self.jugador, (0, -1))
            self.jugador.imagen=self.jugador.imagenes["arriba"]
        elif presionado[pygame.K_s]:
            self.mover_unidad(self.jugador, (0, 1))
            self.jugador.imagen=self.jugador.imagenes["abajo"]
        elif presionado[pygame.K_a]:
            self.mover_unidad(self.jugador, (-1, 0))
            self.jugador.imagen=self.jugador.imagenes["izquierda"]
        elif presionado[pygame.K_d]:
            self.mover_unidad(self.jugador, (1, 0))
            self.jugador.imagen=self.jugador.imagenes["derecha"]


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.estado_juego = EstadoJuego.TERMINADO
            elif evento.type == pygame.KEYDOWN:
                # Si el jugador toca "Esc" el estado del juego cambia a termina.
                if evento.key == pygame.K_ESCAPE:
                    self.estado_juego = EstadoJuego.TERMINADO
                    """"
                elif evento.key == pygame.K_w:  # arriba
                    self.mover_unidad(self.jugador, (0, -1))
                    self.jugador.imagen=self.jugador.imagenes["arriba"]
                elif evento.key == pygame.K_s:  # abajo
                    self.mover_unidad(self.jugador, (0, 1))
                    self.jugador.imagen=self.jugador.imagenes["abajo"]
                elif evento.key == pygame.K_a:  # izquierda
                    self.mover_unidad(self.jugador, (-1, 0))
                    self.jugador.imagen=self.jugador.imagenes["izquierda"]
                elif evento.key == pygame.K_d:  # derecha
                    self.mover_unidad(self.jugador, (1, 0))
                    self.jugador.imagen=self.jugador.imagenes["derecha"]
                    """

    def cargar_mapa(self, nombre_archivo):
        with open('mapas/' + nombre_archivo + ".txt") as mapa_archivo:
            for linea in mapa_archivo:
                letras = []  # Creamos una lista de letras observadas
                # Esto permite determinar que tipo de fondo lleva
                # cada elemento de la matriz mapa
                for i in range(0, len(linea) - 1, 2):
                    # Guardamos todos los valores de las letras
                    letras.append(linea[i])
                # Ahora guardamos esa lista de letras en la matriz mapa
                self.mapa.append(letras)

    def render_mapa(self, pantalla):
        self.seguimiento_camara()

        y_pos = 0
        for linea in self.mapa:  # Recorremos cada fila de la matriz
            x_pos = 0
            for letra in linea:  # Recorremos cada columna de esa fila
                imagen = mapa_letras_imagen[letra]
                rectangulo = pygame.Rect(x_pos * config.ESCALA, (y_pos * config.ESCALA) - (
                    self.camara[1] * config.ESCALA), config.ESCALA, config.ESCALA)
                pantalla.blit(imagen, rectangulo)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

    def mover_unidad(self, unidad, cambio_posicion):
        # Actualizamoss la posicion de la unidad sumand el valor del vector
        # cambio de posicion en x e y.
        nueva_posicion = [unidad.posicion[0]+cambio_posicion[0],
                          unidad.posicion[1]+cambio_posicion[1]]
        # Verificamos que la posicion no se salga del mapa
        if nueva_posicion[0] < 0 or nueva_posicion[0] > (len(self.mapa[0])-1):

            return
        if nueva_posicion[1] < 0 or nueva_posicion[1] > (len(self.mapa[1])-1):

            return
        # Verificamos que la posicion no sea un tipo de mapa por donde
        # el jugador no puede pasar.
        # Por ejemplo un muro
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == "F":

            return
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == "P":

            return
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == "L":

            return
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == "X":

            return
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == "C":

            return
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == "A":

            return
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == "G":

            return
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == "B":

            return
        self.jugador_se_movio = True
        unidad.actualizarPosicion(nueva_posicion)

    def seguimiento_camara(self):
        max_posicion_y = len(self.mapa) - config.ALTO_PANTALLA / config.ESCALA

        # Tendremos al jugador siempre en el centro de la camara
        posicion_y = self.jugador.posicion[1] - math.ceil(
            round(config.ALTO_PANTALLA / config.ESCALA / 2))

        if posicion_y <= max_posicion_y and posicion_y >= 0:
            self.camara[1] = posicion_y
        elif posicion_y < 0:
            self.camara[1] = 0
        else:
            self.camara[1] = max_posicion_y


# Esta es la lista de letras que se usan en el mapa
mapa_letras_imagen = {
    "D": pygame.transform.scale(pygame.image.load("imagenes/D.png"), (config.ESCALA, config.ESCALA)),
    "F": pygame.transform.scale(pygame.image.load("imagenes/T.png"), (config.ESCALA, config.ESCALA)),
    "S": pygame.transform.scale(pygame.image.load("imagenes/S.png"), (config.ESCALA, config.ESCALA)),
    "C": pygame.transform.scale(pygame.image.load("imagenes/C.png"), (config.ESCALA, config.ESCALA)),
    "A": pygame.transform.scale(pygame.image.load("imagenes/A.png"), (config.ESCALA, config.ESCALA)),
    "P": pygame.transform.scale(pygame.image.load("imagenes/P.png"), (config.ESCALA, config.ESCALA)),
    "T": pygame.transform.scale(pygame.image.load("imagenes/T.png"), (config.ESCALA, config.ESCALA)),
    "X": pygame.transform.scale(pygame.image.load("imagenes/X.png"), (config.ESCALA, config.ESCALA)),
    "L": pygame.transform.scale(pygame.image.load("imagenes/L.png"), (config.ESCALA, config.ESCALA)),
    "B": pygame.transform.scale(pygame.image.load("imagenes/B.png"), (config.ESCALA, config.ESCALA)),
    "G": pygame.transform.scale(pygame.image.load("imagenes/G.png"), (config.ESCALA, config.ESCALA)),
    "K": pygame.transform.scale(pygame.image.load("imagenes/K.png"), (config.ESCALA, config.ESCALA)),
}