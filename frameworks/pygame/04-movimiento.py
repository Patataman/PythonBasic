# -*- coding: utf-8 -*-

import pygame, sys
from pygame import sprite       #Para generar y tratar los sprites correctamente
from pygame.locals import *     #Para gestionar eventos

#Antes de nada iniciamos pygame
pygame.init()

#Generamos una ventana donde poner nuestras cosas
ventana = pygame.display.set_mode((700,400))

#Necesario inicializar un reloj para realizar las actualizaciones
clock = pygame.time.Clock()


class Personaje(sprite.Sprite):     #Nuestro personaje hereda de la clase Sprite de Pygame
    
    def __init__(self):
        sprite.Sprite.__init__(self)        #Init de Sprite
        # Cargamos la hoja completa de sprites del personaje.
        # Se realiza convert_alpha() para que tenga en cuenta transparencias
        self.spriteSheet = pygame.image.load("sprites/sheet.png").convert_alpha()
        # "image" se corresponde con la imagen actual a mostrar. La hacemos más pequeña para que quede mejor
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0,200,420)),(100,200))
        self.rect = self.image.get_rect()       #Necesario para mostrar la imagen
        self.rect.center = (ventana.get_width()/2, ventana.get_height()/2)  #Donde se situa la imagen.

        self.frames = 4             #Número máximo de imágenes 
        self.current_frame = 0      #Frame actual
        self.frame_width = 100      #Anchura de la imagen
        self.frame_height = 200     #Altura dela imagen


    def update(self, ventana):       #Método heredado de la clase Sprite
        #Aquí es donde se realizarán las actualizaciones de la imagen.
        #Si se llega al límite de frames se reinicia
        if self.current_frame >= self.frames-1:
            self.current_frame = 0
        #Si no se llega, se sigue aumentando
        else:
            self.current_frame += 1
        #Se actualiza la imagen actual del personaje
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((self.current_frame*self.frame_width*2,0,200,420)),(self.frame_width,self.frame_height))

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
        self.rect.center = (self.rect.centerx+x, self.rect.centery+y)  #Donde se situa la imagen.


#Con esto ya tenemos todo lo básico para generar el sprite.

magickarp = Personaje()  #Creación del personaje
grupo_sprites = pygame.sprite.GroupSingle()
grupo_sprites.add(magickarp) 

while True:     #Bucle de "Juego"
    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa

        #Vamos a movernos sólo cuando se presione alguna tecla
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                for i in grupo_sprites:
                    i.mover(0,-100)
            if keys[K_a]:
                for i in grupo_sprites:
                    i.mover(-100,0)
            if keys[K_d]:
                for i in grupo_sprites:
                    i.mover(100,0)
            if keys[K_s]:
                for i in grupo_sprites:
                    i.mover(0,100)
     
    #Actualizacion de cosas
    ventana.fill((0, 0, 0))             #Limpieza de la pantalla
    grupo_sprites.update(ventana)       #Actualización de los elementos en el grupo
    grupo_sprites.draw(ventana)         #Dibujamos todo lo que hay en el grupo. En este caso a Magickarp
    pygame.display.flip()               #Actualiza la ventana

    clock.tick(6)