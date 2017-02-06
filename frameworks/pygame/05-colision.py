# -*- coding: utf-8 -*-

import pygame, sys
from pygame import sprite		#Para generar y tratar los sprites correctamente
from pygame.locals import *		#Para gestionar eventos

#Antes de nada iniciamos pygame
pygame.init()

#Generamos una ventana donde poner nuestras cosas
ventana = pygame.display.set_mode((700,400))

while True:     #Bucle de "Juego"
    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa
     
    #Actualizacion de cosas
    pygame.display.flip()               #Actualiza la ventana