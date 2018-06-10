# -*- coding: utf-8 -*-

import pygame, sys
from Director import Director
from Selector import Selector
from pygame.locals import *

HEIGHT = 768
WIDTH = 1024


class Scene:
    """Representa un escena abstracta del videojuego.
 
    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones. Tiene que crear un objeto
    derivado de esta clase para crear una escena utilizable."""
 
    def __init__(self, director):
        self.director = director

    def on_update(self, time):
        "Actualización lógica que se llama automáticamente desde el director."
        raise NotImplemented("Tiene que implementar el método on_update.")

    def on_event(self, event):
        "Se llama cuando llega un evento especifico al bucle."
        raise NotImplemented("Tiene que implementar el método on_event.")

    def on_draw(self, screen):
        "Se llama cuando se quiere dibujar la pantalla."
        raise NotImplemented("Tiene que implementar el método on_draw.")

def colorear(args):
    #args = (screen, color)
    args[0].fill(args[1])

class SceneHome(Scene):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""


    def __init__(self, director):
        Scene.__init__(self, director)

        self.rueda = Selector(self.director.screen, (WIDTH/2, HEIGHT/2))

        self.rueda.asociateEvent(0, colorear, self.director.screen,(255,0,0))
        self.rueda.asociateEvent(1, colorear, self.director.screen,(0,0,255))
        self.rueda.asociateEvent(2, colorear, self.director.screen,(0,255,0))
        self.rueda.asociateEvent(3, colorear, self.director.screen,(0,0,0))
        self.rueda.setIcon(0, "images/icon1.png")
        self.rueda.setIcon(1, "images/icon2.png")
        self.rueda.setIcon(2, "images/icon3.png")
        self.rueda.setIcon(3, "images/icon4.png")


    def on_update(self):
        pass

    def on_event(self, event):
        #Al pulsar una tecla...
        if pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            self.rueda.on_event_keys(keys)

        if pygame.mouse.get_pressed()[0]:
            self.rueda.on_event_mouse(pygame.mouse.get_pos())

    def on_draw(self, screen):
        #screen.fill((0, 0, 0))    Comentado por que la función consiste en pintar la pantalla
        self.rueda.draw()