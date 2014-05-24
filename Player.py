import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):

    def __init__(self, image, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.xPos = x
        self.yPos = y
        self.dx = dx
        self.dy = dy

    def update(self, surface):
        self.changeSpeed()
        self.move()
        surface.blit(self.image, self.rect)

    def changeSpeed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.dx = 0.5
                    print "right"
                if event.key == pygame.K_LEFT:
                    self.dx = -0.5
                    print "left"
                if event.key == pygame.K_DOWN:
                    self.dy = 0.5
                    print "down"
                if event.key == pygame.K_UP:
                    self.dy = -0.5
                    print "up"
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.dy = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.dx = 0

    def move(self):
        self.rect = self.rect.move([self.dx, self.dy])
