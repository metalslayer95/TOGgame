from context import *



def screen_creation(screens = []):
        dialog = Dialog("Press any key to continue", [250, 303], None, 10)
        scr = Screen("sprites/tower_main_s_1.jpg",(778,405),(300,200), [dialog],[])
        screens.append([scr])
        ngdialog = Dialog("New game", [400, 300],None, 20)
        lgdialog = Dialog("Load game", [400, 340],None, 20)
        pvpdialog = Dialog("Versus", [400, 380],None, 20)
        hdialog = Dialog("  Help", [400, 420],None, 20)
        cdialog = Dialog(" Credits", [400, 460],None, 20)
        scr2 = Screen("sprites/tower_main_s_2.jpg", (1024, 700), (200, 25), [ngdialog, lgdialog, pvpdialog, hdialog, cdialog], [])
        screens.append([scr2])


class Screen():
    def __init__(self,img = "", size = (), pos = (),dialog = None, addin = []):
        self.background = image.load(img)
        self.screen_size = size
        self.pos = pos
        self.dialog = dialog

    def draw(self,addin = []):
        global screen
        screen = display.set_mode(self.screen_size)
        screen.blit(self.background,[0,0])
        dlg = self.dialog
        if dlg is not None and dlg != []:
            for d in dlg:
                d.draw()
        if addin == []:
            return
        else:
            for adds in addin:
                screen.blit(adds[0],adds[1])


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
