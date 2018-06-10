from pygame import draw, image
from pygame.locals import *
import math

class Selector():

    def __init__(self, screen, position, number_of=4, color=(255,255,255)):
        self.screen = screen                      #screen
        self.number_of = number_of                #number of selectors
        self.secciones_rect = []                  #rect for each selector
        self.puntosExteriores = []                #exterior points of the circle
        self.puntosInteriores = []                #inner points of the circle
        self.funciones = [None]*number_of         #functions for each selector
        self.images = [None]*number_of            #icons for each selector

        #Number of selector * 4 to give some shape.
        for i in range(0, number_of*4):
            # x = r * cos(t)
            # y = r * sen(t)
            self.puntosExteriores.append([self.screen.get_width()/3*math.cos(math.radians(360/(4*number_of)*i))+position[0],
                                  self.screen.get_width()/3*math.sin(math.radians(360/(4*number_of)*i))+position[1]])
            self.puntosInteriores.append([(self.screen.get_width()/10-20)*math.cos(math.radians(360/(4*number_of)*i))+position[0],
                                  (self.screen.get_width()/10-20)*math.sin(math.radians(360/(4*number_of)*i))+position[1]])

    """Call it when you want to draw the selector
    """
    def draw(self):
        self.secciones_rect.clear()
        for i in range(0,self.number_of*4,4):
            self.secciones_rect.append(draw.polygon(self.screen, (255-i*20,255-i*20,255-i*20),
                                            [self.puntosExteriores[(i+4)%(self.number_of*4)],
                                            self.puntosExteriores[i+3],
                                            self.puntosExteriores[i+2], 
                                            self.puntosExteriores[i+1],
                                            self.puntosExteriores[i],
                                            self.puntosInteriores[i],
                                            self.puntosInteriores[i+1],
                                            self.puntosInteriores[i+2],
                                            self.puntosInteriores[i+3],
                                            self.puntosInteriores[(i+4)%(self.number_of*4)]], 0))

        for i in range(0, len(self.images)):
            if i is not None:
                img_rect = self.images[i].get_rect()
                img_rect.center = self.secciones_rect[i].center
                self.screen.blit(self.images[i],img_rect)

    #on_event with mouse
    """Call it when you want activate the functions doing click on the selector

    mouse_position: returned value of `pygame.mouse.get_pos()`
    """
    def on_event_mouse(self, mouse_position):
        if mouse_position[0]:
            for i in range(0,self.number_of):
                if self.secciones_rect[i].collidepoint(mouse_position) and \
                    self.funciones[i] != None:
                    
                    self.funciones[i]()
                    return True

    #on_event with keys
    """Call it when you want activate the functions using the keyboard

    keys: returned value of `pygame.key.get_pressed()`
    """
    def on_event_keys(self, keys):
        if keys[K_UP]:
            if self.funciones[0] != None:
                self.funciones[0]()
        elif keys[K_RIGHT]:
            if self.funciones[1] != None:
                self.funciones[1]()
        elif keys[K_DOWN]:
            if self.funciones[2] != None:
                self.funciones[2]()
        elif keys[K_LEFT]:
            if self.funciones[3] != None:
                self.funciones[3]()

    """Use it to asociate functions for each selector

    selector: int. Represent the selector
    event: function name
    *args: event's args
    return: True with success, False if selector is wrong
    """
    def asociateEvent(self, selector, event, *args):
        if selector > self.number_of or selector < 0:
            return False

        self.funciones[selector] = lambda: event(args)
        return True

    """Use it to place icons in the center of each selector

    selector: int. Represent the selector
    image_path: path to the image
    return: True with success, False if selector is wrong
    """
    def setIcon(self, selector, image_path):
        if selector > self.number_of or selector < 0:
            return False

        image_surface = image.load(image_path)
        self.images[selector] = image_surface
        return True