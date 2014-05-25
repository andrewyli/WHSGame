import pygame
from pygame.locals import *
PACE = 20


class Escobro(pygame.sprite.Sprite):
    def __init__(self, width, height, target, image):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 1
        self.image = image
        self.target = target
        self.rect = image.get_rect().move(width, height)
        self.counter = 0

    def update(self, surface):
        self.counter = self.counter + 1
        if self.counter % PACE == 0:
            self.move()
        surface.blit(self.image, self.rect)
        return self.checkContact()

    def move(self):
        self.xtarget = (self.target.rect.left + self.target.rect.right) / 2
        self.ytarget = (self.target.rect.top + self.target.rect.bottom) / 2
        if abs(self.xtarget - ((self.rect.right + self.rect.left) / 2)) > abs(self.ytarget - ((self.rect.bottom + self.rect.top) / 2)) and self.target.visible:
            self.yspeed = 0
            if ((self.rect.right + self.rect.left) / 2) > self.xtarget:
                self.xspeed = -self.speed
            else:
                self.xspeed = self.speed
        elif self.target.visible:
            self.xspeed = 0
            if ((self.rect.bottom + self.rect.top) / 2) > self.ytarget:
                self.yspeed = -self.speed
            else:
                self.yspeed = self.speed
        if self.target.visible:
            self.rect = self.rect.move(self.xspeed, self.yspeed)

    def checkContact(self):
        if (abs(((self.rect.left + self.rect.right) / 2) - ((self.target.rect.left + self.target.rect.right) / 2))) < 30 and abs(((self.rect.top + self.rect.bottom) / 2) - ((self.target.rect.top + self.target.rect.bottom) / 2)) < 30:
            return True
