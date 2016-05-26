# -*- coding: utf-8 -*-
from context import *


class SpearBearer(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self.hp = 130
        self.strength = 13
        self.agility = 8
        self.wisdom = 5
        self.intelligence = 3
        self.nextlevel = 300
        player.add(self)
        all_sprites.add(self)

    def up(self):
        self.rect.y += -5

    def down(self):
        self.rect.y += 5

    def right(self):
        self.rect.x += 5

    def left(self):
        self.rect.x += -5


class WaveController(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_walk_down/0.png")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 600
        self.hp = 130
        self.strength = 3
        self.agility = 5
        self.wisdom = 9
        self.intelligence = 12
        self.nextlevel = 300
        player.add(self)
        all_sprites.add(self)

    def action(self):
        pass

    def up(self):
        self.rect.y += -5

    def down(self):
        self.rect.y += 5

    def right(self):
        self.rect.x += 5

    def left(self):
        self.rect.x += -5

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
        self.nextlevel = 300

    def basic_attack(self):
        pass

    def move(self,x,y):
        self.rect.x += x
        self.rect.y += y

class LightBearer(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        pass


