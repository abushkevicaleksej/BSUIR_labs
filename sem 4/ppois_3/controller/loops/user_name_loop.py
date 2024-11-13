
from model.settings.buttons import *


def user_name_loop(screen, sounds, score, view, config):
    running = True
    user_name = '|'
    user_tick = config.get('user_tick', 30)
    box_width = True
    pygame.mouse.set_visible(False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                user_name = user_name.replace('|', '')
                user_tick = 150
                if event.key == pygame.K_RETURN:
                    running = False
                    if len(user_name) == 0:
                        user_name = 'NO NAME'
                    return True, user_name
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    if len(user_name) == 0:
                        user_name = 'NO NAME'
                    return False, user_name
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[0:-1]
                else:
                    if box_width:
                        sounds.type_sound.play()
                        if len(user_name) != 12:
                            user_name += event.unicode
                user_name += '|'

        view.draw(screen, user_name, user_tick, score)
        pygame.display.flip()
