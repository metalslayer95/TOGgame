# -*- coding: utf-8 -*-
from utils import *
from spell import *


class Eel(sprite.Sprite):
    def __init__(self, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_controller/walk_down/0.png")
        self.image = transform.scale(self.image, [45,75])
        self.rect = self.image.get_rect()
        self.rect.x = size_x
        self.rect.y = size_y
        self.spells = [Mana_bomb()]
        self.spellsOnField = []
        self.intelligence = 30
        self.attack = 1
        self.direction = 0

    def update(self, player, tick):
        print pixel_distance(self,player)
        if pixel_distance(self,player) <= 17:
            self.update = self.engage

    def engage(self, player, tick):
        print "engaged"
        if self.attack == 1:
            self.spellsOnField.append(Mana_bomb())
            self.attack = 0
        for spell in self.spellsOnField:
            spell.update(self, tick)
        if tick % 60 == 0:
            for cd in range(len(self.spells)):
                if self.spells[cd].cooldown != 0:
                    self.spells[cd].cooldown -= 1
        elif tick % 300 == 0:
            self.attack = 1

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy