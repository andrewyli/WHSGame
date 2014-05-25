import pygame
import sys
import time
from pygame.locals import *
from Player import Player
from Title import Title

pygame.init()

Title.run()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player_img = pygame.image.load("Art/Sprites/Nerd.png")
background = pygame.image.load("Art/Room1/Room1.bmp").convert()

p = Player(player_img, [0, 0], 0, 2, True)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.blit(background, (0, 0))
    p.update(screen)
    pygame.display.update()
