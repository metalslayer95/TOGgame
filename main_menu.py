# -*- coding: utf-8 -*-
from utils import *


class Main_menu():
    def __init__(self,bck = None):
        self.current_screen = 0
        self.focusOnDialog = 0
        self.screens = []
        screen_creation(self.screens)

    def draw(self, index = 0):
        print "Drawing,",self.current_screen,len(self.screens)
        if self.current_screen == len(self.screens):
            return
        #if self.current_screen == 0: TODO: Cambiar para transicion
        #    self.screens[self.current_screen][index].fadeInTransition()
        #else:
        self.screens[self.current_screen][index].draw()
        display.update()

    def update(self):
        # TODO: Cambiar para transicion
        #if self.current_screen == 0:
        #    self.screens[self.current_screen][0].fadeOutTransition()
        if self.current_screen < len(self.screens):
            self.current_screen += 1
        if self.current_screen == len(self.screens):
            return
        pos = self.screens[self.current_screen][self.focusOnDialog].pos
        import os
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (pos[0], pos[1])
        print self.focusOnDialog
        self.screens[self.current_screen][self.focusOnDialog].draw()
        #self.focusOnDialog = 0

    def drawFocus(self):
        select = image.load("sprites/select.png")
        select = Surface.convert_alpha(select)
        self.draw()
        if self.current_screen == 1:
            screen.blit(select,[450,340+40*self.focusOnDialog])
        elif self.current_screen == 2 :
            screen.blit(select,[450,340+80*self.focusOnDialog])

    def blink(self):
        dialogs = self.screens[self.current_screen][self.focusOnDialog].dialog
        dialogs[self.focusOnDialog].blinks()
