import pygame
from pygame.locals import *

class Escena:
    def __init__(self, director):
        self.director = director

    def eventos(self, evento):
        raise NotImplemented("Falta implementar eventos")

    def actualizar(self, t):
        raise NotImplemented("Falta implementar actualizar")

    def pintar(self, ventana):
        raise NotImplemented("Falta implementar pintar")

class Rojo(Escena):

    def __init__(self, director):
        Escena.__init__(self, director)

    def eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            teclas = pygame.key.get_pressed()
            if teclas[K_RETURN]:
                nueva_escena = Juego(self.director)
                self.director.cambiar_escena(nueva_escena)

    def actualizar(self, t):
        pass

    def pintar(self, ventana):
        ventana.fill((255,0,0))
        pygame.display.flip()


from newbola import Bola
from newpala import Pala

from camera import * #Camera, simple_camera, complex_camera

class Backgroung(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fondo.jpg")
        self.rect = self.image.get_rect()

class Punto(pygame.sprite.Sprite):

    def __init__(self, w, h, t):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Comic Sans", 64)
        self.image = self.font.render(str(t), True, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (w,h)

    def cambiar_text(self, t):
        self.image = self.font.render(str(t), True, (255,255,255))


class Juego(Escena):

    def __init__(self, director):
        self.director = director
        self.background = Backgroung()
        self.bola = Bola(1080/2, self.director.h/2)
        self.jugador = Pala(20, self.director.h/2, True)
        self.cpu = Pala(1060, self.director.h/2, True)
        self.group_bola = pygame.sprite.GroupSingle(self.bola)

        self.puntos1 = 0
        self.puntos2 = 0

        self.desplazamiento = 0
        self.desplazamiento2 = 0

        self.sonido_rebote = pygame.mixer.Sound("sonido.wav")
        self.sonido_fondo = pygame.mixer.Sound("sonido2.wav")

        self.camera = Camera(complex_camera, 1080, 600)

        self.p_pj = Punto(200,50,self.puntos1)
        self.p_cpu = Punto(800,50,self.puntos2)

        self.palas = pygame.sprite.Group(self.background, self.p_pj, self.p_cpu, self.jugador, self.cpu)

        self.sonido_fondo.play(-1)

        pygame.mouse.set_visible(0)

    def eventos(self, evento):
        self.desplazamiento = 0
        if evento.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[K_w]:
                self.desplazamiento = -250
            if keys[K_s]:
                self.desplazamiento = 250
            if keys[K_i]:
                self.desplazamiento2 = -250
            if keys[K_k]:
                self.desplazamiento2 = 250


    def actualizar(self, time):
        self.camera.follow(self.bola, self.director.w, self.director.h)

        self.comprobar_bola()
        
        self.group_bola.update()

        self.jugador.mover(self.desplazamiento*time, self.director.h)
        #self.cpu.mover(self.desplazamiento2, self.director.h)

        self.actualizar_cpu()

    def comprobar_bola(self):
        if self.bola.rect.centery >= self.director.h or \
            self.bola.rect.centery <= 0:
            self.bola.vel[1] *= -1

        if pygame.sprite.collide_rect(self.jugador, self.bola) or \
            pygame.sprite.collide_rect(self.cpu, self.bola):
            self.sonido_rebote.play()
            self.bola.vel[0] *= -1

        if self.bola.rect.centerx > 1080 or \
            self.bola.rect.centerx < 0:
            if self.bola.rect.centerx > 1080:
                self.p_pj.cambiar_text(self.puntos1+1)
                self.puntos1 += 1
            if self.bola.rect.centerx < 0:
                self.p_cpu.cambiar_text(self.puntos2+1)
                self.puntos2 += 1
            self.bola.reset(1080/2, self.director.h/2)

    def actualizar_cpu(self):
        if self.bola.rect.centery > self.cpu.rect.centery:
            self.cpu.rect.centery += 10
        if self.bola.rect.centery < self.cpu.rect.centery:
            self.cpu.rect.centery -= 10

    def pintar(self, ventana):
        ventana.fill((0,255,0))
        for e in self.palas:
            ventana.blit(e.image, self.camera.update(e))

        for e in self.group_bola:
            ventana.blit(e.image, self.camera.update(e))
        #self.group_bola.draw(ventana)
        #self.palas.draw(ventana)
        pygame.display.update()
