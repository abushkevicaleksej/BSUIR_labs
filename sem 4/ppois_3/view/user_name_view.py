import pygame
from model.settings.buttons import Button

class UserNameView:
    def __init__(self):
        self.bg = pygame.transform.scale(pygame.image.load('sources/img/help_background/help_back.png'), (800, 600))
        self.bg_rect = self.bg.get_rect()
        pygame.font.init()
        self.font = pygame.font.Font(None, 40)
        self.font1 = pygame.font.Font(None, 30)
        self.success_font = pygame.font.Font(None, 50)

    def draw(self, screen, user_name, user_tick, score):
        screen.fill((90, 22, 45))
        screen.blit(self.bg, self.bg_rect)

        b = Button(screen)
        b_d = self.font.render('ENTER USER NAME', True, '#FFE80E')
        b_surf_rect = b_d.get_rect(center=(540, 250))
        screen.blit(b_d, b_surf_rect)

        user_tick -= 1
        if user_tick == 0:
            user_name = user_name[: -1]
        if user_tick == -150:
            user_name += '|'
            user_tick = 150

        user_name_surf = self.font.render(user_name, True, '#FFE80E')
        user_name_rect = pygame.Rect(440, 294, 400, 50)
        screen.blit(user_name_surf, (user_name_rect.x + 10, user_name_rect.y + 10))

        b_surf = self.font1.render('Press ENTER to continue', True, '#FFE80E')
        b_surf_rect = b_surf.get_rect(center=(140, 550))
        screen.blit(b_surf, b_surf_rect)

        if score < 0:
            success_message = self.success_font.render('Game Over! Wear glasses next time!', True, '#FFE80E')
        elif score < 1000:
            success_message = self.success_font.render('Game Over! Looks like you use aim cheat!', True, '#FFE80E')
        else:
            success_message = self.success_font.render('Game Over! Bet you will be more attentive next time!', True, '#FFE80E')
        success_rect = success_message.get_rect(center=(400, 100))
        screen.blit(success_message, success_rect)

        score_message = self.success_font.render(f'Score: {score}', True, '#FFE80E')
        score_rect = score_message.get_rect(center=(400, 150))
        screen.blit(score_message, score_rect)

