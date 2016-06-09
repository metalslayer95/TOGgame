# -*- coding: utf-8 -*-
from context import *
from spell import *

def charge_images(movement="", character="", nimage=0):
    array = []
    for i in range(0,nimage):
        im = image.load(path + "/sprites/" + character + "/" + movement + "/" + str(i) + ".png")
        im = transform.scale(im, [45, 75])
        array.append(im)
    return array


class WaveController(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_controller/walk_down/0.png")
        self.image = transform.scale(self.image, [45,75])
        self.rect = self.image.get_rect()
        self.left = charge_images("walk_left", "wave_controller", 8)
        self.up = charge_images("walk_up", "wave_controller", 8)
        self.down = charge_images("walk_down", "wave_controller", 8)
        self.right = charge_images("walk_right", "wave_controller", 8)
        self.rect.x = screen.get_size()[0]/2
        self.rect.y = screen.get_size()[1]/2
        self.spells = [Mana_arrow(), Mana_shield(), Mana_bomb(), Mana_storm()]
        self.spellsOnField = []
        self.i = 0
        self.type = "player"
        self.attack = 0
        self.pos = [self.rect.x, self.rect.y]
        self.hpmax = 130
        self.hp = 130
        self.strength = 3
        self.agility = 5
        self.wisdom = 9
        self.intelligence = 12
        self.mana = self.intelligence * 10
        self.manamax = self.intelligence * 10
        self.nextlevel = 300
        self.direction = 0
        players.add(self)
        all_sprites.add(self)

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def action(self, key=None, tick=0):
        if key == K_SPACE and self.attack == 0:
            self.attack += 60
        elif key == K_q and self.mana > 10 and self.spells[0].cooldown == 0:
            self.mana -= 10
            self.spells[0].cooldown += 3
            self.spellsOnField.append(Mana_arrow())
            self.spellsOnField[-1].use(self, tick)
        elif key == K_w and self.mana > 20 and self.spells[1].cooldown == 0:
            self.mana -= 30
            self.spells[1].cooldown += 60
            self.spellsOnField.append(Mana_shield())
            self.spellsOnField[-1].use()
        elif key == K_e and self.mana > 30 and self.spells[2].cooldown == 0:
            self.mana -= 20
            self.spells[2].cooldown += 5
            self.spellsOnField.append(Mana_bomb())
            self.spellsOnField[-1].use(self, tick)
        elif key == K_r and self.mana > 40 and self.spells[3].cooldown == 0:
            self.mana -= 40
            self.spells[3].cooldown += 120
            self.spellsOnField.append(Mana_arrow())
            self.spellsOnField[-1].use(self, tick)

    def kill(self, enemy):
        self.nextlevel -= enemy.xpOnDeath
        if self.nextlevel <= 0:
            self.nextlevel = 600

    def update(self, tick=0):
        for spell in self.spellsOnField:
            spell.update(self, tick)
        if self.attack != 0:
            self.attack -= 1
        if tick % 60 == 0:
            for cd in range(len(self.spells)):
                if self.spells[cd].cooldown != 0:
                    self.spells[cd].cooldown -= 1

        if tick % 180 == 0 and self.mana + int(self.intelligence * 1) <= self.manamax:
            self.mana += int(self.intelligence * 1)
        elif self.mana + int(self.intelligence * 1) >= self.manamax:
            self.mana = self.manamax
        if self.hp <= 0:
            enemies.remove(self)


    def move_up(self):
        self.direction = 1
        if self.rect.y -5 >= 0:
            self.rect.y += -5
        self.pos[1] = self.rect.y
        self.image = self.up[self.i]
        if self.i < len(self.up) - 1:
            self.i += 1
        else:
            self.i = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def move_down(self):
        self.direction = 0
        if self.rect.y + 5 <= screen.get_size()[1]:
            self.rect.y += 5
        self.pos[1] = self.rect.y
        self.image = self.down[self.i]
        if self.i < len(self.down) - 1:
            self.i += 1
        else:
            self.i = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def move_right(self):
        self.direction = 2
        if self.rect.x + 5 <= screen.get_size()[0]:
            self.rect.x += 5
        self.pos[0] = self.rect.x
        self.image = self.right[self.i]
        if self.i < len(self.right) - 1:
            self.i += 1
        else:
            self.i = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def move_left(self):
        self.direction = 3
        if self.rect.x -5 >= 0:
            self.rect.x += -5
        self.pos[0] = self.rect.x
        self.image = self.left[self.i]
        if self.i < len(self.left)-1:
            self.i += 1
        else:
            self.i = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def get_pos(self):
        return self.pos

class SpearBearer(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/spear_walk_down/0.png")
        self.rect = None
        self.hp = 130
        self.maxfury = 100
        self.fury = 0
        self.strength = 13
        self.type = "player"
        self.agility = 8
        self.wisdom = 5
        self.intelligence = 3
        self.nextlevel = 300
        players.add(self)
        all_sprites.add(self)

        def move_up(self):
            self.direction = 1
            if self.rect.y - 5 >= 0:
                self.rect.y += -5
            self.pos[1] = self.rect.y
            self.image = self.up[self.i]
            if self.i < len(self.up) - 1:
                self.i += 1
            else:
                self.i = 0
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

        def move_down(self):
            self.direction = 0
            if self.rect.y + 5 <= screen.get_size()[1]:
                self.rect.y += 5
            self.pos[1] = self.rect.y
            self.image = self.down[self.i]
            if self.i < len(self.down) - 1:
                self.i += 1
            else:
                self.i = 0
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

        def move_right(self):
            self.direction = 2
            if self.rect.x + 5 <= screen.get_size()[0]:
                self.rect.x += 5
            self.pos[0] = self.rect.x
            self.image = self.right[self.i]
            if self.i < len(self.right) - 1:
                self.i += 1
            else:
                self.i = 0
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

        def move_left(self):
            self.direction = 3
            if self.rect.x - 5 >= 0:
                self.rect.x += -5
            self.pos[0] = self.rect.x
            self.image = self.left[self.i]
            if self.i < len(self.left) - 1:
                self.i += 1
            else:
                self.i = 0
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

        def get_pos(self):
            return self.pos


class Fisherman(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self.hp = 130
        self.strength = 13
        self.agility = 8
        self.wisdom = 5
        self.intelligence = 3
        self.fury = 0
        self.nextlevel = 300

    def action(self):
        pass

    def move(self,x,y):
        self.rect.x += x
        self.rect.y += y

class LightBearer(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        pass


