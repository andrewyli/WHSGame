import pygame
from pygame.locals import *

class Nerd(Player):
    def __init__(self, image, speed, direction, movespeed):
        Player.__init__(self, image, speed, direction, movespeed)
        self.movespeed = 2*movespeed/3
    def update(self, surface):
        Player.update(self, surface)
        event = pygame.event.get()
        if event.type = KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.visible:
                    self.visible = False


