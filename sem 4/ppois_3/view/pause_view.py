
import pygame

class PauseView:
    def __init__(self):
        self.bg = pygame.transform.scale(pygame.image.load('sources/img/pause_background/pause.png'), (800,600))
        self.bg_rect = self.bg.get_rect()
        self.font = pygame.font.Font(None, 60)

    def draw(self, screen, buttons, cursor):
        screen.fill((255, 204, 255))
        screen.blit(self.bg, self.bg_rect)

        di = self.font.render('Main Menu', True, '#FFE80E')
        di_rect = di.get_rect(center=(400, 270))
        buttons.pause_buttons.append(di_rect)
        screen.blit(di, di_rect)

        di2 = self.font.render('Exit', True, '#FFE80E')
        di2_rect = di2.get_rect(center=(400, 370))
        buttons.pause_buttons.append(di2_rect)
        screen.blit(di2, di2_rect)

        cursor.draw(screen)
        cursor.update()
