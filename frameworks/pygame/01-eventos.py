#Necesario para las teclas presionadas
from pygame.locals import *
#Import del paquete
import pygame
import sys

#se inicializa
pygame.init()

ventana = pygame.display.set_mode((700,400))

#Bucle de "Juego"
while True:
    ''' Documentación relacionado con los eventos:
        https://www.pygame.org/docs/ref/event.html
    '''
    #Obtenemos todos los eventos que ocurren en este momento
    for event in pygame.event.get():
        '''
            Hasta aqui todo era exactamente igual que en el ejemplo anterior.

            En este ejemplo vamos a hacer que se modifique el color de fondo
            cuando se pulsen algunas teclas en concreto.
        '''
        #Cuando el evento es presionar una tecla...
        if event.type == pygame.KEYDOWN:
            #Obtenemos el mapping de teclas presionadas
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                #Rellenamos la ventana con un color de Pygame
                ventana.fill(pygame.Color("blue"))
            if keys[K_a]:
                ventana.fill(pygame.Color("red"))
            if keys[K_d]:
                ventana.fill(pygame.Color("green"))

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
