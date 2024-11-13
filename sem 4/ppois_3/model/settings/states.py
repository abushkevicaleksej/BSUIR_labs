import os
import pygame.sprite
from random import randint
from loop_imports import *
from controller.loops.play_loop import play_loop
from objects_imports import *
from settings_imports import *
from view.exit_view import ExitView
from view.best_score_view import BestScoreView
from view.help_view import HelpView
from view.pause_view import PauseView
from view.user_name_view import UserNameView
import json


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


class State:
    def back_to_intro_mode(self):
        raise NotImplementedError

    def enter_new_screen(self):
        raise NotImplementedError

    def play_game_mode(self):
        raise NotImplementedError

    def best_game_mode(self):
        raise NotImplementedError

    def help_game_mode(self):
        raise NotImplementedError

    def exit_game_mode(self):
        raise NotImplementedError


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


class MainMenuState(State):
    def __init__(self, game):
        self.game = game

    def enter_new_screen(self):
        pygame.display.set_caption("Moorhuhn")
        chosen_screen = main_menu_loop(self.game.setup.screen, self.game.setup.sounds, self.game.setup.cursor, self.game.setup.cursor_group, self.game.setup.main_buttons)
        if chosen_screen == 1:
            self.game.play_game_mode()
        elif chosen_screen == 2:
            self.game.best_game_mode()
        elif chosen_screen == 3:
            self.game.help_game_mode()
        elif chosen_screen == 4:
            self.game.exit_game_mode()


    def back_to_intro_mode(self):
        pygame.display.set_caption("Moorhuhn")
        chosen_screen = main_menu_loop(self.game.setup.screen, self.game.setup.sounds, self.game.setup.cursor_group, self.game.setup.buttons)
        if chosen_screen == 1:
            self.game.play_game_mode()
        elif chosen_screen == 2:
            self.game.best_game_mode()
        elif chosen_screen == 3:
            self.game.help_game_mode()

    def play_game_mode(self):
        self.game.change_game_state(PlayState(self.game))

    def username_game_mode(self):
        self.game.change_game_state(UserNameState(self.game))

    def best_game_mode(self):
        self.game.change_game_state(BestScoreState(self.game))

    def help_game_mode(self):
        self.game.change_game_state(HelpState(self.game))

    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))

class PlayState(State):
    def __init__(self, game):
        self.game = game
        self.scores = 0
    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(game = self.game))

    def enter_new_screen(self):
        pygame.display.set_caption('PLAY')
        mill = pygame.sprite.Group()
        for i in range(0, 4):
            mill.add(MillChicken(self.game.setup.screen, i))

        ammo = Ammo(self.game.setup.sounds)
        ammo_group = pygame.sprite.Group()
        for i in range(0, 8):
            ammo_group.add(AmmoGroup(self.game.setup.screen, i))


        pumpkin = Pumpkin(self.game.setup.screen)

        sign_post = SignPost(self.game.setup.screen)
        chickens_small_group = pygame.sprite.Group()
        chickens_small_group.add(ChickenSmall(self.game.setup.screen, randint(100, 200)))
        chickens_mid_group = pygame.sprite.Group()
        chickens_mid_group.add(ChickenMiddle(self.game.setup.screen, randint(100, 300)))
        chickens_big_group = pygame.sprite.Group()
        chickens_big_group.add(ChickenBig(self.game.setup.screen, randint(100, 500)))

        scores_group = pygame.sprite.Group()
        score_manager = ScoreManager(self.game.setup.screen)
        scores_group.add(ScoreImgManager(self.game.setup.screen, score_manager))

        big_chicken_group = pygame.sprite.Group()

        check, score = play_loop(self.game.setup.clock, self.game.setup.screen, self.game.setup.sounds, self.game.setup.buttons, self.game.setup.cursor, self.game.setup.cursor_group, chickens_small_group, chickens_mid_group,
                                 chickens_big_group, ammo, ammo_group, score_manager, scores_group, pumpkin, sign_post, big_chicken_group, mill, self.game.config)

        self.game.scores = score
        if check == 1:
            self.game.change_game_state(PauseState(self.game))
        elif check == 2:
            self.game.change_game_state(UserNameState(self.game))

    def play_game_mode(self):
        pass

    def best_game_mode(self):
        self.game.change_game_state(BestScoreState(self.game))

    def help_game_mode(self):
        self.game.change_game_state(HelpState(self.game))

    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))

