import pygame, sys  #Import del paquete
from pygame.locals import *     #Necesario para las teclas presionadas

pygame.init()       #se inicializa

ventana = pygame.display.set_mode((700,400))

while True:     #Bucle de "Juego"
    for event in pygame.event.get():    #Cuando ocurre un evento...
        #Hasta aqui todo era exactamente igual que en el ejemplo anterior
        #En este ejemplo vamos a hacer que se modifique el color de fondo
        #cuando se pulsen algunas teclas en concreto.
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                ventana.fill(pygame.Color("blue"))
            if keys[K_a]:
                ventana.fill(pygame.Color("red"))
            if keys[K_d]:
                ventana.fill(pygame.Color("green"))

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()