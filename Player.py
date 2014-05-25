import math
import pygame
import sys
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Player(pygame.sprite.Sprite):

    def __init__(self, image, speed, direction, movespeed, visible):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect().move(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.direction = direction
        self.speed = speed
        self.movespeed = movespeed
        self.visible = visible
        self.startCooldown = None
        self.cooldown = 5000

    def update(self, surface):
        event = pygame.event.get()
        self.changeSpeed(event)
        surface.blit(self.image, self.rect)

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
        pygame.event.clear()

    def move(self):
        for i in range(10):
            if (self.canMove()):
                self.rect = self.rect.move(self.speed)
                pygame.time.delay(10)

    def canMove(self):
        if (self.direction == 0):
            if self.rect.top > 30:
                return True
            return False
        if (self.direction == 90):
            if self.rect.right < SCREEN_WIDTH - 30:
                return True
            return False
        if (self.direction == 180):
            if self.rect.bottom < SCREEN_HEIGHT - 30:
                return True
            return False
        if (self.direction == 270):
            if self.rect.left > 35:
                return True
            return False
