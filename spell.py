# -*- coding: utf-8 -*-
from context import *
from utils import *

class Mana_arrow(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.collidesound = mixer.Sound(path + "/music/bomb_hit.wav")
        self.image = image.load(path + "/sprites/wave_controller/spells/mana_arrow.png")
        self.rect = self.image.get_rect()
        self.cooldown = 0
        self.direction = -1
        self.sound = mixer.Sound(path + "/music/arrow_cast.wav")
        self.damage = 0
        self.distance = 1000
        self.track = None
        self.i = 1
        self.update = self._update

    def _update(self, player, tick):
        self.damage = 20 + int(player.intelligence * 0.2)
        self.direction = player.direction
        if self.direction == 0:
            self.image = transform.rotate(self.image, 270)
            self.rect = self.image.get_rect()
        if self.direction == 1:
            self.image = transform.rotate(self.image, 90)
            self.rect = self.image.get_rect()
        if self.direction == 3:
            self.image = transform.rotate(self.image, 180)
            self.rect = self.image.get_rect()
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
            try:
                player.spellsOnField.remove(self)
            except:
                pass
            self.distance = 1000
            self.update = self._update

    def enemy_moving(self, player, tick):
        if self.direction == 0:
            self.rect.y -= 2
        elif self.direction == 1:
            self.rect.y += 2
        elif self.direction == 2:
            self.rect.x -= 2
        elif self.direction == 3:
            self.rect.x += 2
            self.distance -= 2
        elif self.distance == 0:
            try:
                player.spellsOnField.remove(self)
            except:
                pass
            spells.remove(self)

    def use(self,player, tick):
        self.update(player, tick)
        ch2.play(self.sound)
        if player.type is 'player':
            spells.add(self)
            self.update = self.moving
        else:
            e_spells.add(self)
            self.update = self.enemy_moving

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


class Mana_bomb(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_controller/spells/mana_bomb.png")
        self.rect = self.image.get_rect()
        self.cooldown = 0
        self.sound = mixer.Sound(path + "/music/mana_bomb.wav")
        self.collidesound = mixer.Sound(path + "/music/bomb_hit.wav")
        self.direction = -1
        self.distance = 500
        self.damage = 0
        self.track = None
        self.i = 1

    def update(self, player, tick):
        self.damage = 80 + int(player.intelligence * 0.7)
        self.direction = player.direction
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

    def enemy_moving(self,player, tick):
        if self.direction == 0:
            self.rect.y -= 2
        elif self.direction == 1:
            self.rect.y += 2
        elif self.direction == 2:
            self.rect.x -= 2
        elif self.direction == 3:
            self.rect.x += 2
            self.distance -= 2
        elif self.distance == 0:
            try:
                player.spellsOnField.remove(self)
            except:
                pass
            spells.remove(self)

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
            try:
                player.spellsOnField.remove(self)
            except:
                pass
            spells.remove(self)

    def use(self, player, tick):
        ch2.play(self.sound)
        self.update(player, tick)
        if player.type is 'player':
            spells.add(self)
            self.update = self.moving
        else:
            e_spells.add(self)
            self.update = self.enemy_moving
        self.i = 0

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


class Mana_shield(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_controller/spells/mana_shield.png")
        self.image = transform.scale(self.image, [110, 110])
        self.rect = self.image.get_rect()
        self.sound = mixer.Sound(path + "/music/mana_shield.wav")
        self.collidesound = mixer.Sound(path + "/music/mana_shield.wav")
        self.cooldown = 0
        self.time = 0
        self.damage = 0
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
            ch2.play(self.sound)
            self.used = 1
            self.time = 30
            spells.add(self)

    def change_pos(self, dx, dy): #unused
        pass


class Mana_storm(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/sprites/wave_controller/spells/mana_shield.png")
        self.rect = self.image.get_rect()
        self.sound = mixer.Sound(path + "/music/storm_cast.wav")
        self.cooldown = 0
        self.damage = 0
        self.time = 60

    def update(self, player, tick):
        self.damage = 80 + int(player.intelligence * 0.7)
        self.direction = player.direction
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

    def enemy_moving(self, player, tick):
        if self.direction == 0:
            self.rect.y -= 2
        elif self.direction == 1:
            self.rect.y += 2
        elif self.direction == 2:
            self.rect.x -= 2
        elif self.direction == 3:
            self.rect.x += 2
            self.distance -= 2
        elif self.distance == 0:
            try:
                player.spellsOnField.remove(self)
            except:
                pass
            spells.remove(self)

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
            try:
                player.spellsOnField.remove(self)
            except:
                pass
            spells.remove(self)

    def use(self, player, tick):
        ch2.play(self.sound)
        self.update(player, tick)
        if player.type is 'player':
            spells.add(self)
            self.update = self.moving
        else:
            e_spells.add(self)
            self.update = self.enemy_moving
        self.i = 0

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy