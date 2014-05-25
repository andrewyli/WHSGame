import pygame
import sys
import math
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Player(pygame.sprite.Sprite):  # takes stuff from Sprite

    def __init__(self, image, speed, direction, movespeed, visible, sprint):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # rect is for blitting
        self.direction = direction  # direction (N, S, E, W)
        self.speed = speed  # speed tuple
        self.movespeed = movespeed  # ignore
        self.visible = visible  # for stealth mode
        self.startCooldown = None  # for timing
        self.cooldown = 5000
        self.sprint = sprint

    def update(self, surface):  # main function called in loop of main
        event = pygame.event.get()  # get an event
        self.changeSpeed(event)  # move and change speed based on this
        surface.blit(self.image, self.rect)  # display

    def changeSpeed(self, events):  # for all events, check if its the type required
        for event in events:
            if event.type == QUIT:
                sys.exit()
            # elif event.type == pygame.KEYDOWN:
            if event.type == KEYDOWN:
                if event.key == pygame.K_RIGHT:  # rotate clockwise
                    self.image = pygame.transform.rotate(self.image, -90)
                    self.direction = (self.direction + 90) % 360
                if event.key == pygame.K_LEFT:  # rotate counter clockwise
                    self.image = pygame.transform.rotate(self.image, 90)
                    self.direction = (self.direction - 90) % 360
                if event.key == pygame.K_UP:  # move forward in current direction
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
        pygame.event.clear()  # no idea what this does

    def move(self):  # move 10 times, delay between little movements
        for i in range(10):
            if (self.canMove()):
                self.rect = self.rect.move(self.speed)
                pygame.time.delay(5)

    def canMove(self):  # if we're not running into a wall, pixels precomputed
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
            if self.rect.left > 30:
                return True
            return False

    def isAtPortal(self, portalPos):
        x = self.rect.x
        y = self.rect.y
        if math.sqrt((x - portalPos[0]) ** 2 + (y - portalPos[1]) ** 2) <= 20:
            return True
        else:
            return False
