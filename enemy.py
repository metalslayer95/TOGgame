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
        self.type = "enemy"
        self.spellsOnField = []
        self.hp = 1000
        self.intelligence = 30
        self.attack = 1
        self.direction = 0
        enemies.add(self)
        all_sprites.add(self)

    def update(self, player, tick):
        if pixel_distance(self, player) <= 17:
            self.update = self.engage

    def engage(self, player, tick):
        print "Engage", self.attack
        if self.attack == 1:
            self.spellsOnField.append(Mana_bomb())
            self.spellsOnField[-1].update(self, tick)
            self.spellsOnField[-1].use(self, tick)
            self.attack = 0
        for spell in self.spellsOnField:
            spell.update(self, tick)
        if tick % 300 == 0:
            self.attack = 1
        if self.hp <= 0:
            enemies.remove(self)

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy