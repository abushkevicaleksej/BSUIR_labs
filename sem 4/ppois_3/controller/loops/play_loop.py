import sys
import time
import pygame.event
from model.settings.timer import Timer
from model.objects.background import *
from model.settings.timer import Timer
from objects_imports import *
from model.objects.background import *
from model.objects.trees import *


def play_loop(clock, screen, sounds, buttons, cursor, cursor_group, chickens_small_group, chickens_mid_group,
              chickens_big_group, ammo, ammo_group, score_manager, scores_group, pumpkin, sign_post, big_chicken_group,
              mill, config):
    sounds.play_background.play(-1)
    running = True
    timer = Timer()
    pygame.mouse.set_visible(False)
    init_time = config.get('init_time', 0)
    big_chick_timer = config.get('big_chick_timer', 0)
    ammo_count = config.get('ammo_count', -1)
    tree1 = Tree(screen, 'sources/img/tree/trunkBig1.png', 300, 200)
    tree2 = Tree(screen, 'sources/img/tree/trunkSmall1.png',1900, 100)
    trees = pygame.sprite.Group()
    trees.add(tree1)
    trees.add(tree2)

    camera1 = Camera(0, 0, 100)
    camera2 = Camera(0, 80, 1900)
    camera3 = Camera(0, 130, 890)
    camera4 = Camera(0, 160, 1900)

    running = True
    while running:
        dt = clock.tick(config.get('fps'))
        cursor_x = cursor.rect.x
        if cursor_x >= 550 and cursor_x <= 800:
            if camera1.move(2) and camera2.move(5) and camera3.move(15) and camera4.move(40):
                chickens_small_group.update(dt, 'move_r')
                chickens_mid_group.update(dt, 'move_r')
                chickens_big_group.update(dt, 'move_r')
                big_chicken_group.update('move_r')

                mill.update('move_r')
                pumpkin.update('move_r')
                sign_post.update('move_r')
                trees.update('move_r')

        elif cursor_x <= 50 and cursor_x >= -50:
            if camera1.move(-2) and camera2.move(-5) and camera3.move(-15) and camera4.move(-40):
                chickens_small_group.update(dt, 'move_l')
                chickens_mid_group.update(dt, 'move_l')
                chickens_big_group.update(dt, 'move_l')
                big_chicken_group.update('move_l')

                mill.update('move_l')
                pumpkin.update('move_l')
                sign_post.update('move_l')
                trees.update('move_l')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.play_background.stop()
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.play_background.stop()
                    running = False
                    return 1, 0
                elif event.key == pygame.K_SPACE:

                    if ammo.count < 8:
                        ammo_count = ammo.update(screen, ammo_group)

            elif event.type == pygame.USEREVENT:
                chickens_small_group.add(ChickenSmall(screen, randint(100, 200)))
                chickens_mid_group.add(ChickenMiddle(screen, randint(100, 300)))
                chickens_big_group.add(ChickenBig(screen, randint(100, 500)))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    check_shot, ammo_count = ammo.shot()
                    x, y = event.pos
                    if cursor.shoot_big_chicken(sounds, cursor, big_chicken_group, check_shot, score_manager,
                                                scores_group):
                        break
                    elif cursor.shoot_tree(sounds, trees, check_shot):
                        break
                    elif cursor.shoot_chicken(sounds, chickens_big_group, check_shot, score_manager, scores_group):
                        print('big')
                        break
                    elif cursor.shoot_chicken(sounds, chickens_mid_group, check_shot, score_manager, scores_group):
                        print('mid')
                        break
                    elif cursor.shoot_chicken(sounds, chickens_small_group, check_shot, score_manager, scores_group):
                        print('small')
                        break
                    elif cursor.shoot_mill(cursor, x, y, sounds, mill, check_shot, score_manager, scores_group):
                        break
                    elif cursor.shoot_sign_post(sounds, sign_post, check_shot, score_manager, scores_group):
                        break
                    elif cursor.shoot_pumpkin(sounds, pumpkin, check_shot, score_manager, scores_group):
                        break

        big_chick_timer += 1
        if big_chick_timer == 40:
            sounds.big_chicken_pops_up_sound.play()
            x = randint(100, 1700)
            big_chicken_group.add(BigChicken(screen, (x, 450)))
            big_chick_timer = -300

        init_time += 1
        if init_time == 1:
            start_time = time.time()
        play_time = round(time.time() - start_time)

        play_time_check = timer.time_check(sounds, play_time)
        if play_time_check == 1:
            sounds.play_background.stop()
            sounds.game_over_sound.play()
            running = False
            return 2, score_manager.return_score()
        screen.fill((90, 100, 45))
        screen.blit(sky, (-camera1.rect[0], camera1.rect[1]))
        screen.blit(hills, (-camera2.rect[0], camera2.rect[1]))
        chickens_small_group.draw(screen)
        chickens_small_group.update(dt, 'no')
        screen.blit(castle, (-camera3.rect[0], camera3.rect[1]))
        chickens_mid_group.draw(screen)
        chickens_mid_group.update(dt, 'no')
        screen.blit(green, (-camera4.rect[0], camera4.rect[1]))
        pumpkin.update('no')
        mill.update('no')
        chickens_big_group.draw(screen)
        chickens_big_group.update(dt, 'no')
        sign_post.update('no')
        scores_group.update()
        trees.update('no')
        buttons.draw_text(f'Time: {90 - play_time}', 30, 70, 20)
        buttons.draw_text(f'Score: {score_manager.return_score()}', 30, 710, 20)
        big_chicken_group.update('no')
        ammo_group.update(dt, ammo_count)
        cursor_group.draw(screen)
        cursor_group.update()

        pygame.display.flip()