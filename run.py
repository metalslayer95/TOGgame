# -*- coding: utf-8 -*-
from main_menu import *

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

def run_Game():
    main_menu = Main_menu()
    pause_menu = Pause_menu()
    main_menu.draw()
    state = main_menu

    onMenu = 1
    onGame = 0
    while onMenu:
        for ev in event.get():
            if ev.type == QUIT:
                display.quit()
                quit()
                graficando = 0
                return
            elif ev.type == KEYDOWN:
                if ev.key == K_DOWN and main_menu.focusOnDialog < len(main_menu.screens[main_menu.current_screen][0].dialog)-1\
                        and main_menu.current_screen > 0:
                    main_menu.focusOnDialog = main_menu.focusOnDialog + 1
                elif ev.key == K_UP and main_menu.focusOnDialog > 0 and main_menu.current_screen > 0:
                    main_menu.focusOnDialog = main_menu.focusOnDialog - 1
                elif ev.key != K_UP and ev.key != K_DOWN and ev.key != K_ESCAPE:
                    main_menu.update()
                elif ev.key == K_ESCAPE and main_menu.current_screen > 0:
                    main_menu.current_screen -= 2
                    main_menu.update()
                main_menu.drawFocus()
                if main_menu.current_screen == len(main_menu.screens):
                    onMenu = 0
                    onGame = 1
                    main_menu.current_screen -= 1
        display.update()
        clock.tick(60)
    while onGame:
            print "On game now"
            for ev in event.get():
                if ev.type == QUIT:
                    display.quit()
                    quit()
                    return
                elif ev.type == KEYDOWN:
                    if ev.key == K_p:
                        image.save(screen, path + "/.tmp/game.png")
                        pause_menu.paused(state)
            main_menu.draw()
            display.update()
            clock.tick(60)
    quit()

if __name__ == '__main__':
    #try:
    run_Game()
    #except:
    #    raise UserWarning, "Ha ocurrido un problema y el juego debe cerrarse."