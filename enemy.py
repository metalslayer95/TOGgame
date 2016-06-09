# -*- coding: utf-8 -*-
from utils import *
from spell import *


class Enemy(sprite.Sprite):
    def __init__(self, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = None
        self.rect = self.image.get_rect()
        self.type = "enemy"
        self.spellsOnField = []
        self.hp = None
        self.intelligence = None
        self.attack = 1
        self.direction = 0
        self.xpOnDeath = None


    def engage(self):
        pass

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


class Eel(sprite.Sprite):
    def __init__(self, size_x, size_y):
        sprite.Sprite.__init__(self)
        super(Eel, self).__init__()
        self.image = image.load(path + "/sprites/wave_controller/walk_down/0.png")
        self.image = transform.scale(self.image, [45,75])
        self.rect = self.image.get_rect()
        self.rect.x = size_x
        self.rect.y = size_y
        self.type = "enemy"
        self.spellsOnField = []
        self.hp = 1000
        self.intelligence = 30
        self.attack = 1
        self.direction = 0
        self.xpOnDeath = 500
        enemies.add(self)
        all_sprites.add(self)

    def update(self, player, tick):
        if pixel_distance(self, player) <= 17 and pixel_distance(self, player) > 0 :
            self.update = self.engage

    def engage(self, player, tick):
        if self.attack == 1:
            self.spellsOnField.append(Mana_bomb())
            self.spellsOnField[-1].use(self, tick)
            self.attack = 0
        for spell in self.spellsOnField:
            spell.update(self, tick)
        if tick % 300 == 0:
            self.attack = 1
        if self.hp <= 0:
            player.kill(self)
            enemies.remove(self)

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy