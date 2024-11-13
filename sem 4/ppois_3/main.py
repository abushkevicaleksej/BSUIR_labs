import pygame
from model.settings.game import Game
from model.settings.config import ConfigClass
from model.settings.game_setup import GameSetup

config = ConfigClass(config_file='config.json')
setup = GameSetup(config)
game = Game(setup)

if __name__ == '__main__':
    print('START GAME')
    game.start_game()
pygame.quit()

