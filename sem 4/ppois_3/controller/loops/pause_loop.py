import pygame


def pause_loop(screen, sounds, buttons, cursor, view):
    running = True
    pygame.mouse.set_visible(False)
    sounds.main_theme_sound.play(-1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.main_theme_sound.stop()
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if buttons.pause_buttons[0].collidepoint(pygame.mouse.get_pos()):
                        sounds.main_theme_sound.stop()
                        sounds.button_click_sound.play()
                        running = False
                        return 1
                    elif buttons.pause_buttons[1].collidepoint(pygame.mouse.get_pos()):
                        sounds.main_theme_sound.stop()
                        sounds.button_click_sound.play()
                        running = False
                        return 2

        view.draw(screen, buttons, cursor)
        pygame.display.flip()
