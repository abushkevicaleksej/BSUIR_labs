from model.settings.states import *
from model.settings.config import ConfigClass
from model.settings.highscore_table import Highscore_table
from model.settings.states import State
class Game:
    def __init__(self, setup):
        self.setup = setup
        self.game_state = MainMenuState(game = self)
        self.save = Save()
        self.scores = 0
        self.username = ''
        self.config = ConfigClass()
        self.highscore = Highscore_table(self.save.get(), self.setup.buttons, self.config)

    def start_game(self):
        self.game_state.enter_new_screen()

    def change_game_state(self, new_state: State):
        if self.game_state == None:
            pass
        self.game_state = new_state
        self.game_state.enter_new_screen()

    def play_game_mode(self):
        self.game_state.play_game_mode()

    def best_game_mode(self):
        self.game_state.best_game_mode()

    def help_game_mode(self):
        self.game_state.help_game_mode()

    def exit_game_mode(self):
        self.game_state.exit_game_mode()