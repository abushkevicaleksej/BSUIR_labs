import pygame
import random

from model.settings.score_manager import ScoreImgManager


class Cursor(pygame.sprite.Sprite):
    def __init__(self, screen, img_path):
        super().__init__()
        self.screen = screen
        self.simple = 'sources/img/cursor/cursor.png'
        self.target = 'sources/img/cursor/cursorred.png'
        self.image = pygame.image.load(self.simple)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot_chicken(self, sounds, chickens_group, check_shot, score_manager, scores_group):
        for chicken in chickens_group:
            if self.rect.colliderect(chicken.rect) and chicken.alive:
                if check_shot:
                    index = random.randint(0, 2)
                    sounds.return_chick_hits(index).play()

                    score1 = ScoreImgManager(self.screen, score_manager)
                    score1.show = True
                    scores_group.add(score1)
                    for score in scores_group:
                        if score.show:
                            score.shot(chicken)

                    chicken.alive = False
                    return True

    def shoot_pumpkin(self, sounds, pumpkin, check_shot, score_manager, scores_group):
        if self.rect.colliderect(pumpkin.rect) and pumpkin.alive:
            if check_shot:
                sounds.pumpkin_shot_sound.play()

                score1 = ScoreImgManager(self.screen, score_manager)
                scores_group.add(score1)
                score1.show = True
                for score in scores_group:
                    if score.show:
                        score.shot(pumpkin)

                pumpkin.alive = False

                return True

    def shoot_sign_post(self, sounds, sign_post, check_shot, score_manager, scores_group):

        if self.rect.colliderect(sign_post.rect):
            if check_shot:
                sounds.sign_post_sound.play()

                score1 = ScoreImgManager(self.screen, score_manager)
                scores_group.add(score1)
                score1.show = True
                for score in scores_group:
                    if score.show:
                        score.shot(sign_post)
                if sign_post.shot:
                    sign_post.shot = False
                else:
                    sign_post.shot = True
                return True

    def shoot_big_chicken(self, sounds, cursor, big_chicken_group, check_shot, score_manager, scores_group):
        for big_chicken in big_chicken_group:
            if self.rect.colliderect(big_chicken.rect):
                if check_shot:
                    index = random.randint(0, 2)
                    sounds.return_chick_hits(index).play()

                    score1 = ScoreImgManager(self.screen, score_manager)
                    scores_group.add(score1)
                    score1.show = True
                    for score in scores_group:
                        if score.show:
                            score.shot(big_chicken)

                    if big_chicken.alive:
                        big_chicken.alive = False
                        big_chicken.current_time = 0

                return True

    def shoot_mill(self, cursor, x, y, sounds, mill, check_shot, score_manager, scores_group):
        for chicken in mill:
            k = chicken.check_shot(cursor,x,y)
            if k:
                if check_shot:
                    index = random.randint(0, 2)
                    sounds.return_chick_hits(index).play()

                    score1 = ScoreImgManager(self.screen, score_manager)
                    scores_group.add(score1)
                    score1.show = True
                    for score in scores_group:
                        if score.show:
                            score.shot(chicken)

                    if chicken.alive:
                        chicken.alive = False
                        chicken.current_time = 0

                return True

    def shoot_tree(self, sounds, trees, check_shot):
        for tree in trees:
            if self.rect.colliderect(tree.rect):
                if check_shot:
                    sounds.tree_hit_sound.play()
                return True
        return False

    def check_main_buttons(self, cursor, x, y, main_buttons, name):
        for button in main_buttons:
            if button.check(cursor, x, y) and button.name == name:
                return True
        return False

    def change_main_button(self, cursor, x, y, main_buttons, name):
        for button in main_buttons:
            if button.check(cursor, x, y) and button.name == name:
                new_button = 'sources/img/main_menu_background/' + name + '_h.png'
                button.change(new_button)
                return True
            else:
                if button.name == name:
                    new_button = 'sources/img/main_menu_background/' + name + '_normal.png'
                    button.change(new_button)
        return False

    def change_pressed_button(self, cursor, x, y, main_buttons, name):
        for button in main_buttons:
            if button.check(cursor, x, y) and button.name == name:
                new_button = 'sources/img/main_menu_background/' + name + '_pressed.png'

                button.change(new_button)
                print('it is', new_button)
                return True
            else:
                if button.name == name:
                    new_button = 'sources/img/main_menu_background/' + name + '_normal.png'
                    button.change(new_button)
        return False