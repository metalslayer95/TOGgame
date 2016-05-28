# -*- coding: utf-8 -*-
from main_menu import *
from level import *
from character import *
'''
Final
Usar TilesMap
1) Documento
2) Versionamiento Github
videojuego plataforma con las sig caracteristicas
3) Menu inicial y de pausa
Inicial:
	Inicio
	Tutorial
	Salir
Pausa:
	Configurar teclado
	Continuar
	Salir


4) 5 modificaciones de juego
   5 tipos de enemigo
   1 Jefe de nivel
5) 1 nivel de 2 subniveles
6) Sonido, musica de fondo, sprites animados, linea de vida, puntaje
7) Indtroduccion y final (historia )
8) Jugabilidad
9) Originalidad
'''




 ## modo testing de juego, menu obviado
def run_Game():
    main_menu = Main_menu()
    pause_menu = Pause_menu()
    #main_menu.draw()
    level = LevelOne()
    onMenu = 0
    onGame = 1
    tick = 0
    while onMenu:
        for ev in event.get():
            if ev.type == QUIT:
                display.quit()
                quit()
                return
            elif ev.type == KEYDOWN:
                if not first_screen(main_menu, ev):
                    if not second_screen(main_menu, ev):
                        third_screen(main_menu, ev)
                main_menu.drawFocus()
                if main_menu.current_screen == len(main_menu.screens):
                    onMenu = 0
                    onGame = 1
                    main_menu.current_screen -= 1
        display.update()
        clock.tick(60)
    display.set_mode((1024,700))
    if main_menu.charSelect == 0:
        player = WaveController()
    elif main_menu.charSelect == 1:
        player = SpearBearer()
    level.draw()
    camera = Camera(level.image.get_size()[0], level.image.get_size()[1])
    while onGame:
            keys = key.get_pressed()
            for ev in event.get():
                if ev.type == QUIT:
                    display.quit()
                    quit()
                    return
                elif ev.type == KEYDOWN:
                    if ev.key == K_p:
                        image.save(screen, path + "/.tmp/game.png")
                        pause_menu.paused()
                    else:
                        player.action(ev.key, tick)
            if keys[K_DOWN]:
                player.move_down()
                level.update(player,2)
            if keys[K_UP]:
                level.update(player,3)
                player.move_up()
            if keys[K_RIGHT]:
                player.move_right()
                level.update(player,1)
            if keys[K_LEFT]:
                player.move_left()
                level.update(player,0)
            level.draw()
            player.update(tick)
            all_sprites.draw(screen)
            spells.draw(screen)
            display.update()
            tick += 1
            clock.tick(60)
    quit()

if __name__ == '__main__':
    #try:
    run_Game()
    #except:
    #    raise UserWarning, "Ha ocurrido un problema y el juego debe cerrarse."