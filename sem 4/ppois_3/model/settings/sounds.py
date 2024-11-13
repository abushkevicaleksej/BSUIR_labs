import pygame


class Sound():
    def __init__(self):
        self.button_click_sound = pygame.mixer.Sound('sources/sounds/button_click.ogg')

        self.main_theme_sound = pygame.mixer.Sound('sources/sounds/main_theme.ogg')

        self.type_sound = pygame.mixer.Sound('sources/sounds/type_sound.wav')
        self.ready_after_user_name = pygame.mixer.Sound('sources/sounds/game_start.ogg')

        self.shot_sound = pygame.mixer.Sound('sources/sounds/gun_shot_sound.ogg')
        self.play_background = pygame.mixer.Sound('sources/sounds/ambientloop.ogg')
        self.pumpkin_shot_sound = pygame.mixer.Sound('sources/sounds/pumpkin_shot_sound.ogg')
        self.time_running = pygame.mixer.Sound('sources/sounds/time_running.ogg')
        self.game_over_sound = pygame.mixer.Sound('sources/sounds/game_over.ogg')
        self.big_chicken_pops_up_sound = pygame.mixer.Sound('sources/sounds/big_chicken_pops_up.ogg')
        self.sign_post_sound = pygame.mixer.Sound('sources/sounds/sign_post_sound.ogg')
        self.mill_hit_sound = pygame.mixer.Sound('sources/sounds/mill_hit_sound.ogg')
        self.tree_hit_sound = pygame.mixer.Sound('sources/sounds/treebranch_shot.wav')

        self.chick_hit1 = pygame.mixer.Sound('sources/sounds/chick_hit1.ogg')
        self.chick_hit2 = pygame.mixer.Sound('sources/sounds/chick_hit2.ogg')
        self.chick_hit3 = pygame.mixer.Sound('sources/sounds/chick_hit3.ogg')
        self.chick_hits = []
        self.chick_hits.append(self.chick_hit1)
        self.chick_hits.append(self.chick_hit2)
        self.chick_hits.append(self.chick_hit3)

        self.empty_shot_sound = pygame.mixer.Sound('sources/sounds/empty_shot_sound.ogg')
        self.update_ammo = pygame.mixer.Sound('sources/sounds/update_ammo.ogg')

    def return_chick_hits(self, sound):
        return self.chick_hits[sound]