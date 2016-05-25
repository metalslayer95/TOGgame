# -*- coding: utf-8 -*-
from context import *


class Pause_menu():

    def __init__(self):
        cfdialog = Dialog("Configurar teclado", [350, 300], None, 20)
        adialog = Dialog("  Ayuda", [400, 380], None, 20)
        sdialog = Dialog("  Salir", [400, 460], None, 20)
        screen1 = Screen("", (1024,700), (300,200), [cfdialog, adialog, sdialog], [], path + "/.tmp/game.png")
        self.screens = []
        self.screens.append(screen1)
        self.focusOnDialog = 0
        self.current_screen = 0

    def update(self):
        if self.focusOnDialog == 0:
            pass
        elif self.focusOnDialog == 1:
            pass
        elif self.focusOnDialog == 2:
            salir()

    def paused(self, state=None):
        while True:
                for ev in event.get():
                    if ev.type == QUIT:
                        display.quit()
                        quit()
                        return
                    if ev.type == KEYDOWN:
                        if ev.key == K_p:
                            state.current_screen = 2
                            state.draw(state.focusOnDialog)
                            self.focusOnDialog = 0
                            display.update()
                            return
                        elif ev.key == K_UP and self.focusOnDialog > 0:
                            self.focusOnDialog -= 1
                        elif ev.key == K_DOWN and self.focusOnDialog < 2:
                            self.focusOnDialog += 1
                        elif ev.key == K_RETURN:
                            self.update()
                    self.screens[self.current_screen].draw()
                    self.drawFocus()
                    display.update()
                    clock.tick(60)

    def drawFocus(self):
            select = image.load("sprites/select.png")
            screen.blit(select,[450,340+80*self.focusOnDialog])


class Screen:
    def __init__(self, img="", size=(), pos=(), dialog=None, addin=[], tmpImg=""):
        global screen
        if img != "":
            self.background = image.load(img)
        else:
            self.tmpImg = image.load(tmpImg)
            self.tmpImg.set_alpha(128)
            self.background = None
        self.screen_size = size
        self.pos = pos
        self.dialog = dialog

    def draw(self,addin = []):
        screen = display.set_mode(self.screen_size)
        print self.background, "background"
        if self.background != None:
            screen.blit(self.background,[0,0])
        else:
            screen.fill(BLACK)
            screen.blit(self.tmpImg,[0,0])
            display.update()
        dlg = self.dialog
        if dlg is not None and dlg != []:
            for d in dlg:
                d.draw()
        if addin == []:
            return
        else:
            for adds in addin:
                screen.blit(adds[0],adds[1])

    def fadeInTransition(self):
        screen = display.set_mode(self.screen_size)
        for i in range(0,255,2):
            for ev in event.get():
                if ev.type == QUIT:
                    display.quit()
                    quit()
                    return
                if ev.type == KEYDOWN:
                        self.background.set_alpha(255)
                        self.draw()
                        return
            self.background.set_alpha(i)
            screen.fill((0, 0, 0))
            screen.blit(self.background, [0, 0])
            time.delay(20)
            display.update()
        self.draw()

    def fadeOutTransition(self):
        screen = display.set_mode(self.screen_size)
        for i in range(255,0,-2):
            for ev in event.get():
                if ev.type == QUIT:
                    display.quit()
                    quit()
                    return
                if ev.type == KEYDOWN:
                    self.background.set_alpha(0)
                    self.draw()
                    return
            self.background.set_alpha(i)
            screen.fill((0, 0, 0))
            screen.blit(self.background, [0, 0])
            time.delay(20)
            display.update()

class Dialog():
    def __init__(self, text = "",  pos = [cx, cy], bck = None,scale = 15):
        if bck is not None:
            background = image.load(bck)
            screen.blit(background,pos)
        self.pos = pos
        self.text = text
        self.message = []
        self.scale = scale
        self.analize()
        self.blink = scale

    def __repr__(self):
        return self.text

    def analize(self):
        for l in self.text:
            if l != " " and l != "-" :
                letter = image.load("sprites/letters/"+l+".png")
                letter = transform.scale(letter, (self.scale, self.scale))
                self.message.append(letter)
            else:
                self.message.append(l)

    def draw(self):
        new_pos = (self.pos[0] + self.scale, self.pos[1] + self.scale)
        for img in self.message:
            if img == " ":
                new_pos = (new_pos[0] + self.scale, new_pos[1])
            elif img == "-":
                new_pos = (self.pos[0] + self.scale, new_pos[1] + self.scale + 10)
            else:
                screen.blit(img, new_pos)
                new_pos = (new_pos[0] + self.scale, new_pos[1])

    def blinks(self):
        new_pos = (self.pos[0] + self.scale - self.blink, self.pos[1] + self.scale)
        self.message = []
        self.analize()
        copy = self.message
        for i in range(len(copy)):
            img = copy[i]
            if img == " ":
                new_pos = (new_pos[0] + self.blink, new_pos[1])
            else:
                copy[i] = transform.scale(copy[i], (self.blink, self.blink))
                screen.blit(copy[i], new_pos)
                new_pos = (new_pos[0] + self.blink, new_pos[1])
        if self.blink > (self.scale + 5):
            self.blink = self.scale
        else:
            self.blink = self.blink + 1
        print "blinkeo con",self.blink


def salir():
    # TODO: implementacion sqlite
    display.quit()
    quit()
    exit()

def screen_creation(screens = []):
        dialog = Dialog("Presione una tecla para continuar", [250, 303], None, 10)
        scr = Screen(path + "/sprites/starting_screen.jpg",(778,405),(300,200), [dialog],[])
        screens.append([scr])
        ngdialog = Dialog("Nuevo juego", [400, 300],None, 20)
        lgdialog = Dialog("Cargar juego", [400, 340],None, 20)
        pvpdialog = Dialog("  Versus", [400, 380],None, 20)
        hdialog = Dialog("  Ayuda", [400, 420],None, 20)
        cdialog = Dialog(" Creditos", [400, 460],None, 20)
        scr2 = Screen(path + "/sprites/main_menu_screen.jpg", (1024, 700), (200, 25), [ngdialog, lgdialog, pvpdialog, hdialog, cdialog], [])
        screens.append([scr2])
        j1dialog = Dialog("Juego facil",[400,300],None,20)
        j2dialog = Dialog("Juego normal",[400,380],None,20)
        j3dialog = Dialog("Juego dificil",[400,460],None,20)
        scr3 = Screen(path + "/sprites/main_menu_screen.jpg", (1024, 700), (200, 25), [j1dialog,j2dialog,j3dialog], [])
        p1 = Dialog("Personaje a nivel X",[400,300],None,20)
        p2 = Dialog("Personaje b nivel Y",[400,380],None,20)
        scr4 = Screen("sprites/main_menu_screen.jpg", (1024, 700), (200, 25), [p1,p2], [])
        d = Dialog("Modo versus en desarrollo",[400,300],None,20)
        scr5 = Screen(path + "/sprites/main_menu_screen.jpg", (1024, 700), (200, 25), [d], [])
        screens.append([scr3, scr4, scr5,scr5,scr5])