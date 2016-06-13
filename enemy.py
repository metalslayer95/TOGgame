# -*- coding: utf-8 -*-
from utils import *
from spell import *
from context import *

class Enemy(sprite.Sprite):
    image = None
    rect = None
    type = "enemy"
    spellsOnField = []
    hp = None
    intelligence = None
    attack = 1
    direction = 0
    xpOnDeath = None
    up = []
    down = []
    left = []
    right = []
    movement_speed = int(2.5 * (difficulty + 1))
    i = 0
    pos = []

    def __init__(self, size_x, size_y):
        sprite.Sprite.__init__(self)
        if self.type == 'boss':
            self.movement = 15

    def engage(self, player, tick):
        pass

    def move_up(self):
        self.direction = 1
        if self.rect.y -self.movement_speed >= 0:
            self.rect.y += -self.movement_speed
        self.pos[1] = self.rect.y
        if self.up != []:
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
        if self.rect.y + self.movement_speed <= screen.get_size()[1]:
            self.rect.y += self.movement_speed
        self.pos[1] = self.rect.y
        if self.down != []:
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
        if self.rect.x + self.movement_speed <= screen.get_size()[0]:
            self.rect.x += self.movement_speed
        self.pos[0] = self.rect.x
        if self.right != []:
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
        if self.rect.x -self.movement_speed >= 0:
            self.rect.x += -self.movement_speed
        self.pos[0] = self.rect.x
        if self.left != []:
            self.image = self.left[self.i]
            if self.i < len(self.left)-1:
                self.i += 1
            else:
                self.i = 0
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]


