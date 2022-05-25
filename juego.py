import pygame
from jugador import Jugador
from estado_juego import EstadoJuego

class Juego:
    #Constructor por defecto.
    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.objetos = []
        self.estado_juego = EstadoJuego.NULO #Establecemos el juego como en el constructor por defecto.
    def configurar(self):#Esta funcion hace una configuracion inicial del juego, creando un Jugador localizado en el 1,1
        print("do set up")
        jugador = Jugador(1,1)
        self.jugador = jugador
        #Cargamos al jugador dentro de la lista de objetos
        self.objetos.append(jugador)
        self.estado_juego = EstadoJuego.CORRIENDO
    def actualizar(self):
        #Este es el constante actualizador
        #Ctemente esta fijandose si se actualizaron los datos del juego
        #Y luego renderizandolos
        print("do update")
        for objeto in self.objetos:
            objeto.render(self.pantalla) #Aca asumimos que todos los objetos 
                                #de esta lista tiene el metodo render()
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.estado_juego = EstadoJuego.TERMINADO
            elif event.type == pygame.KEYDOWN:
                #Si el jugador toca "Esc" el estado del juego cambia a termina.
                if event.key == pygame.K_ESCAPE:
                    self.estado_juego = EstadoJuego.TERMINADO
                elif event.key == pygame.K_w: #arriba
                    self.jugador.actualizar_posicion(0,-1)
                elif event.key == pygame.K_s: #abajo
                    self.jugador.actualizar_posicion(0,1)
                elif event.key == pygame.K_a: #izquierda
                    self.jugador.actualizar_posicion(-1,0)
                elif event.key == pygame.K_d: #derecha
                    self.jugador.actualizar_posicion(1,0)