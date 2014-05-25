import pygame, sys
from pygame.locals import *



class Escobro(pygame.sprite.Sprite):
    def __init__(self, width, height, target, image):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 4
        self.image = image
        self.target = target
        self.rect = image.get_rect().move(width, height)
    def move(self):
        self.xtarget = (self.target.rect.left + self.target.rect.right) / 2
        self.ytarget = (self.target.rect.top + self.target.rect.bottom) / 2
        if abs(self.xtarget - ((self.rect.right + self.rect.left) / 2 )) > abs(self.ytarget - ((self.rect.bottom + self.rect.top) / 2)):
            self.yspeed = 0
            if ((self.rect.right + self.rect.left) / 2) > self.xtarget:
                self.xspeed = -self.speed
            else:
                self.xspeed = self.speed
        else:
            self.xspeed = 0
            if ((self.rect.bottom + self.rect.top) / 2) > self.ytarget:
                self.yspeed = -self.speed
            else:
                self.yspeed = self.speed
        self.rect = self.rect.move(self.xspeed, self.yspeed)
    def checkContact(self):
        if (abs(((self.rect.left + self.rect.right) / 2) - ((self.target.rect.left + self.target.rect.right) / 2))) < 30 and abs(((self.rect.top + self.rect.bottom) / 2) - ((self.target.rect.top + self.target.rect.bottom) / 2)) < 30:
            sys.exit()
