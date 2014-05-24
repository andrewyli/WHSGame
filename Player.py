import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):

    image = pygame.image.load("player.png")
    rect = image.get_rect()
    xPos = 0
    yPos = 0
    dx = 0
    dy = 0

    def __init__(self, image, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.xPos = x
        self.yPos = y
        self.dx = dx
        self.dy = dy

    def update(self):
        self.move()
        
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.dx = 20
                    print "right"
                if event.key == pygame.K_LEFT:
                    self.dx = -20
                    print "left"
                if event.key == pygame.K_DOWN:
                    self.dy = 20
                    print "down"
                if event.key == pygame.K_UP:
                    self.dy = -20
                    print "up"
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.dy = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.dx = 0
