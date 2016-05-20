from utils import *


class Main_menu():
    def __init__(self,bck = None):
        global screen
        self.current_screen = 0
        self.focusOnDialog = 0
        self.screens = []
        screen_creation(self.screens)

    def draw(self):
        self.screens[self.current_screen][self.focusOnDialog].draw()

    def update(self):
        if self.current_screen < len(self.screens):
            self.current_screen += 1
        if self.current_screen == len(self.screens):
            return
        pos = self.screens[self.current_screen][self.focusOnDialog].pos
        import os
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (pos[0], pos[1])
        self.screens[self.current_screen][self.focusOnDialog].draw()

    def blink(self):
        dialogs = self.screens[self.current_screen][self.focusOnDialog].dialog
        dialogs[self.focusOnDialog].blinks()
