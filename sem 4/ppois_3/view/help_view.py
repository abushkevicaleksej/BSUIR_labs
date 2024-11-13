import pygame


class HelpView:
    def __init__(self):
        self.bg = pygame.transform.scale(pygame.image.load('sources/img/help_background/help_back.png'), (800,600))
        self.bg_rect = self.bg.get_rect()

        self.mouse1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('sources/img/help_background/mouse-right-click.png').convert_alpha(),(150,100)),True,False)
        self.mouse1_rect = self.mouse1.get_rect(center = (370,150))

        self.space = pygame.transform.scale(pygame.image.load('sources/img/help_background/space.png').convert_alpha(),(150, 160))
        self.space_rect = self.space.get_rect(center=(370, 330))

        self.esc = pygame.transform.scale(pygame.image.load('sources/img/help_background/6.jpg').convert_alpha(), (90, 90))
        self.esc_rect = self.esc.get_rect(center=(370, 500))

        pygame.font.init()
        self.font1 = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 50)
        self.font3 = pygame.font.Font(None, 50)

    def draw(self, screen, cursor_group):
        screen.fill((90, 15, 45))
        screen.blit(self.bg, self.bg_rect)
        screen.blit(self.mouse1,self.mouse1_rect)
        screen.blit(self.space,self.space_rect)
        screen.blit(self.esc,self.esc_rect)

        ier = self.font1.render(' - SHOOT', True, '#FFE80E')
        ier_rect = ier.get_rect(center=(520, 150))
        screen.blit(ier, ier_rect)

        crr = self.font2.render(' - RECHARGE', True, '#FFE80E')
        crr_rect = crr.get_rect(center=(580, 330))
        screen.blit(crr, crr_rect)

        pp = self.font3.render(' - MAIN MENU', True, '#FFE80E')
        pp_rect = pp.get_rect(center=(580, 500))
        screen.blit(pp, pp_rect)

        cursor_group.draw(screen)
        cursor_group.update()
