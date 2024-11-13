from model.objects.chicken import *
from model.objects.big_chicken import BigChicken
from model.objects.mill import MillChicken
from model.objects.pumpkin import *
from model.objects.sign_post import *


class ScoreImgManager(pygame.sprite.Sprite):
    def __init__(self, screen, score_manager):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.score = 0
        self.score_manager = score_manager
        self.font = pygame.font.Font('sources/fonts/AA_Magnum.ttf', 50)

        self.show = False
        self.max_show_y = 25
        self.current_score = 0

        self.max_show_time = 3
        self.show_time = 0

        self.image = self.font.render('0', True, (255,255,255,255))
        self.rect = self.image.get_rect()


    def shot(self, shot_object):
        if isinstance(shot_object, ChickenSmall):

            self.score += 20
            self.score_manager.update_score('+',20)
            self.show = True
            self.draw_score(str(20), shot_object)

        elif isinstance(shot_object, ChickenMiddle):
            if shot_object.size == (60,60):
                self.score += 15
                self.score_manager.update_score('+', 15)
                self.show = True
                self.draw_score(str(15), shot_object)
        elif isinstance(shot_object, ChickenBig):
            if shot_object.size == (80,80):
                self.score += 10
                self.score_manager.update_score('+', 10)
                self.show = True
                self.draw_score(str(10), shot_object)


        elif isinstance(shot_object, Pumpkin):
            self.score_manager.update_score('+', 15)
            self.show = True
            self.draw_score(str(15), shot_object)

        elif isinstance(shot_object, SignPost):
            self.score_manager.update_score('-', 15)
            self.show = True
            self.draw_score(str(-15), shot_object)

        elif isinstance(shot_object, BigChicken):
            self.score_manager.update_score('+', 25)
            self.show = True
            self.draw_score(str(25), shot_object)

        elif isinstance(shot_object, MillChicken):
            self.score_manager.update_score('+', 25)
            self.show = True
            self.draw_score(str(25), shot_object)


    def draw_score(self, new_score, shot_object):
        self.image = self.font.render(new_score, True, (255,255,255))
        self.rect = self.image.get_rect(center=(shot_object.rect.x, shot_object.rect.y))
        self.current_score = new_score


    def update(self):
        if self.show:
            self.show_time += 1
            self.screen.blit(self.image, self.rect)
            if self.show_time == self.max_show_time:
                self.max_show_y -= 5
                self.rect.y -= 5

                if self.max_show_y == 0:
                    self.show = False
                    self.kill()
                else:
                    self.show_time = 0


    def draw_text(self, text, size, pos_x, pos_y):
        font = pygame.font.SysFont('Comic Sans MS', size)
        button_text = font.render(text, True, (0, 1, 1))
        button_rect = button_text.get_rect()
        button_rect.center = (pos_x, pos_y)

        self.screen.blit(button_text, button_rect)


class ScoreManager:

    def __init__(self, screen):
        self.screen = screen
        self.score = 0

    def update_score(self, sign, new_score):
        if sign == '+':
            print('score before ', self.score)
            self.score += new_score
            print('score after ', self.score)
        elif sign == '-':
            self.score -= new_score

    def return_score(self):
        return int(self.score)