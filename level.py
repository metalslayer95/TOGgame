# -*- coding: utf-8 -*-
from utils import *
#from pytmx.util_pygame import *


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

class LevelOne(sprite.Sprite):
    def __init__(self  ):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/level1.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = -self.image.get_size()[0] + 1024, -self.image.get_size()[1] + 700

    def draw(self, playerpos=()):
        screen.blit(self.image, self.rect)

    def scroll(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy




