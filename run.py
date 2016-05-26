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
    state = main_menu

    onMenu = 0
    onGame = 1
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
    screen.fill(BLACK)
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
            if keys[K_DOWN]:
                player.down()
            if keys[K_UP]:
                player.up()
            if keys[K_RIGHT]:
                player.right()
            if keys[K_LEFT]:
                player.left()
            screen.fill(BLACK)
            all_sprites.draw(screen)
            display.update()
            clock.tick(60)
    quit()

if __name__ == '__main__':
    #try:
    run_Game()
    #except:
    #    raise UserWarning, "Ha ocurrido un problema y el juego debe cerrarse."