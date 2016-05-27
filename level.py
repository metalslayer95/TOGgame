# -*- coding: utf-8 -*-
from utils import *
from pytmx.util_pygame import *


class LevelOne(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(path + "/level1.png")
        self.image = transform.scale(self.image,[self.image.get_size()[0]*5/7,self.image.get_size()[1]*5/7])
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.image, ((-self.image.get_size()[0]) + 1124,-self.image.get_size()[1]+700))