# USER NAME
class UserNameState(State):
    def __init__(self, game):
        self.game = game

    def enter_new_screen(self):
        view = UserNameView()
        check, user_name = user_name_loop(self.game.setup.screen, self.game.setup.sounds, self.game.scores, view, self.game.config)
        self.game.username = user_name

        if check:
            print('user name: ', user_name)
            self.game.highscore.update(self.game.username,self.game.scores)
            self.game.save.add(self.game.username, self.game.scores)
            self.game.change_game_state(BestScoreState(self.game))


    def back_to_intro_mode(self):
        pass
    def play_game_mode(self):
        pass
    def best_game_mode(self):
        pass
    def help_game_mode(self):
        pass
    def exit_game_mode(self):
        pass

class PauseState(State):
    def __init__(self, game):
        self.game = game

    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(game=self.game))

    def enter_new_screen(self):
        pygame.display.set_caption('PAUSE')
        view = PauseView()
        check = pause_loop(self.game.setup.screen, self.game.setup.sounds, self.game.setup.buttons, self.game.setup.cursor_group, view)
        if check == 1:
            self.game.change_game_state(MainMenuState(self.game))
        elif check == 2:
            self.game.change_game_state(ExitState(self.game))

    def play_game_mode(self):
        pass

    def best_game_mode(self):
        self.game.change_game_state(BestScoreState(self.game))

    def help_game_mode(self):
        self.game.change_game_state(HelpState(self.game))

    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))

class BestScoreState(State):
    def __init__(self, game):
        self.game = game

    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(self.game))

    def enter_new_screen(self):
        pygame.display.set_caption('BEST SCORE TABLE')
        view = BestScoreView()
        new_state = best_score_loop(self.game.setup.screen, self.game.setup.sounds, self.game.setup.cursor_group, self.game.setup.buttons, self.game.username, self.game.scores, self.game, view)

        if new_state:
            self.game.change_game_state(MainMenuState(self.game))

    def play_game_mode(self):
        self.game.change_game_state(PlayState(self.game))

    def best_game_mode(self):
        pass

    def help_game_mode(self):
        self.game.change_game_state(HelpState(self.game))

    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))


class HelpState(State):
    def __init__(self, game):
        self.game = game

    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(self.game))

    def enter_new_screen(self):
        pygame.display.set_caption('HELP INFORMATION')
        view = HelpView()
        check = help_loop(self.game.setup.screen, self.game.setup.sounds, self.game.setup.cursor_group, self.game.setup.buttons, view)
        if check:
            self.game.change_game_state(MainMenuState(self.game))

    def play_game_mode(self):
        self.game.change_game_state(PlayState(self.game))

    def best_game_mode(self):
        self.game.change_game_state(BestScoreState(self.game))

    def help_game_mode(self):
        pass
    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))


class Save:
    def __init__(self):
        self.file = 'highscore.json'
        self.data = self._load()

    def _load(self):
        if os.path.exists(self.file):
            with open(self.file, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return {}

    def save(self, table):
        self.data['score'] = table
        self._write()

    def add(self, name, value):
        self.data[name] = value
        self._write()

    def _write(self):
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
    def get(self):
        return self.data


class Highscore_table:
    def __init__(self, table, buttons, config):
        self.hs_table = table
        self.buttons = buttons
        self.config = config

    def update(self, name, score):
        self.hs_table[name] = score
        if len(self.hs_table) > self.config.get('max_records', 5):
            sorted_scores = sorted(self.hs_table.items(), key=lambda item: item[1], reverse=True)
            self.hs_table = dict(sorted_scores[:self.config.get('max_records', 5)])

    def print(self, x, y):
        step_x = 300
        step_y = 30
        sorted_scores = sorted(self.hs_table.items(), key=lambda item: item[1], reverse=True)[:self.config.get('max_records', 5)]
        for name, score in sorted_scores:
            self.buttons.draw_text(name, 30, x, y)
            self.buttons.draw_text(str(score), 30, x + step_x, y)
            y += step_y


class ConfigClass:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config_dict = {}
        self.readFromFile()

    def readFromFile(self):
        with open(self.config_file, 'r', encoding='utf-8') as config_file:
            self.config_dict = json.load(config_file)

    def get(self, key, default=None):
        return self.config_dict.get(key, default)
# EXIT
class ExitState(State):
    def __init__(self, game):
        self.game = game

    # -> Main Menu
    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(self.game))

    # we work here
    def enter_new_screen(self):
        pygame.display.set_caption('EXIT')
        view = ExitView()
        check = exit_loop(self.game.setup.screen, self.game.setup.sounds, self.game.setup.cursor_group, self.game.setup.buttons, view)
        if check == 1:
            pygame.quit()
        elif check == 2:
            self.game.change_game_state(MainMenuState(self.game))
        elif check == 0:
            self.game.change_game_state(MainMenuState(self.game))

    def play_game_mode(self):
        pass
    def best_game_mode(self):
        pass
    def help_game_mode(self):
        pass
    def exit_game_mode(self):
        pass
