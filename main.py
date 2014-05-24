import pygame
import sys
import time
from pygame.locals import *
from Player import Player

pygame.init()


def removeWhite(image):
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            if image.get_at((x, y)) == (255, 255, 255, 255):
                image.set_at((x, y), (255, 255, 255, 0))
    return image

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player_img = pygame.image.load("player.png")
background = pygame.image.load("map1.bmp").convert()

p = Player(player_img, 0, 0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.blit(background, (0, 0))
    p.update(screen)
    pygame.display.update()
