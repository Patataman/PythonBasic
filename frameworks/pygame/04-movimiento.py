
from pygame import sprite       #Para generar y tratar los sprites correctamente
from pygame.locals import *     #Para gestionar eventos

import pygame
import sys

pygame.init()

ventana = pygame.display.set_mode((700,400))

#El reloj interno nos valdrá para realizar las actualizaciones de sprite
# o movimiento. https://www.pygame.org/docs/ref/time.html
clock = pygame.time.Clock()

''' Documentación sobre sprites
    https://www.pygame.org/docs/ref/sprite.html

    Principalmente los sprites están compuestos de una imagen
    y posteriormente de un objeto Rect (https://www.pygame.org/docs/ref/rect.html)
    que utiliza Pygame para situarlo dentro de la pantalla y otras cosas
    como colisiones, etc
'''
class Personaje(sprite.Sprite):     #Nuestro personaje hereda de la clase Sprite de Pygame

    def __init__(self):
        #Init de Sprite
        sprite.Sprite.__init__(self)
        ''' Cargamos la hoja completa de sprites del personaje.
            Se realiza convert_alpha() para que tenga en cuenta transparencias (capa alpha)
        '''
        self.spriteSheet = pygame.image.load("sprites/sheet.png").convert_alpha()
        # "image" se corresponde con la imagen actual a mostrar.
        #La hacemos más pequeña para que quede mejor
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0,200,420)),(100,200))
        #Necesario para mostrar la imagen
        self.rect = self.image.get_rect()
        #Donde se situa la imagen.
        self.rect.center = (ventana.get_width()/2, ventana.get_height()/2)

        self.speed = 10     #Se va a mover 10px en la dirección que sea

        ''' Variables para nuestro control del sprite
        '''
        self.frames = 4             #Número máximo de imágenes
        self.current_frame = 0      #Frame actual
        self.frame_width = 100      #Anchura de la imagen
        self.frame_height = 200     #Altura dela imagen


    #Método heredado de la clase Sprite
    def update(self, dt, ventana):
        ''' Aquí es donde se realizarán las actualizaciones del personaje.
            Es decir, movimiento, cambios en el sprite, cambios
            de atributos como puede ser la vida...

            En este caso, si se llega al límite de frames se reinicia.
            De esta forma estará animándo siempre en bucle.
        '''
        if self.current_frame >= self.frames-1:
            self.current_frame = 0
        #Si no se llega, se sigue aumentando
        else:
            #Hacemos x3 por que queremos que salgan 3 imágenes por segundo
            self.current_frame += 3*dt

        ''' Una vez actualizados los frames, se actualiza la imagen actual del personaje.

            Para ello, realizamos el mismo recorte que antes, pero la diferencia
            principal ahora es que la imagen que se recorta, va a
            depender del frame (momento actual) en el que nos situemos.
        '''
        self.image = pygame.transform.scale(
            self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width*2,0,200,420)),
            (self.frame_width,self.frame_height))

    #######################################
    ###### HASTA AQUÍ ERA TODO IGUAL ######
    ###### PERO TODO CAMBIÓ CUANDO LA #####
    ###### LA NACIÓN DEL FUEGO ATACÓ ######
    #######################################

    '''
    Método para mover el personaje. Por defecto, si no pones valor a X e Y, no se mueve.
    X e Y pueden ser tanto positivas (moverse a la drch o arriba) como negativas (izq o abajo)
    '''
    def mover(self, x=0, y=0):
        #Comprobación para no salirnos del mapa
        if self.rect.centerx+x >= ventana.get_width() or self.rect.centerx+x < 0:
            return
        #Comprobación para no salirnos del mapa
        if self.rect.centery+y >= ventana.get_height() or self.rect.centery+y < 0:
            return
        #Si el movimiento está dentro de los límites de la pantalla,
        #se "recoloca" el centro de la imagen
        self.rect.center = (self.rect.centerx+x, self.rect.centery+y)

#Con esto ya tenemos todo lo básico para generar el sprite.
magikarp = Personaje()  #Creación del personaje
speed = magikarp.speed
grupo_sprites = pygame.sprite.GroupSingle()
grupo_sprites.add(magikarp)


while True:     #Bucle de "Juego"
    ''' Esto significa que se van realizan 30
        actualizaciones del juego por segundo.

        Es necesario hacerlo en cada iteración
        por que si no se reinicia
    '''
    dt = clock.tick(30) / 1000
    pixels_h = pixels_v = 0

    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa

        #Vamos a movernos cuando se presione las teclas W, A, D y S

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            #Se deja el movimiento de pixels_v o pixels_h en cero para evitar movimiento diagonales
            pixels_v = -speed
            pixels_h = 0
        if keys[K_a]:
            pixels_v = 0
            pixels_h = -speed
        if keys[K_d]:
            pixels_v = 0
            pixels_h = speed
        if keys[K_s]:
            ''' También podemos modificar el personaje de forma
                individual, aunque dado que los grupos van a "agrupar"
                cosas que van juntas lo suyo sería hacerlo con los grupos
            '''
            pixels_v = speed
            pixels_h = 0

    for i in grupo_sprites:
        i.mover(pixels_h,pixels_v)

    #Actualizacion de cosas
    ventana.fill((0, 0, 0))             #Limpieza de la pantalla
    grupo_sprites.update(dt, ventana)       #Actualización de los elementos en el grupo
    grupo_sprites.draw(ventana)         #Dibujamos todo lo que hay en el grupo. En este caso a Magickarp
    pygame.display.update()               #Actualiza la ventana