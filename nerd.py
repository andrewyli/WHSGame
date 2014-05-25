import pygame
from pygame.locals import *


class Nerd(Player):
    def __init__(self, image, speed, direction, movespeed):
        Player.__init__(self, image, speed, direction, movespeed)
        self.movespeed = 2 * movespeed / 3

    def update(self, surface):
        event = pygame.event.get()
        self.changeSpeed(event)
        surface.blit(self.image, self.rect)
        if self.visible:
            if self.cooldown >= 5000:
                self.cooldown = pygame.time.get_ticks() - self.startCooldown
        else:
            self.cooldown = 5000 - pygame.time.get_ticks() + self.startCooldown
        if self.cooldown <= 0:
            self.visible = True
            self.image = pygame.image.load("Sprites/Nerd.png").convert_alpha()

    def changeSpeed(self, events):
        for event in events:
            if event.type == QUIT:
                sys.exit()
            # elif event.type == pygame.KEYDOWN:
            if event.type == KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.image = pygame.transform.rotate(self.image, -90)
                    self.direction = (self.direction + 90) % 360
                if event.key == pygame.K_LEFT:
                    self.image = pygame.transform.rotate(self.image, 90)
                    self.direction = (self.direction - 90) % 360
                if event.key == pygame.K_UP:
                    if self.direction == 0:
                        self.speed[0] = 0
                        self.speed[1] = -self.movespeed
                    if self.direction == 90:
                        self.speed[0] = self.movespeed
                        self.speed[1] = 0
                    if self.direction == 180:
                        self.speed[0] = 0
                        self.speed[1] = self.movespeed
                    if self.direction == 270:
                        self.speed[0] = -self.movespeed
                        self.speed[1] = 0
                    self.move()
                if event.key == pygame.K_SPACE:
                    if self.cooldown == 5000:
                        self.visible = False
                        self.image = pygame.image.load("Sprites/NerdCloak.png").convert_alpha()
                        self.startCooldown = pygame.time.get_ticks()
        pygame.event.clear()
