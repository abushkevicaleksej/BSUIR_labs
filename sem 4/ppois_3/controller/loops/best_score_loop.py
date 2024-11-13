from model.settings.buttons import *


def best_score_loop(screen, sounds, cursor_group, buttons, user_name, score, game, view):
    running = True
    sounds.main_theme_sound.play(-1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.main_theme_sound.stop()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.best_score_buttons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.main_theme_sound.stop()
                        sounds.button_click_sound.play()
                        running = False
                        return True

        view.draw(screen, buttons, game, cursor_group)
        pygame.display.flip()
