
import pygame
import random


class ChickenSmall(pygame.sprite.Sprite):
    def __init__(self, screen, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        self.alive = True

        self.dead_index = 0
        self.max_dead_time = 2
        self.dead_time = 0

        self.fly_index = 0
        self.max_fly_time = 2
        self.fly_time = 0

        self.size = (40,40)
        self.speed = 0.1

        self.direction = 0
        self.img_path = None
        r = random.choice([0,800])
        if r == 0:
            self.direction = 1
            self.img_path = 'sources/img/chicken_flight/chicken1.png'
        else:
            self.direction = -1
            self.img_path = 'sources/img/chicken_flight/chicken1.png'

        self.image = pygame.transform.scale(pygame.image.load(self.img_path).convert_alpha(), self.size)
        self.rect = self.image.get_rect(center=(r,pos_y))

    def update(self, dt, move):

        if self.alive:
            self.fly_time +=1
            self.screen.blit(self.image, self.rect)

            if self.direction == 1:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed*dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed*dt))
                else:
                    self.rect.x += float(self.speed*dt)

                if self.fly_time == self.max_fly_time:
                    self.fly_time = 0
                    self.fly_index += 1
                    if self.fly_index == 13:
                        self.fly_index = 0
                    elif self.fly_index <= 12:
                        path = 'sources/img/chicken_flight/chicken' + str(self.fly_index) + '.png'
                        self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size),True,False)

            else:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed*dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed*dt))
                else:
                    self.rect.x -= float(self.speed * dt)

                if self.fly_time == self.max_fly_time:
                    self.fly_time = 0
                    self.fly_index += 1
                    if self.fly_index == 13:
                        self.fly_index = 0
                    elif self.fly_index <= 12:
                        path = 'sources/img/chicken_flight/chicken' + str(self.fly_index) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)

            if self.rect.y >= 540:
                self.kill()
            elif self.rect.x >= 4000:
                self.kill()
            if  self.rect.x == -4000:
                self.kill()

        if not self.alive:
            self.dead_time += 1
            self.rect.y += float(self.speed * dt)

            if self.dead_time == self.max_dead_time:
                self.dead_time = 0
                self.dead_index += 1
                if self.dead_index == 9:
                    self.kill()
                elif self.dead_index <= 8:
                    path = 'sources/img/chicken_flight_death/chickendead' + str(self.dead_index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)


class ChickenMiddle(pygame.sprite.Sprite):
    def __init__(self, screen, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        self.alive = True

        self.dead_index = 0
        self.max_dead_time = 2
        self.dead_time = 0

        self.fly_index = 0
        self.max_fly_time = 2
        self.fly_time = 0

        self.size = (60,60)
        self.speed = 0.2

        self.direction = 0
        self.img_path = None
        r = random.choice([0,800])
        if r == 0:
            self.direction = 1
            self.img_path = 'sources/img/chicken_flight/chicken1.png'
        else:
            self.direction = -1
            self.img_path = 'sources/img/chicken_flight/chicken1.png'

        self.image = pygame.transform.scale(pygame.image.load(self.img_path).convert_alpha(), self.size)
        self.rect = self.image.get_rect(center=(r,pos_y))

    def update(self, dt, move):

        if self.alive:
            self.fly_time +=1
            self.screen.blit(self.image, self.rect)

            if self.direction == 1:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed*dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed*dt))
                else:
                    self.rect.x += float(self.speed*dt)

                if self.fly_time == self.max_fly_time:
                    self.fly_time = 0
                    self.fly_index += 1
                    if self.fly_index == 13:
                        self.fly_index = 0
                    elif self.fly_index <= 12:
                        path = 'sources/img/chicken_flight/chicken' + str(self.fly_index) + '.png'
                        self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size),True,False)

            else:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed*dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed*dt))
                else:
                    self.rect.x -= float(self.speed * dt)

                if self.fly_time == self.max_fly_time:
                    self.fly_time = 0
                    self.fly_index += 1
                    if self.fly_index == 13:
                        self.fly_index = 0
                    elif self.fly_index <= 12:
                        path = 'sources/img/chicken_flight/chicken' + str(self.fly_index) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)

            if self.rect.y >= 540:
                self.kill()
            elif self.rect.x >= 4000:
                self.kill()
            if  self.rect.x == -4000:
                self.kill()

        if not self.alive:
            self.dead_time += 1
            self.rect.y += float(self.speed * dt)

            if self.dead_time == self.max_dead_time:
                self.dead_time = 0
                self.dead_index += 1
                if self.dead_index == 9:
                    self.kill()
                elif self.dead_index <= 8:
                    path = 'sources/img/chicken_flight_death/chickendead' + str(self.dead_index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)


class ChickenBig(pygame.sprite.Sprite):
    def __init__(self, screen, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        self.alive = True

        self.dead_index = 0
        self.max_dead_time = 2
        self.dead_time = 0

        self.fly_index = 0
        self.max_fly_time = 2
        self.fly_time = 0

        self.size = (80,80)
        self.speed = 0.2

        self.direction = 0
        self.img_path = None
        r = random.choice([0,800])
        if r == 0:
            self.direction = 1
            self.img_path = 'sources/img/chicken_flight/chicken1.png'
        else:
            self.direction = -1
            self.img_path = 'sources/img/chicken_flight/chicken1.png'

        self.image = pygame.transform.scale(pygame.image.load(self.img_path).convert_alpha(), self.size)
        self.rect = self.image.get_rect(center=(r,pos_y))

    def update(self, dt, move):

        if self.alive:
            self.fly_time +=1
            self.screen.blit(self.image, self.rect)

            if self.direction == 1:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed*dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed*dt))
                else:
                    self.rect.x += float(self.speed*dt)

                if self.fly_time == self.max_fly_time:
                    self.fly_time = 0
                    self.fly_index += 1
                    if self.fly_index == 13:
                        self.fly_index = 0
                    elif self.fly_index <= 12:
                        path = 'sources/img/chicken_flight/chicken' + str(self.fly_index) + '.png'
                        self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size),True,False)

            else:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed*dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed*dt))
                else:
                    self.rect.x -= float(self.speed * dt)

                if self.fly_time == self.max_fly_time:
                    self.fly_time = 0
                    self.fly_index += 1
                    if self.fly_index == 13:
                        self.fly_index = 0
                    elif self.fly_index <= 12:
                        path = 'sources/img/chicken_flight/chicken' + str(self.fly_index) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)

            if self.rect.y >= 540:
                self.kill()
            elif self.rect.x >= 4000:
                self.kill()
            if self.rect.x == -4000:
                self.kill()

        if not self.alive:
            self.dead_time += 1
            self.rect.y += float(self.speed * dt)

            if self.dead_time == self.max_dead_time:
                self.dead_time = 0
                self.dead_index += 1
                if self.dead_index == 9:
                    self.kill()
                elif self.dead_index <= 8:
                    path = 'sources/img/chicken_flight_death/chickendead' + str(self.dead_index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)
