''' Este post de stackoverflow es muy bueno (votadlo positivo si tenéis cuenta xD)
    https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame/14357169#14357169

    A grandes rasgos cuando un juego implementa una cámara que se va moviendo
    por el escenario, lo que se hace es "fijar" un objeto y desplazar todos los
    demás elementos en dirección contraria tanto como se mueva el objeto fijado.

    Ej: Fijo a mi pj que está en el medio de la pantalla. Si lo muevo 5px a la
    derecha, el resto de elementos los moveré 5px a la izquierda para dar la
    sensación de movimiento.

    Mi idea original era hacerlo con grupos, pero la aproximación de esta buena
    persona es más sencilla e igualmente válida.
'''

from pygame import sprite       #Para generar y tratar los sprites correctamente
from pygame.locals import *     #Para gestionar eventos

import pygame
import sys

WIDTH = 800
HEIGHT = 600
TOTAL_WIDTH = 1000
TOTAL_HEIGHT = 700

pygame.init()

ventana = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hacemos cosas con cámaras!")

''' Misma clase para Magikarp '''
class Magikarp(sprite.Sprite):     #Nuestro personaje hereda de la clase Sprite de Pygame

    def __init__(self):
        #Init de Sprite
        sprite.Sprite.__init__(self)

        self.spriteSheet = pygame.image.load("sprites/sheet.png").convert_alpha()
        # "image" se corresponde con la imagen actual a mostrar.
        #La hacemos más pequeña para que quede mejor
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0,200,420)),(100,200))
        #Necesario para mostrar la imagen
        self.rect = self.image.get_rect()
        #Donde se situa la imagen.
        self.rect.center = (TOTAL_WIDTH/2, TOTAL_HEIGHT/2)

        self.speed = 10     #Se va a mover 10px en la dirección que sea

        self.frames = 4             #Número máximo de imágenes
        self.current_frame = 0      #Frame actual
        self.frame_width = 100      #Anchura de la imagen
        self.frame_height = 200     #Altura dela imagen


    #Método heredado de la clase Sprite
    def update(self, dt, ventana):
        if self.current_frame >= self.frames-1:
            self.current_frame = 0
        #Si no se llega, se sigue aumentando
        else:
            #Hacemos x3 por que queremos que salgan 3 imágenes por segundo
            self.current_frame += 3*dt

        self.image = pygame.transform.scale(
            self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width*2,0,200,420)),
            (self.frame_width,self.frame_height))

    def mover(self, x=0, y=0):
        #Comprobación para no salirnos del mapa
        if self.rect.centerx+x >= TOTAL_WIDTH or self.rect.centerx+x < 0:
            return
        #Comprobación para no salirnos del mapa
        if self.rect.centery+y >= TOTAL_HEIGHT or self.rect.centery+y < 0:
            return
        #Si el movimiento está dentro de los límites de la pantalla,
        #se "recoloca" el centro de la imagen
        self.rect.center = (self.rect.centerx+x, self.rect.centery+y)

''' Definición de nuestra clase cámara, con la que haremos
    la bujería para enfocar al jugador y mover el resto del
    mundo
'''
class Camera(object):
    ''' Camera_func es el tipo de "seguir" que vamos
        a hacer sobre el objeto.
        Width y Height, tamaño total del mapa/escena, es decir,
        si nuestra ventana es de 800x600 pero la escena de 1000x700,
        pues ponemos 1000x700
    '''
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    ''' Sobre qué objeto vamos a realizar el seguimiento.
        Se puede cambiar "en vivo"
    '''
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    ''' Función a la que llamamos a la hora de hacer "update"
        para desplazar el resto del mundo con respecto
        a nuestro "objetivo".
    '''
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

''' Cámara que sigue al objetivo, pero le
    dan igual los límites de la ventana
'''
def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+WIDTH//2, -t+HEIGHT//2, w, h)

''' Cámara que sigue al objetivo, pero tiene en 
    cuenta los límites de la ventana
'''
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+WIDTH//2, -t+HEIGHT//2, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)



camera = Camera(complex_camera, TOTAL_WIDTH,TOTAL_HEIGHT)
#Personaje al que va a seguir la cámara
main_pj = Magikarp()
#Lo coloco fuera de la vista inicial
otro_pj = Magikarp()
otro_pj.rect.centerx = 900
otro_pj.rect.centery = 450
#Grupo donde irán el resto de elementos
ingame_elements = pygame.sprite.Group()
ingame_elements.add(otro_pj)
ingame_elements.add(main_pj)

clock = pygame.time.Clock()

''' Bucle de juego'''
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

        #Vamos a movernos sólo cuando se presione alguna tecla
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            pixels_v = -main_pj.speed
        if keys[K_a]:
            pixels_h = -main_pj.speed
        if keys[K_d]:
            pixels_h = main_pj.speed
        if keys[K_s]:
            ''' También podemos modificar el personaje de forma
                individual, aunque dado que los grupos van a "agrupar"
                cosas que van juntas lo suyo sería hacerlo con los grupos
            '''
            pixels_v = main_pj.speed

    #Actualizacion de cosas
    ventana.fill((255, 255, 0))             #Limpieza de la pantalla

    camera.update(main_pj)

    main_pj.mover(pixels_h,pixels_v)
    ingame_elements.update(dt, ventana)
    for e in ingame_elements:
        ventana.blit(e.image, camera.apply(e))

    pygame.display.update()