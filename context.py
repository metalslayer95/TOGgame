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
screen = None
ancho = 800
alto = 600
size = [ancho, alto]
cx, cy = ancho / 2, alto / 2
init()
screen = display.set_mode(size)
display.set_caption("Tower Of God game")
clock = time.Clock()

all_sprites = sprite.Group()

npc = sprite.Group()

enemies = sprite.Group()

player = sprite.Group()