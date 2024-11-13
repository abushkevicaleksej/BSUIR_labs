import pygame
from model.settings.buttons import *
from model.settings.sounds import Sound
from model.objects.cursor import Cursor

class GameSetup:
    def __init__(self, config):
        pygame.init()
        self.HEIGHT = config.get('height', 600)
        self.WIDTH = config.get('width', 800)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.time.set_timer(pygame.USEREVENT, 4000)
        self.buttons = Button(self.screen)
        self.main_buttons = pygame.sprite.Group()
        for i in range(0, 4):
            self.main_buttons.add(MainMenuButtons(self.screen, i))
        self.sounds = Sound()
        self.cursor = Cursor(self.screen, 'sources/img/cursor/cursor.png')
        self.cursor_group = pygame.sprite.Group()
        self.cursor_group.add(self.cursor)
        self.clock = pygame.time.Clock()