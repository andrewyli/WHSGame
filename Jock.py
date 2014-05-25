import pygame
from pygame.locals import *


class Jock(Player):
    def __init__(self, image, speed, direction, movespeed):
        Player.__init__(self, image, speed, direction, movespeed)
        
    def update(self, surface):
        event = pygame.event.get()
        self.changeSpeed(event)
        surface.blit(self.image, self.rect)
        if not self.sprint:
            if self.cooldown < 5000:
                self.cooldown = pygame.time.get_ticks() - self.startCooldown
            
