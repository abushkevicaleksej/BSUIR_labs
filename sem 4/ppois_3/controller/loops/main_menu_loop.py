
from model.settings.buttons import *


def main_menu_loop(screen, sounds, cursor, cursor_group, main_buttons):
    running = True

    # turn off the image of the REAL 'CURSOR'
    pygame.mouse.set_visible(False)

    # main theme SOUND
    sounds.main_theme_sound.play(-1)
    back = pygame.image.load("sources/img/main_menu_background/main_menu.png")
    back_rect = back.get_rect()
    moorhuhn = pygame.image.load("sources/img/main_menu_background/moorhuhn.png")
    moorhuhn_rect = moorhuhn.get_rect(center=(400,66))

    # for HOLES
    new_holes_max_time = 15
    new_holes_current_time = 0
    index = 0
    finish = False

    while running:
        screen.fill((0, 100, 0))
        screen.blit(back, back_rect)
        screen.blit(moorhuhn, moorhuhn_rect)

        main_buttons.update()
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.main_theme_sound.stop()
                running = False

            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                if cursor.change_main_button(cursor, x, y, main_buttons, 'start'):
                    break
                elif cursor.change_main_button(cursor, x, y, main_buttons, 'score'):
                    break
                elif cursor.change_main_button(cursor, x, y, main_buttons, 'menu'):
                    break
                elif cursor.change_main_button(cursor, x, y, main_buttons, 'exit'):
                    break


            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if cursor.check_main_buttons(cursor, x, y, main_buttons, 'start'):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        sounds.main_theme_sound.stop()
                        running = False
                        sounds.ready_after_user_name.play()
                        return 1
                elif cursor.check_main_buttons(cursor, x, y, main_buttons, 'score'):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        sounds.main_theme_sound.stop()
                        running = False
                        return  2
                elif cursor.check_main_buttons(cursor, x, y, main_buttons, 'menu'):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        sounds.main_theme_sound.stop()
                        running = False
                        return  3
                elif cursor.check_main_buttons(cursor, x, y, main_buttons, 'exit'):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        sounds.main_theme_sound.stop()
                        running = False
                        return  4

        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()
