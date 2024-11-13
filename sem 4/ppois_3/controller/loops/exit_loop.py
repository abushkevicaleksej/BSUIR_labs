import pygame


def exit_loop(screen, sounds, cursor_group, buttons, view):
    running = True
    sounds.main_theme_sound.play(-1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.main_theme_sound.stop()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.main_theme_sound.stop()
                    running = False
                    return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.exit_buttons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.main_theme_sound.stop()
                        sounds.button_click_sound.play()
                        running = False
                        return 1
                elif buttons.exit_buttons[1].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.main_theme_sound.stop()
                        sounds.button_click_sound.play()
                        running = False
                        return 2

        view.draw(screen, buttons, cursor_group)
        pygame.display.flip()
