# -*- coding: utf-8 -*-

# Módulos
from Scene import SceneHome
from Director import Director
import pygame
# ---------------------------------------------------------------------

def main():
	dir = Director()
	scene = SceneHome(dir)
	dir.change_scene(scene)
	dir.loop()
 
if __name__ == '__main__':
	pygame.init()
	main()
