import pygame


class BestScoreView:
    def __init__(self):
        self.bg = pygame.transform.scale(pygame.image.load('sources/img/help_background/help_back.png'), (800, 600))
        self.bg_rect = self.bg.get_rect()
        self.font = pygame.font.Font(None, 60)

    def draw(self, screen, buttons, game, cursor_group):
        screen.fill((90, 22, 45))
        screen.blit(self.bg, self.bg_rect)

        buttons.draw_text('Best Score Table', 50, 530, 100)
        buttons.draw_text(f'Name:', 30, 350, 200)
        buttons.draw_text(f'Score:', 30, 650, 200)
        game.highscore.print(350,230)
        buttons.draw_best_score('Main Menu', 40, 140, 550)
        cursor_group.draw(screen)
        cursor_group.update()

