# -*- coding: utf-8 -*-

import pygame, sys
from pygame import sprite		#Para generar y tratar los sprites correctamente
from pygame.locals import *		#Para gestionar eventos

#Antes de nada iniciamos pygame
pygame.init()

#Generamos una ventana donde poner nuestras cosas
ventana = pygame.display.set_mode((700,400))


class Personaje(sprite.Sprite): 	#Nuestro personaje hereda de la clase Sprite de Pygame
	
	def __init__(self):
		sprite.Sprite.__init__(self)		#Init de Sprite
		# Cargamos la hoja completa de sprites del personaje.
		# Se realiza convert_alpha() para que tenga en cuenta transparencias
		self.spriteSheet = pygame.image.load("sprites/sheet.png").convert_alpha()
		# "image" se corresponde con la imagen actual a mostrar. La hacemos más pequeña para que quede mejor
		self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0,200,420)),(100,200))
		self.rect = self.image.get_rect()		#Necesario para mostrar la imagen
		self.rect.center = (ventana.get_width()/2, ventana.get_height()/2)	#Donde se situa la imagen.

	def update(self):		#Método heredado de la clase Sprite y que no vamos a usar
		pass

#Con esto ya tenemos todo lo básico para generar el sprite.


magickarp = Personaje()  #Creación del personaje
grupo_sprites = pygame.sprite.GroupSingle()
grupo_sprites.add(magickarp) 

while True:     #Bucle de "Juego"
    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa
     
    #Actualizacion de cosas
    grupo_sprites.draw(ventana)			#Dibujamos todo lo que hay en el grupo. En este caso a Magickarp
    pygame.display.flip()               #Actualiza la ventana