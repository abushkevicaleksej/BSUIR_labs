import pygame

class PlayView:
    def __init__(self, screen, sky, hills, castle, green):
        self.screen = screen
        self.sky = sky
        self.hills = hills
        self.castle = castle
        self.green = green

    def render_background(self, camera1, camera2, camera3, camera4):
        self.screen.fill((90, 100, 45))
        self.screen.blit(self.sky, (-camera1.rect[0], camera1.rect[1]))
        self.screen.blit(self.hills, (-camera2.rect[0], camera2.rect[1]))
        self.screen.blit(self.castle, (-camera3.rect[0], camera3.rect[1]))
        self.screen.blit(self.green, (-camera4.rect[0], camera4.rect[1]))

    def render_chickens(self, chickens_small_group, chickens_mid_group, chickens_big_group):
        chickens_small_group.draw(self.screen)
        chickens_mid_group.draw(self.screen)
        chickens_big_group.draw(self.screen)

    def render_other_elements(self, pumpkin, mill, sign_post, scores_group, trees, buttons, big_chicken_group, ammo_group, cursor_group, play_time, score_manager, dt, ammo_count):
        pumpkin.update('no')
        mill.update('no')
        sign_post.update('no')
        scores_group.update()
        trees.update('no')
        buttons.draw_text(f'Time: {90 - play_time}', 30, 70, 20)
        buttons.draw_text(f'Score: {score_manager.return_score()}', 30, 710, 20)
        big_chicken_group.update('no')
        ammo_group.update(dt, ammo_count)
        cursor_group.draw(self.screen)
        cursor_group.update()

    def update_display(self):
        pygame.display.flip()