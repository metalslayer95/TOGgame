# -*- coding: utf-8 -*-
from utils import *
from enemy import *

HALF_WIDTH = 512
HALF_HEIGHT = 350
WIN_WIDTH = 1661
WIN_HEIGHT = 2526

class Camera(object):
    def __init__(self, width, height):
        self.camera_func = self.complex_camera
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    def complex_camera(self,camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h # center player

        l = min(0, l)                           # stop scrolling at the left edge
        l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
        t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
        t = min(0, t)                           # stop scrolling at the top

        return Rect(l, t, w, h)


def apply_offset(offset_x,offset_y):
    for sp in spells:
        sp.change_pos(offset_x, offset_y)
    for en in enemies:
        en.change_pos(offset_x, offset_y)

class LevelOne(sprite.Sprite):
    def __init__(self  ):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/level1.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = -self.image.get_size()[0] + 1324, -self.image.get_size()[1] + 700
        self.sound = mixer.Sound(path + "/music/level1.wav")
        ch1.play(self.sound, -1)
        eel = Eel(-self.image.get_size()[0] + 2100, -self.image.get_size()[1] + 1100)
        enemies.add(eel)
        all_sprites.add(eel)

    def update(self, player, direction):
        if player.rect.x <= 10 and direction == 0: # left
            if self.rect.x + 30 <= 0 :
                self.rect.x += 30
                player.change_pos(30, 0)
                apply_offset(30, 0)
        elif player.rect.x >= 1014  and direction == 1: # right
            if self.rect.x - 40 >= -self.image.get_size()[0] + screen.get_size()[0] + 50:
                self.rect.x -= 40
                player.change_pos(-40, 0)
                apply_offset(-40, 0)
        elif player.rect.y >= 690 and direction == 2: # down
            if self.rect.y - 100 >= -self.image.get_size()[1] + screen.get_size()[1] - 150:
                self.rect.y -= 100
                player.change_pos(0, -100)
                apply_offset(0, -100)
        elif player.rect.y <= 10 and direction == 3: #up
            if self.rect.y + 100 <= -100:
                self.rect.y += 100
                player.change_pos(0, 100)
                apply_offset(0, 100)

    def draw(self):
        screen.blit(self.image,self.rect)

    def cleared(self):
        if len(enemies) == 0:
            ch1.stop()
            return 1


class LevelTwo(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/level1.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = -self.image.get_size()[0] + 1324, -self.image.get_size()[1] + 700
        self.sound = mixer.Sound(path + "/music/level1.wav")
        ch1.play(self.sound, -1)


    def draw(self):
        screen.blit(self.image, self.rect)

    def cleared(self):
        if len(enemies) == 0:
            ch1.stop()
            return 1