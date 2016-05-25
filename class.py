# -*- coding: utf-8 -*-
from context import *


class Fisherman(sprite.Sprites):

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

class WaveController(sprite.Sprites):

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self.hp = 130
        self.strength = 3
        self.agility = 5
        self.wisdom = 9
        self.intelligence = 12
        self.nextlevel = 300

class SpearBearer(sprite.Sprites):

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


class LightBearer(sprite.Sprites):
    def __init__(self):
        sprite.Sprite.__init__(self)
        pass


