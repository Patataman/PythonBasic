''' Una forma muy común de organizar juegos es por escenas.

    El juego comienza en 1 pantalla, ocurre algún evento y se
    avanza a otra ventana. Es un modelo muy común y que se sigue
    usando hoy en día, además de sencillo de entender.

    Tenemos un "Director" que se encarga de ejecutar "Escenas".
    Una "Escena" es la pantalla que se está viendo y ejecutando
    en el momento actual.

    El ejemplo más sencillo es: Iniciamos el juego y tenemos la
    pantalla de presentación, con un título y el típico "Press Start".
    Esto es una escena y en el momento qe presionemos "Start", se 
    cargará otra escena nueva y el "Director" sustituirá la pantalla
    actual con la nueva escena.
'''

''' Paso 1. Definir el Director
'''

import pygame
from pygame.locals import *

class Director:
    '''Representa el objeto principal del juego.
    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.
    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene.'''

    def __init__(self):
        ''' En el init establecemos las características globales como
            resolución, título de la ventana, etc"
        '''
        self.screen = pygame.display.set_mode([800,600])
        pygame.display.set_caption("Estamos haciendo escenas")
        self.scene = None       #Escena actual
        self.quit_flag = False  #Control para el bucle de juego
        self.clock = pygame.time.Clock()

    def loop(self):
        ''' Bucle de juego'''
        while not self.quit_flag:
            time = self.clock.tick(60)  #PCMaster Race

            # Eventos que capturamos en cada momento
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                    break

                ''' Si el juego no se ha cancelado,
                    le tenemos que pasar a la escena actual
                    los eventos capturados para sus cosas
                '''
                self.scene.on_event(time, event)
            
            # actualiza la escena
            self.scene.on_update(time)

            # dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        '''Altera la escena actual'''
        self.scene = scene

    def quit(self):
        '''Para cuando queremos salir'''
        self.quit_flag = True

''' Paso 2. Definir la clase Escena
'''

class Scene:
    '''Representa un escena abstracta del videojuego.
 
    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones. Esta clase servirá como
    estructura para poder crear luego nuestras propias escenas
    '''
 
    def __init__(self, director):
        #Contiene el director para poder acceder a cosas como
        #el reloj o la pantalla
        self.director = director
 
    def on_update(self, time):
        ''' Actualización lógica que se llama automáticamente desde el director
        '''
        raise NotImplemented("Tiene que implementar el método on_update.")
 
    def on_event(self, time, event):
        ''' Se llama cuando llega un evento especifico al bucle
            Le pasamos también la variable "time" por que para
            actualizaciones de movimiento, etc nos vendrá bien
        '''
        raise NotImplemented("Tiene que implementar el método on_event.")
 
    def on_draw(self, screen):
        ''' Se llama cuando se quiere dibujar la pantalla
        '''
        raise NotImplemented("Tiene que implementar el método on_draw.")


''' Ya tenemos nuestro director y escena definidos, ahora ya podemos
    crear cosas.

    Paso 3. Crear escenas y "rellenarlas"
'''

class Pantalla1(Scene):
    ''' Esta pantalla va a tener el color azul.
        Cuando se presione la tecla "Enter" lo que
        se va a hacer es cambiar de escena a "Pantalla2"
    '''
    def __init__(self, director):
        Scene.__init__(self, director)

    def on_update(self, time):
        pass

    def on_event(self, time, event):
        ''' El director pasa aquí los eventos que ha captado
        '''
        if event.type == KEYDOWN:   #Si el usuario ha presionado una tecla
            #Recuperamos las teclas presionadas
            keys = pygame.key.get_pressed()
            if keys[K_RETURN]:  #Presiona la tecla de "Enter":
                #Creamos la nueva escena y le decimos 
                # al director que ahora queremos esa
                self.director.change_scene(Pantalla2(self.director))

    def on_draw(self, screen):
        #se pone la pantalla de color azul
        screen.fill((0,0,255))

class Pantalla2(Scene):
    ''' Esta pantalla va a tener el color rojo.
        Por lo demás, es casi idéntica a la Pantalla1
    '''
    def __init__(self, director):
        Scene.__init__(self, director)

    def on_update(self, time):
        pass

    def on_event(self, ime, event):
        ''' El director pasa aquí los eventos que ha captado
        '''
        if event.type == KEYDOWN:   #Si el usuario ha presionado una tecla
            #Recuperamos las teclas presionadas
            keys = pygame.key.get_pressed()
            if keys[K_BACKSPACE]:  #Presiona la tecla de "Retroceso":
                #Aquí vamos a volver a Pantalla1, así hacemos un bucle
                self.director.change_scene(Pantalla1(self.director))

    def on_draw(self, screen):
        #se pone la pantalla de color rojo
        screen.fill((255,0,0))


''' Paso 4, poner todo junto.

    Ya hemos definido nuestro Director y Escenas, ahora toca
    crear todo e instanciar cosas.
'''

#Creamos el director
director = Director()
#Creamos la instancia de la escena
scene = Pantalla1(director)
#Le decimos al director la escena que ejecutará
director.change_scene(scene)
#Y ponemos en marcha el juego!
director.loop()