class Eel(Enemy):
    def __init__(self, size_x, size_y):
        super(Enemy, self).__init__()
        self.image = image.load(path + "/sprites/wave_controller/walk_down/0.png")
        self.image = transform.scale(self.image, [45,75])
        self.rect = self.image.get_rect()
        self.rect.x = size_x
        self.rect.y = size_y
        self.type = "enemy"
        self.spellsOnField = []
        self.hp = 100
        self.intelligence = 30
        self.attack = 1
        self.pos = [self.rect.x, self.rect.y]
        self.direction = 0
        self.xpOnDeath = 500
        enemies.add(self)
        all_sprites.add(self)

    def update(self, player, tick):
        if pixel_distance(self, player) <= 17 and pixel_distance(self, player) > 0 :
            self.update = self.engage

    def movement(self,x,y):
        if(x > self.rect.x):
            self.move_up()
        if(x < self.rect.x):
            self.move_down()
        if(y > self.rect.y):
            self.move_right()
        if(y < self.rect.y):
            self.move_left()

    def hit(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            enemies.remove(self)
            all_sprites.remove(self)

    def engage(self, player, tick):
        self.movement(player.rect.x, player.rect.y)
        if self.attack == 1:
            self.spellsOnField.append(Mana_bomb())
            self.spellsOnField[-1].use(self, tick)
            self.attack = 0
        for spell in self.spellsOnField:
            spell.update(player, tick)
        if tick % 180 == 0:
            self.attack = 1
        if self.hp <= 0:
            player.kill(self)
            enemies.remove(self)
            all_sprites.remove(self)

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy



class Fighter1(Enemy):
    def __init__(self, size_x, size_y):
        super(Enemy, self).__init__()
        self.image = image.load(path + "/sprites/fighter1/walk_down/0.png")
        self.image = transform.scale(self.image, [45,75])
        self.rect = self.image.get_rect()
        self.rect.x = size_x
        self.rect.y = size_y
        self.left = charge_images("walk_left", "fighter1", 9)
        self.up = charge_images("walk_up", "fighter1", 9)
        self.down = charge_images("walk_down", "fighter1", 9)
        self.right = charge_images("walk_right", "fighter1", 9)
        self.dead = charge_images("dead", "fighter1", 5)
        self.type = "enemy"
        self.spellsOnField = []
        self.hp = 150
        self.intelligence = 30
        self.attack = 1
        self.pos = [self.rect.x, self.rect.y]
        self.direction = 0
        self.xpOnDeath = 500
        enemies.add(self)
        self.i = 0
        all_sprites.add(self)

    def hit(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            enemies.remove(self)
            all_sprites.remove(self)

    def update(self, player, tick):
        if 0 < pixel_distance(self, player) <= 5 :
            self.update = self.engage

    def movement(self,x,y):
        if(x > self.rect.x):
            self.move_up()
        if(x < self.rect.x):
            self.move_down()
        if(y > self.rect.y):
            self.move_right()
        if(y < self.rect.y):
            self.move_left()

    def engage(self, player, tick):
        self.movement(player.rect.x, player.rect.y)
        if self.attack == 1:
            self.spellsOnField.append(Mana_arrow())
            self.spellsOnField[-1].use(self, tick)
            self.attack = 0
        for spell in self.spellsOnField:
            spell.update(player, tick)
        if tick % 60 == 0:
            self.attack = 1
        if self.hp <= 0:
            player.kill(self)
            enemies.remove(self)
            all_sprites.remove(self)

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy



class Fighter2(Enemy):
    def __init__(self, size_x, size_y):
        super(Enemy, self).__init__()
        self.image = image.load(path + "/sprites/fighter2/walk_down/0.png")
        self.image = transform.scale(self.image, [45,75])
        self.rect = self.image.get_rect()
        self.rect.x = size_x
        self.rect.y = size_y
        self.left = charge_images("walk_left", "fighter2", 9)
        self.up = charge_images("walk_up", "fighter2", 9)
        self.down = charge_images("walk_down", "fighter2", 9)
        self.right = charge_images("walk_right", "fighter2", 9)
        self.dead = charge_images("dead", "fighter2", 5)
        self.type = "enemy"
        self.spellsOnField = []
        self.hp = 150
        self.intelligence = 30
        self.attack = 1
        self.pos = [self.rect.x, self.rect.y]
        self.direction = 0
        self.xpOnDeath = 500
        enemies.add(self)
        self.i = 0
        all_sprites.add(self)

    def hit(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            enemies.remove(self)
            all_sprites.remove(self)

    def update(self, player, tick):
        if 0 < pixel_distance(self, player) <= 5 :
            self.update = self.engage

    def movement(self,x,y):
        if(x > self.rect.x):
            self.move_up()
        if(x < self.rect.x):
            self.move_down()
        if(y > self.rect.y):
            self.move_right()
        if(y < self.rect.y):
            self.move_left()

    def engage(self, player, tick):
        self.movement(player.rect.x, player.rect.y)
        if self.attack == 1:
            self.spellsOnField.append(Mana_arrow())
            self.spellsOnField[-1].use(self, tick)
            self.attack = 0
        for spell in self.spellsOnField:
            spell.update(player, tick)
        if tick % 30 == 0:
            self.attack = 1
        if self.hp <= 0:
            player.kill(self)
            enemies.remove(self)
            all_sprites.remove(self)

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


class Anak(Enemy):
    def __init__(self, size_x, size_y):
        super(Enemy, self).__init__()
        self.image = image.load(path + "/sprites/anak/walk_down/0.png")
        self.image = transform.scale(self.image, [45,75])
        self.rect = self.image.get_rect()
        self.rect.x = size_x
        self.rect.y = size_y
        self.left = charge_images("walk_left", "anak", 8)
        self.up = charge_images("walk_up", "anak", 8)
        self.down = charge_images("walk_down", "anak", 8)
        self.right = charge_images("walk_right", "anak", 8)
        #self.dead = charge_images("dead", "anak", 5)
        self.type = "enemy"
        self.spellsOnField = []
        self.hp = 150
        self.intelligence = 30
        self.attack = 1
        self.pos = [self.rect.x, self.rect.y]
        self.direction = 0
        self.xpOnDeath = 500
        enemies.add(self)
        self.i = 0
        all_sprites.add(self)

    def hit(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            enemies.remove(self)
            all_sprites.remove(self)

    def update(self, player, tick):
        if 0 < pixel_distance(self, player) <= 5 :
            self.update = self.engage

    def movement(self,x,y):
        if(x > self.rect.x):
            self.move_up()
        if(x < self.rect.x):
            self.move_down()
        if(y > self.rect.y):
            self.move_right()
        if(y < self.rect.y):
            self.move_left()

    def engage(self, player, tick):
        self.movement(player.rect.x, player.rect.y)
        if self.attack == 1:
            self.spellsOnField.append(Mana_arrow())
            self.spellsOnField[-1].use(self, tick)
            self.attack = 0
        for spell in self.spellsOnField:
            spell.update(player, tick)
        if tick % 30 == 0:
            self.attack = 1
        if self.hp <= 0:
            player.kill(self)
            enemies.remove(self)
            all_sprites.remove(self)

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class Urek(Enemy):
    def __init__(self, size_x, size_y):
        super(Enemy, self).__init__()
        self.image = image.load(path + "/sprites/urek/walk_down/0.png")
        self.image = transform.scale(self.image, [45,75])
        self.rect = self.image.get_rect()
        self.rect.x = size_x
        self.rect.y = size_y
        self.left = charge_images("walk_left", "urek", 8)
        self.up = charge_images("walk_up", "urek", 8)
        self.down = charge_images("walk_down", "urek", 8)
        self.right = charge_images("walk_right", "urek", 8)
        #self.dead = charge_images("dead", "anak", 5)
        self.type = "boss"
        self.spellsOnField = []
        self.hp = 500
        self.hpmax = 500
        self.intelligence = 30
        self.strenght = 100
        self.attack = 1
        self.pos = [self.rect.x, self.rect.y]
        self.direction = 0
        self.xpOnDeath = 500
        enemies.add(self)
        self.i = 0
        all_sprites.add(self)

    def hit(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            enemies.remove(self)
            all_sprites.remove(self)

    def update(self, player, tick):
        if 0 < pixel_distance(self, player) <= 50 :
            self.update = self.engage

    def movement(self,x,y):
        if(x > self.rect.x):
            self.move_up()
        if(x < self.rect.x):
            self.move_down()
        if(y > self.rect.y):
            self.move_right()
        if(y < self.rect.y):
            self.move_left()

    def engage(self, player, tick):
        screen.blit
        self.movement(player.rect.x, player.rect.y)
        if self.attack == 1:
            self.spellsOnField.append(Mana_arrow())
            self.spellsOnField[-1].use(self, tick)
            self.attack = 0
        for spell in self.spellsOnField:
            spell.update(player, tick)
        if tick % 30 == 0:
            self.attack = 1
        if self.hp <= 0:
            player.kill(self)
            enemies.remove(self)
            all_sprites.remove(self)

    def change_pos(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy