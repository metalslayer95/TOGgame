# -*- coding: utf-8 -*-
from context import *


class Pause_menu():

    def __init__(self):
        self.titledialog = Dialog("PAUSA",[250, 100],None, 80)
        self.cfdialog = Dialog("Configurar teclado", [350, 300], None, 20)
        self.adialog = Dialog("  Ayuda", [400, 380], None, 20)
        self.sdialog = Dialog("  Salir", [400, 460], None, 20)
        screen1 = Screen("", (1024,700), (300,200), [self.titledialog,  self.cfdialog,  self.adialog,  self.sdialog], [], "")
        self.screens = []
        self.screens.append(screen1)
        self.focusOnDialog = 0
        self.current_screen = 0

    def update(self):
        if self.focusOnDialog == 0:
            print "Configurar teclado"
        elif self.focusOnDialog == 1:
            print "ayuda"
        elif self.focusOnDialog == 2:
            salir()

    def paused(self, state=None):
        self.screens[0].update("", path + "/.tmp/game.png")
        while True:
                for ev in event.get():
                    if ev.type == QUIT:
                        display.quit()
                        quit()
                        return
                    if ev.type == KEYDOWN:
                        if ev.key == K_p:
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
    def __init__(self, img="", size=(), pos=(), dialog=None, addins=[], tmpImg=""):
        self.background = None
        self.tmpImg = None
        self.size = size
        self.update(img, tmpImg)
        self.pos = pos
        self.dialog = dialog
        self.addins = addins

    def update(self,img="",tmpImg=""):
        if img != "":
            self.background = image.load(img)
            self.background = transform.scale(self.background, self.size)
        elif tmpImg != "":
            self.tmpImg = image.load(tmpImg)
            self.tmpImg.set_alpha(40)
            self.background = None

    def draw(self):
        screen = display.set_mode(self.size)
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
        if self.addins == []:
            return
        else:
            for adds in self.addins:
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
                letter = image.load("sprites/letters/"+l.upper()+".png")
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


def salir():
    # TODO: implementacion sqlite
    display.quit()
    quit()
    exit()

def screen_creation(screens = []):
        dialog = Dialog("Presione una tecla para continuar", [250, 303], None, 10)
        scr = Screen(path + "/sprites/starting_screen.jpg",(778,405),(300, 200), [dialog],[])
        screens.append([scr])

        ngdialog = Dialog("Nuevo juego", [350, 200],None, 20)
        lgdialog = Dialog("Cargar juego", [350, 240],None, 20)
        pvpdialog = Dialog("  Versus", [350, 280],None, 20)
        hdialog = Dialog("  Ayuda", [350, 320],None, 20)
        cdialog = Dialog(" Creditos", [350, 360],None, 20)
        scr2 = Screen(path + "/sprites/main_menu_screen.jpg", (900, 700), (200, 25), [ngdialog, lgdialog, pvpdialog,                                                                          hdialog, cdialog], [])
        screens.append([scr2])

        j1dialog = Dialog(" Juego facil",[350,240],None,20)
        j2dialog = Dialog("Juego normal",[350,320],None,20)
        j3dialog = Dialog("Juego dificil",[350,400],None,20)
        scr3 = Screen(path + "/sprites/main_menu_screen.jpg", (900, 700), (200, 25), [j1dialog,j2dialog,j3dialog], [])

        p1 = Dialog("Personaje a nivel X",[400,300],None,20)
        p2 = Dialog("Personaje b nivel Y",[400,380],None,20)
        scr4 = Screen("sprites/main_menu_screen.jpg", (900, 700), (200, 25), [p1,p2], [])

        d = Dialog("Modo versus en desarrollo",[400,300],None,20)
        scr5 = Screen(path + "/sprites/main_menu_screen.jpg", (900, 700), (200, 25), [d], [])

        screens.append([scr3, scr4, scr5, scr5, scr5])

        seldialog = Dialog("Seleccion de personaje",[50,0], None, 40)
        d1 = Dialog("Wave controller",[200, 550], None, 20)
        wavedialog = Dialog("Ataques magicos",[250, 600], None, 10)
        d2 = Dialog("Spear bearer",[600, 550], None, 20)
        speardialog = Dialog("Ataques fisicos",[650, 600], None, 10)
        wave = image.load(path + "/sprites/wave_character.png")
        wave = transform.scale(wave, (300,300))
        spear = image.load(path + "/sprites/spear_character.png")
        spear = transform.scale(spear, (300,300))
        scr6 = Screen(path + "/sprites/char_screen.jpg", (1024, 700), (200, 25), [seldialog, wavedialog, speardialog, d1
            , d2], [(wave, [200, 200]), (spear, [600, 200])])
        screens.append([scr6, scr6, scr6, scr6])


def first_screen(main_menu=None,ev=None):
    if ev.key == K_DOWN and main_menu.focusOnDialog < 4 and main_menu.current_screen == 1:
        main_menu.focusOnDialog += 1
    elif ev.key == K_UP and main_menu.focusOnDialog > 0 and main_menu.current_screen == 1:
        main_menu.focusOnDialog -= 1
    elif ev.key == K_RETURN and main_menu.current_screen < 2:
        main_menu.update()
        return 1
    elif ev.key == K_ESCAPE and main_menu.current_screen > 0:
        main_menu.focusOnDialog = 0
        main_menu.current_screen -= 2
        main_menu.update()
    return 0


def second_screen(main_menu=None, ev=None):
    if main_menu.focusOnDialog == 0 and main_menu.current_screen == 2:
        if ev.key == K_DOWN  and main_menu.diffSelect < 2:
            main_menu.diffSelect += 1
        elif ev.key == K_UP and main_menu.diffSelect > 0:
            main_menu.diffSelect -= 1
        elif ev.key == K_RETURN:
            main_menu.update()
            return 1
        elif ev.key == K_ESCAPE:
            main_menu.focusOnDialog = 0
            main_menu.diffSelect = 0
            main_menu.current_screen -= 2
            main_menu.update()
    if main_menu.focusOnDialog == 1 and main_menu.current_screen == 2:
        if ev.key == K_DOWN  and main_menu.charSelect < 2: # aca se carga de bd
            main_menu.charSelect += 1
        elif ev.key == K_UP and main_menu.charSelect > 0:
            main_menu.charSelect -= 1
        elif ev.key == K_RETURN:
            main_menu.update()
            return 1
        elif ev.key == K_ESCAPE:
            main_menu.focusOnDialog = 0
            main_menu.charSelect = 0
            main_menu.current_screen -= 2
            main_menu.update()
    return 0


def third_screen(main_menu=None, ev=None):
    if main_menu.focusOnDialog == 0 and main_menu.current_screen == 3:
        print "entro"
        if ev.key == K_RIGHT and main_menu.charSelect < 1:
            main_menu.charSelect += 1
        elif ev.key == K_LEFT and main_menu.charSelect > 0:
            main_menu.charSelect -= 1
        elif ev.key == K_RETURN:
            main_menu.update()
            return 1
        elif ev.key == K_ESCAPE:
            main_menu.focusOnDialog = 0
            main_menu.charSelect = 0
            main_menu.current_screen -= 2
            main_menu.update()
    return 0