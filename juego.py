from ast import If
import math
from threading import Timer
import pygame
# Modulos creados
from jugador import Jugador
from estado_juego import EstadoJuego
from iteraccion_objetos import IteraccionObjetos
from utilidades import generar_burbuja_text_nivel, generar_burbuja_texto, generar_burbuja_texto2,generar_burbuja_ganar,generar_burbuja_no_ganar, generar_burbuja_texto3
from estado_nivel import EstadoNivel
import config
import textos


class Juego:
    # Constructor por defecto.
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.objetos = []
        # Establecemos el juego como en el constructor por defecto.
        self.estado_juego = EstadoJuego.NULO
        self.iteraccion_objetos = IteraccionObjetos.NADA
        self.mapa = []  # Creamos un arreglo donde almacenar la matriz del mapa
        # Por defecto sino se ha movido aun, no ha desenlazado todos los enventos
        self.jugador_se_movio = False
        # Creamos un objeto camara para seguimiento_camara en el mapa
        self.camara = [0, 0]
        self.estado_nivel = EstadoNivel()
        # Atributo que nos dice si la princesa ya tiene la llave
        self.llave = False
    
    def configurar(self):  # Esta funcion hace una configuracion inicial del juego, creando un Jugador localizado en el 1,1
        jugador = Jugador(1, 1)
        self.jugador = jugador
        # Cargamos al jugador dentro de la lista de objetos
        self.objetos.append(jugador)
        self.estado_juego = EstadoJuego.CORRIENDO
        self.cargar_mapa("04")

    def actualizar(self):
        self.pantalla.fill(config.NEGRO)
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
            self.chequear_interacciones()
        self.iteracciones_jugador()

    def iteracciones_jugador(self):
        if self.iteraccion_objetos == IteraccionObjetos.NADA:
            return
        elif self.iteraccion_objetos == IteraccionObjetos.PINGUINO_INICIO:
            #reaccion(self.pantalla, "Hola!")
            generar_burbuja_texto2(
                self.pantalla, textos.SALUDO_PINGUINO,textos.SALUDO_PINGUINO2, textos.OPCION1_PINGUINO, textos.OPCION2_PINGUINO)
            #self.iteraccion_objetos = IteraccionObjetos.NADA
            return
        elif self.iteraccion_objetos == IteraccionObjetos.MANZANA:
            generar_burbuja_texto2(self.pantalla, textos.PREGUNTA_MANZANA, textos.PREGUNTA_MANZANA2,
                                   textos.OPCION1_MANZANA, textos.OPCION2_MANZANA)
            #self.iteraccion_objetos = IteraccionObjetos.NADA
            return
        elif self.iteraccion_objetos == IteraccionObjetos.CALCULADORA:
            generar_burbuja_texto(
                self.pantalla, textos.PREGUNTA_CAL, textos.OPCION2_CAL, textos.OPCION1_CAL)
            return

        elif self.iteraccion_objetos == IteraccionObjetos.BOLA:
            generar_burbuja_texto(self.pantalla, textos.PREGUNTA_BOLACRISTAL,
                                  textos.OPCION2_BOLACRISTAL, textos.OPCION1_BOLACRISTAL)
            return

        elif self.iteraccion_objetos == IteraccionObjetos.BRUJULA:
            generar_burbuja_texto(self.pantalla, textos.PREGUNTA_BRUJULA,
                                  textos.OPCION1_BRUJULA, textos.OPCION2_BRUJULA)
            return

        elif self.iteraccion_objetos == IteraccionObjetos.GIT:
            generar_burbuja_texto(
                self.pantalla, textos.PREGUNTA_GIT, textos.OPCION1_GIT, textos.OPCION2_GIT)
            return

        elif self.iteraccion_objetos == IteraccionObjetos.LIBRO:
            generar_burbuja_texto(
                self.pantalla, textos.PREGUNTO_LIBRO, textos.OPCION1_LIBRO, textos.OPCION2_LIBRO)
            return

        elif self.iteraccion_objetos == IteraccionObjetos.SERPIENTE:
            generar_burbuja_texto3(self.pantalla, textos.PREGUNTA_SERPIENTE, textos.PREGUNTA_SERPIENTE2,
                                   textos.OPCION2_SERPIENTE, textos.OPCION1_SERPIENTE)
            return

        elif self.iteraccion_objetos == IteraccionObjetos.POCION:
            generar_burbuja_texto2(
                self.pantalla, textos.PREGUNTA_POCION, textos.PREGUNTA_POCION2,
                textos.OPCION1_POCION, textos.OPCION2_POCION)
            return
        elif self.iteraccion_objetos == IteraccionObjetos.NIVEL:
            textos_vector = self.estado_nivel.acceder_nivel()
            generar_burbuja_text_nivel(self.pantalla, textos_vector)
            return
        elif self.iteraccion_objetos == IteraccionObjetos.GANAR:
            if (self.chequear_interacciones()):
                self.llave = True
                generar_burbuja_ganar(
                self.pantalla)
                return
            else:
                generar_burbuja_no_ganar(self.pantalla)
                return

    def determinar_eventos_jugador(self):
        #Tenemos que chequear si el jugador ya gano el juego,
        #Primero chequeamos que todas las interacciones esten listas
        #Luego que la princesa haya tocado la llave.
        letra_mapa = self.mapa[self.jugador.posicion[1]
                               ][self.jugador.posicion[0]]
        if letra_mapa == config.LETRA_MAPA_INICIO_FIN and self.llave == True:
            self.estado_juego = EstadoJuego.TERMINADO
        #Luego que la princesa este en el terreno de salida
    def chequear_interacciones(self):
        #Si todas los estados del nivel estan completos entonces podemos seguir.
        if (self.estado_nivel.uno == True and 
        self.estado_nivel.dos == True and
        self.estado_nivel.tres == True and
        self.estado_nivel.cuatro == True and
        self.estado_nivel.cinco == True and 
        self.estado_nivel.seis == True and 
        self.estado_nivel.siete == True and
        self.estado_nivel.ocho == True and
        self.estado_nivel.nueve == True):
            return True
    def manipular_eventos(self):
        # Si el jugador toca o mantiene presionada una tecla.
        presionado = pygame.key.get_pressed()
        # Si toca o mantiene presionado w se mueve arriba
        if presionado[pygame.K_w]:
            self.mover_unidad(self.jugador, (0, -1))
            self.jugador.imagen = self.jugador.imagenes["arriba"]
        # Si toca o mantiene presionado w se mueve abajo
        elif presionado[pygame.K_s]:
            self.mover_unidad(self.jugador, (0, 1))
            self.jugador.imagen = self.jugador.imagenes["abajo"]
        # Si toca o mantiene presionado w se mueve izquierda
        elif presionado[pygame.K_a]:
            self.mover_unidad(self.jugador, (-1, 0))
            self.jugador.imagen = self.jugador.imagenes["izquierda"]
        # Si toca o mantiene presionado w se mueve derecha
        elif presionado[pygame.K_d]:
            self.mover_unidad(self.jugador, (1, 0))
            self.jugador.imagen = self.jugador.imagenes["derecha"]
        # Si presiona una sola vez la tecla se genera un evento
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.estado_juego = EstadoJuego.TERMINADO
            elif evento.type == pygame.KEYDOWN:
                # Si el jugador toca "Esc" el estado del juego cambia a termina.
                if evento.key == pygame.K_ESCAPE:
                    self.estado_juego = EstadoJuego.TERMINADO
                # Si el jugador toca la letra "E" para interactuar
                elif evento.key == pygame.K_e:
                    if self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == "1":
                        self.iteraccion_objetos = IteraccionObjetos.PINGUINO_INICIO

                    elif self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == "2":
                        self.iteraccion_objetos = IteraccionObjetos.MANZANA

                    elif self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == "3":
                        self.iteraccion_objetos = IteraccionObjetos.CALCULADORA

                    elif self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == "4":
                        self.iteraccion_objetos = IteraccionObjetos.BRUJULA

                    elif self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == "5":
                        self.iteraccion_objetos = IteraccionObjetos.BOLA

                    elif self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == "6":
                        self.iteraccion_objetos = IteraccionObjetos.GIT

                    elif self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == "7":
                        self.iteraccion_objetos = IteraccionObjetos.LIBRO

                    elif self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == "8":
                        self.iteraccion_objetos = IteraccionObjetos.SERPIENTE

                    elif self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == "9":
                        self.iteraccion_objetos = IteraccionObjetos.POCION
                    elif self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]] == config.LETRA_MAPA_LLAVE:
                        self.iteraccion_objetos = IteraccionObjetos.GANAR

                elif evento.key == pygame.K_q:
                    self.iteraccion_objetos = IteraccionObjetos.NADA
                # Evalua si esta en un estado de eventos y si se toco alguna de las letras
                # En caso de que toque la letra "Y" se confirma.
                elif evento.key == pygame.K_y:
                    if self.iteraccion_objetos == IteraccionObjetos.MANZANA:
                        # Actuliza el nivel para mantener un registro del juego.
                        self.estado_nivel.actualizar_nivel(
                            self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]])
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.PINGUINO_INICIO:
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.CALCULADORA:
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.BRUJULA:
                        self.estado_nivel.actualizar_nivel(
                            self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]])
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.BOLA:
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.GIT:
                        self.estado_nivel.actualizar_nivel(
                            self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]])
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.LIBRO:
                        self.estado_nivel.actualizar_nivel(
                            self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]])
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.SERPIENTE:
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.POCION:
                        self.estado_nivel.actualizar_nivel(
                            self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]])
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                # En caso de que toque la letra "N" se rechaza.
                elif evento.key == pygame.K_n:

                    if self.iteraccion_objetos == IteraccionObjetos.MANZANA:
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.PINGUINO_INICIO:
                        self.estado_nivel.actualizar_nivel(
                            self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]])
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.CALCULADORA:
                        self.estado_nivel.actualizar_nivel(
                            self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]])
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.BRUJULA:
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.BOLA:
                        self.estado_nivel.actualizar_nivel(
                            self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]])
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.GIT:
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.LIBRO:
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.SERPIENTE:
                        self.estado_nivel.actualizar_nivel(
                            self.mapa[self.jugador.posicion[1]][self.jugador.posicion[0]])
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                    elif self.iteraccion_objetos == IteraccionObjetos.POCION:
                        self.iteraccion_objetos = IteraccionObjetos.NADA

                # En caso de que el jugador toque la letra "V" pueda observar lo completado hasta ahora.
                elif evento.key == pygame.K_v:
                    self.iteraccion_objetos = IteraccionObjetos.NIVEL

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
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_PARED:
            return
        # PINGUINO
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_PINGUINO:
            return
        # MANZANA
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_MANZANA:
            return
        # CALCULADORA
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_CALCULADORA:
            return
        # BRUJULA
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_BRUJULA:

            return
        # BOLA
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_BOLA:

            return
        # GIT
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_GIT:

            return
        # LIBRO
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_LIBRO:

            return
        # SERPIENTE
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_SERPIENTE:
            return

        # POCION
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_POCION:
            return
        # LUZ
        if self.mapa[nueva_posicion[1]][nueva_posicion[0]] == config.LETRA_MAPA_LUZ:
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
    #CALCULADORA /C
    config.LETRA_MAPA_CALCULADORA: pygame.transform.scale(pygame.image.load("imagenes/Calculadora.png"), (config.ESCALA, config.ESCALA)),
    config.LETRA_INT_CALCULADORA: pygame.transform.scale(pygame.image.load("imagenes/S.png"), (config.ESCALA, config.ESCALA)),
    #PINGUINO /P
    config.LETRA_MAPA_PINGUINO: pygame.transform.scale(pygame.image.load("imagenes/A.png"), (config.ESCALA, config.ESCALA)),
    config.LETRA_INT_PINGUINO: pygame.transform.scale(pygame.image.load("imagenes/S.png"), (config.ESCALA, config.ESCALA)),
    #BOLA /B
    config.LETRA_MAPA_BOLA: pygame.transform.scale(pygame.image.load("imagenes/P.png"), (config.ESCALA, config.ESCALA)),
    config.LETRA_INT_BOLA: pygame.transform.scale(pygame.image.load("imagenes/frame.png"), (config.ESCALA, config.ESCALA)),
    #POSION /X
    config.LETRA_MAPA_POCION: pygame.transform.scale(pygame.image.load("imagenes/X.png"), (config.ESCALA, config.ESCALA)),
    config.LETRA_INT_POCION: pygame.transform.scale(pygame.image.load("imagenes/frame.png"), (config.ESCALA, config.ESCALA)),
    # LIBRO ROJO /R
    config.LETRA_MAPA_LIBRO: pygame.transform.scale(pygame.image.load("imagenes/R.png"), (config.ESCALA, config.ESCALA)),
    config.LETRA_INT_LIBRO: pygame.transform.scale(pygame.image.load("imagenes/frame.png"), (config.ESCALA, config.ESCALA)),
    # GIT
    config.LETRA_MAPA_GIT: pygame.transform.scale(pygame.image.load("imagenes/Gato.png"), (config.ESCALA, config.ESCALA)),
    config.LETRA_INT_GIT: pygame.transform.scale(pygame.image.load("imagenes/S.png"), (config.ESCALA, config.ESCALA)),
    # SERPIENTE
    config.LETRA_MAPA_SERPIENTE: pygame.transform.scale(pygame.image.load("imagenes/Serpiente.png"), (config.ESCALA, config.ESCALA)),
    config.LETRA_INT_SERPIENTE: pygame.transform.scale(pygame.image.load("imagenes/S.png"), (config.ESCALA, config.ESCALA)),
    # MANZANA
    config.LETRA_MAPA_MANZANA: pygame.transform.scale(pygame.image.load("imagenes/Manzana.png"), (config.ESCALA, config.ESCALA)),
    config.LETRA_INT_MANZANA: pygame.transform.scale(pygame.image.load("imagenes/S.png"), (config.ESCALA, config.ESCALA)),
    # BRÚJULA
    config.LETRA_MAPA_BRUJULA: pygame.transform.scale(pygame.image.load("imagenes/Brújula.png"), (config.ESCALA, config.ESCALA)),
    config.LETRA_INT_BRUJULA: pygame.transform.scale(pygame.image.load("imagenes/S.png"), (config.ESCALA, config.ESCALA)),
    # LUZ
    "L": pygame.transform.scale(pygame.image.load("imagenes/L.png"), (config.ESCALA, config.ESCALA)),
    # LIBRO VERDE /G
    "G": pygame.transform.scale(pygame.image.load("imagenes/G.png"), (config.ESCALA, config.ESCALA)),
    # MESA
    "T": pygame.transform.scale(pygame.image.load("imagenes/frame.png"), (config.ESCALA, config.ESCALA)),
    # LLAVE
    "K": pygame.transform.scale(pygame.image.load("imagenes/K.png"), (config.ESCALA, config.ESCALA))


}
