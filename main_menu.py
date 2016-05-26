# -*- coding: utf-8 -*-
from utils import *


class Main_menu():
    def __init__(self,bck = None):
        self.current_screen = 0
        self.focusOnDialog = 0
        self.charSelect = 0
        self.loadSelect = 0
        self.diffSelect = 0
        self.screens = []
        screen_creation(self.screens)
        self.scr = self.screens[self.current_screen][self.focusOnDialog]

    def draw(self, index=0):
        if self.current_screen == len(self.screens):
            return
        #if self.current_screen == 0: TODO: Cambiar para transicion
        #    self.screens[self.current_screen][index].fadeInTransition()
        #else:
        self.scr.draw()
        display.update()

    def update(self):
        # TODO: Cambiar para transicion
        #if self.current_screen == 0:
        #    self.screens[self.current_screen][0].fadeOutTransition()

        if self.current_screen < len(self.screens):
            self.current_screen += 1
        if self.current_screen == len(self.screens):
            print "salgo",self.current_screen
            return

        print len(self.screens)
        print self.current_screen
        pos = self.screens[self.current_screen][self.focusOnDialog].pos
        import os
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (pos[0], pos[1])
        if self.current_screen <= 2:
            self.scr = self.screens[self.current_screen][self.focusOnDialog]
            self.scr.draw()
        elif self.current_screen == 3 and self.focusOnDialog == 0:
            self.scr = self.screens[self.current_screen][0]
            self.scr.draw()
        elif self.current_screen == 3 and self.focusOnDialog == 1:
            self.scr = self.screens[self.current_screen][1]
            self.scr.draw()


    def drawFocus(self):
        select = image.load("sprites/select.png")
        select = Surface.convert_alpha(select)
        if self.current_screen == 1:
            self.scr.draw()
            screen.blit(select, [400, 240 + 40 * self.focusOnDialog])
        elif self.current_screen == 2 and self.focusOnDialog == 0:
            self.scr.draw()
            screen.blit(select, [420, 280+80 * self.diffSelect])
        elif self.current_screen == 3 and self.focusOnDialog == 0:
            self.scr.draw()
            screen.blit(select, [280 + 400 * self.charSelect, 500])
        else:
            self.draw()

    def blink(self):
        dialogs = self.screens[self.current_screen][self.focusOnDialog].dialog
        dialogs[self.focusOnDialog].blinks()
