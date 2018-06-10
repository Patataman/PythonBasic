import pygame

class Bola(pygame.sprite.Sprite):

    def __init__(self, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [w,h]
        self.vel = [10,10]   #x, y

    def update(self):
        self.rect.centerx += self.vel[0]
        self.rect.centery += self.vel[1]

    def reset(self, w, h):
        self.rect.center = [w,h]
        self.vel = [10,10]   #x, y

    #Lo ignoramos por usar luego Group()
    #def draw(self, ventana):
    #    ventana.blit(ventana, self.image)
