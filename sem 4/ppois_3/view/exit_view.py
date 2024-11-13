import pygame


class ExitView:
    def __init__(self):
        self.bg = pygame.transform.scale(pygame.image.load('sources/img/help_background/help_back.png'), (800, 600))
        self.bg_rect = self.bg.get_rect()
        self.font = pygame.font.Font(None, 60)

    def draw(self, screen, buttons, cursor_group):
        screen.fill((90, 22, 45))
        screen.blit(self.bg, self.bg_rect)

        top = self.font.render('Are you sure?', True, '#FFE80E')
        top_rect = top.get_rect(center=(540, 200))
        screen.blit(top, top_rect)

        top1 = self.font.render('Yes', True, '#FFE80E')
        top1_rect = top1.get_rect(center=(530, 280))
        buttons.exit_buttons.append(top1_rect)
        screen.blit(top1, top1_rect)

        top2 = self.font.render('No', True, '#FFE80E')
        top2_rect = top2.get_rect(center=(530, 350))
        buttons.exit_buttons.append(top2_rect)
        screen.blit(top2, top2_rect)

        cursor_group.draw(screen)
        cursor_group.update()
