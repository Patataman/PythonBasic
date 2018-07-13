import pygame
from pygame.locals import *

WIDTH = 800
HEIGHT = 600

class Director:

    def __init__(self):
        self.escena = None
        self.quit_flag = False
        self.ventana = pygame.display.set_mode([WIDTH, HEIGHT])
        self.w = WIDTH
        self.h = HEIGHT
        self.reloj = pygame.time.Clock()

    def change_flag(self):
        self.quit_flag = True

    def cambiar_escena(self, escena):
        self.escena = escena

    def loop(self):

        while not self.quit_flag:
            tiempo = self.reloj.tick(30)

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    teclas = pygame.key.get_pressed()

                    if teclas[K_ESCAPE]:
                        self.change_flag()

                if evento.type == pygame.QUIT:
                    self.change_flag()

                self.escena.eventos(evento)

            t_delta = tiempo / 1000
            self.escena.actualizar(t_delta)
            self.escena.pintar(self.ventana)
