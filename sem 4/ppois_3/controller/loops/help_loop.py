import pygame


def help_loop(screen, sounds, cursor_group, buttons, view):
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
                    return True

        view.draw(screen, cursor_group)
        pygame.display.flip()
