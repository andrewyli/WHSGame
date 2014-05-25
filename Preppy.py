import pygame
from Player import Player
from pygame.locals import *


class Prep(Player):
    def __init__(self, image, speed, direction, movespeed, teleportable):
        Player.__init__(self, image, speed, direction, movespeed, teleport)
        self.text = ""

    def update(self, surface):
        event = pygame.event.get()
        self.changeSpeed(event)
        surface.blit(self.image, self.rect)
        if self.teleport:
            if self.cooldown < 5000:
                self.cooldown = pygame.time.get_ticks() - self.startCooldown - 5000
        else:
            self.cooldown = 5000 - pygame.time.get_ticks() + self.startCooldown
        if self.cooldown <= 0:
            self.teleport = True
            self.text = "Cooldown: " + str(self.cooldown)
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
                        self.teleport = False
                        self.teleportation()
                        self.startCooldown = pygame.time.get_ticks()
    def teleportation(self):
        self.rect = (width - x, height - y)
