from main_menu import *

def run_Game():
    main_menu = Main_menu()
    main_menu.draw()
    onMenu = 1
    while onMenu:
        for ev in event.get():
            if ev.type == QUIT:
                display.quit()
                quit()
                graficando = 0
                return
            elif ev.type == KEYDOWN:
                if ev.key == K_DOWN and main_menu.focusOnDialog < 3 and main_menu.current_screen >0:
                    main_menu.focusOnDialog = main_menu.focusOnDialog + 1
                elif ev.key == K_UP and main_menu.focusOnDialog > 0 and main_menu.current_screen >0:
                    main_menu.focusOnDialog = main_menu.focusOnDialog - 1
                else:
                    main_menu.update()
                if main_menu.current_screen == len(main_menu.screens):
                    onMenu = 0
                    onGame = 1
        #main_menu.blink()
        display.update()
        clock.tick(15)
    while onGame:
            print "On game now"
            for ev in event.get():
                if ev.type == QUIT:
                    display.quit()
                    quit()
                    return
            clock.tick(1)
    quit()

run_Game()