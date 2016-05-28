# -*- coding: utf-8 -*-
from context import *


class Mana_arrow(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_spells/mana_shield.png")
        self.image = transform.scale(self.image, [50, 50])
        self.rect = self.image.get_rect()
        self.cooldown = 0
        self.direction = -1
        self.damage = 0
        self.distance = 1000
        self.update = self._update

    def _update(self, player, tick):
        self.damage = 20 + int(player.intelligence * 0.2)
        self.direction = player.direction
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

    def moving(self, player, tick):
        if self.distance > 0 and tick % 60:
            if self.direction == 0:
                self.rect.y += 5
            elif self.direction == 1:
                self.rect.y -= 5
            elif self.direction == 2:
                self.rect.x += 5
            elif self.direction == 3:
                self.rect.x -= 5
            self.distance -= 5
        elif self.distance == 0:
            spells.remove(self)
            player.spellsOnField.remove(self)
            self.distance = 1000
            self.update = self._update

    def use(self,player,tick):
        spells.add(self)
        self.update(player, tick)
        self.update = self.moving

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


class Mana_bomb(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_spells/mana_shield.png")
        self.image = transform.scale(self.image, [50, 50])
        self.rect = self.image.get_rect()
        self.cooldown = 0
        self.direction = -1
        self.distance = 500
        self.damage = 0
        self.update = self._update

    def _update(self, player,tick):
        self.damage = 80 + int(player.intelligence * 0.7)
        self.direction = player.direction
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

    def moving(self, player, tick):
        if self.distance > 0 and tick % 60:
            if self.direction == 0:
                self.rect.y += 2
            elif self.direction == 1:
                self.rect.y -= 2
            elif self.direction == 2:
                self.rect.x += 2
            elif self.direction == 3:
                self.rect.x -= 2
            self.distance -= 2
        elif self.distance == 0:
            player.spellsOnField.remove(self)
            spells.remove(self)
            self.distance = 700
            self.update = self._update

    def use(self,player,tick):
        spells.add(self)
        self.update(player, tick)
        self.update = self.moving


    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


class Mana_shield(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_spells/mana_shield.png")
        self.image = transform.scale(self.image, [110, 110])
        self.rect = self.image.get_rect()
        self.cooldown = 0
        self.time = 0
        self.used = 0

    def update(self, player, tick):
        self.rect.x = player.rect.x - 32
        self.rect.y = player.rect.y - 25
        if self.time > 0 and tick % 60 == 0:
            self.time -= 1
        elif self.used == 1 and self.time == 0:
            spells.remove(self)
            self.used = 0

    def use(self):
        if self.used == 0:
            print "used mana shield"
            self.used = 1
            self.time = 30
            spells.add(self)

    def change_pos(self, dx, dy): #unused
        pass


class Mana_storm(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_spells/mana_shield.png")
        self.rect = self.image.get_rect()
        self.cooldown = 0
        self.time = 60

    def use(self):
        pass#spells.add(self)