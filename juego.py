import pygame
from player import Player
from estado_juego import EstadoJuego

class Juego:
    #Constructor por defecto.
    def __init__(self,screen):
        self.screen = screen
        self.objetos = []
        self.estado_juego = EstadoJuego.NULO
    def set_up(self):
        print("do set up")
        jugador = Player(1,1)
        self.jugador = jugador
        #Cargamos al jugador dentro de la lista de objetos
        self.objetos.append(jugador)
        self.estado_juego = EstadoJuego.CORRIENDO
    def update(self):
        print("do update")
        for objeto in self.objetos:
            objeto.render(self.screen) #Aca asumimos que todos los objetos 
                                #de esta lista tiene el metodo render()
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.estado_juego = EstadoJuego.TERMINADO
            elif event.type == pygame.KEYDOWN:
                #If "Esc" el estado del juego termina.
                if event.key == pygame.K_ESCAPE:
                    self.estado_juego = EstadoJuego.TERMINADO
                elif event.key == pygame.K_w: #up
                    self.jugador.actualizar_posicion(0,-1)
                elif event.key == pygame.K_s: #down
                    self.jugador.actualizar_posicion(0,1)
                elif event.key == pygame.K_a: #left
                    self.jugador.actualizar_posicion(-1,0)
                elif event.key == pygame.K_d: #right
                    self.jugador.actualizar_posicion(1,0)