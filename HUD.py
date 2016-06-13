# -*- coding: utf-8 -*-
from context import *

class HUD(sprite.Sprite):
    def __init__(self, player):
        sprite.Sprite.__init__(self)
        self.label_hp = monospace_big.render("HP ", 1, (255, 255, 0))
        self.label_mana = monospace_big.render("MA ", 1, (255, 255, 0))
        self.label_xp = monospace_big.render("XP ", 1, (255, 255, 0))
        self.label_boss = monospace_big.render("BOSS FIGHT ", 1, (255, 255, 0))
        self.label_boss_hp = monospace_big.render("UREK MAZINO ", 1, (255, 255, 0))
        self.hp_image = Surface((100, 25))
        self.hp_image.fill(GREEN)
        self.hp_rect = self.hp_image.get_rect()

        self.mana_image = Surface((100, 25))
        self.mana_image.fill(SKY_BLUE)
        self.mana_rect = self.mana_image.get_rect()

        self.xp_image = Surface((100, 25))
        self.xp_image.fill(MID_BLUE)
        self.xp_rect = self.xp_image.get_rect()
        self.boss_hp = None
        self.update(player)

    def update(self, player):
        updatehp, updatemana = player.hp*100/player.hpmax, player.mana*100/player.manamax
        if updatehp < 0:
            updatehp = 0
        if updatemana < 0:
            updatemana = 1
        self.hp_image = Surface((updatehp, 25))
        self.hp_image.fill(GREEN)
        self.hp_rect = self.hp_image.get_rect()
        self.mana_image = Surface((updatemana, 25))
        self.mana_image.fill(SKY_BLUE)
        self.mana_rect = self.mana_image.get_rect()
        self.xp_image = Surface((100, 25))
        self.xp_image.fill(MID_BLUE)
        self.xp_rect = self.xp_image.get_rect()
        self.hp_rect.x, self.hp_rect.y = 35, 25
        self.mana_rect.x, self.mana_rect.y = 35, 50
        self.xp_rect.x, self.xp_rect.y = screen.get_size()[0]-100, 80
        for enemy in enemies:
            if enemy.type == 'boss':
                updatehp = enemy.hp * 100 / enemy.hpmax
                if updatehp < 0:
                    updatehp = 0
                self.boss_hp = Surface((updatehp * 4, 25))
                self.boss_hp.fill(RED)

    def draw(self, player):
        self.update(player)
        if self.boss_hp is not None:
            screen.blit(self.label_boss, (400, 0))
            screen.blit(self.label_boss_hp, (350, 650))
            screen.blit(self.boss_hp, (350, 675))

        screen.blit(self.label_hp, (0, 25))
        screen.blit(self.hp_image, self.hp_rect)
        screen.blit(self.label_mana, (0, 50))
        screen.blit(self.mana_image, self.mana_rect)
        #screen.blit(self.label_xp, (screen.get_size()[0]-150, 80))
        #screen.blit(self.xp_image, self.xp_rect)