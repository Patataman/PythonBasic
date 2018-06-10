import pygame
from pygame.locals import *

class Pala(pygame.sprite.Sprite):

    def __init__(self, w, h, is_player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,100])
        self.image.fill([255,255,255])
        self.rect = self.image.get_rect()
        self.rect.center = [w,h]
        self.is_player = is_player

    def mover(self, despl, max_altura):
        if self.rect.centery + despl >= 0 and \
            self.rect.centery + despl <= max_altura:
            self.rect.centery += despl
