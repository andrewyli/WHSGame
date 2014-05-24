import math
import pygame
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Player(pygame.sprite.Sprite):

    def __init__(self, image, x, y, speed, direction, movespeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.xPos = x
        self.yPos = y
        self.direction = direction
        self.speed = speed
        self.movespeed = movespeed
    def update(self, surface):
        self.changeSpeed()
        self.move()
        surface.blit(self.image, self.rect)

    def changeSpeed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    self.image = pygame.transform.rotate(self.image, -90)
                    self.direction = (self.direction + 90) % 360
                if keys[pygame.K_LEFT]:
                    self.image = pygame.transform.rotate(self.image, 90)
                    self.direction = (self.direction - 90) % 360
                if keys[pygame.K_UP]:
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
                if keys[pygame.K_DOWN]:
                    if self.direction == 180:
                        self.speed[0] = 0
                        self.speed[1] = -self.movespeed
                    if self.direction == 270:
                        self.speed[0] = self.movespeed
                        self.speed[1] = 0
                    if self.direction == 0:
                        self.speed[0] = 0
                        self.speed[1] = self.movespeed
                    if self.direction == 90:
                        self.speed[0] = -self.movespeed
                        self.speed[1] = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.speed = [0, 0]

    def move(self):
        self.rect = self.rect.move(self.speed)
