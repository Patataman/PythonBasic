import pygame

from newdirector import Director
from newescena import Rojo

pygame.mixer.pre_init(44100, -16, 1, 2048)
pygame.mixer.init()

pygame.init()

pepe = Director()
rojo = Rojo(pepe)

pepe.cambiar_escena(rojo)
pepe.loop()
