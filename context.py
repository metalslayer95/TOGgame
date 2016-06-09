# -*- coding: utf-8 -*-
from pygame import *
import os

path = os.path.dirname(os.path.abspath(__file__))
BLACK = (0, 0, 0)
BLACK2 = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (184, 132, 11)
RED = (165, 42, 42)
GREEN = (0, 255, 0)
MID_BLUE = (25, 25, 112)
SKY_BLUE = (0, 191, 255)
screen = None
ancho = 778
alto = 405
size = [ancho, alto]
cx, cy = ancho / 2, alto / 2
init()
screen = display.set_mode(size)
display.set_caption("Tower Of God game")

monospace_big = font.SysFont("monospace", 24)
monospace_big.set_bold(1)

clock = time.Clock()


ch1 = mixer.Channel(1)
ch2 = mixer.Channel(2)

all_sprites = sprite.Group()

npcs = sprite.Group()

enemies = sprite.Group()

players = sprite.Group()

spells = sprite.Group()

e_spells = sprite.Group()