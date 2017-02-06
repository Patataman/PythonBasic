import pygame, sys   #Import del paquete

pygame.init()  #se inicializa

ventana = pygame.display.set_mode((700,400))
pygame.display.set_caption("Titulo de ventana") #podemos ponerle titulo a nuestra ventana

while True:     #Bucle de "Juego"
    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa
                
    pygame.display.flip()               #Genera la ventana