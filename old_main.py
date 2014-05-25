import pygame
import os
import sys
import time
from pygame.locals import *
from Player import Player
import Title

pygame.init()

os.system("python Title.py")

f = open("output.txt", "r")
character_type = f.read()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if character_type == "Nerd":
    player_img = pygame.image.load("Sprites/Nerd.png")
if character_type == "Jock":
    player_img = pygame.image.load("Sprites/Jock.png")
if character_type == "Prep":
    player_img = pygame.image.load("Sprites/Prep.png")

background = pygame.image.load("Room1/Room1.bmp").convert()

p = Player(player_img, [0, 0], 0, 2, True)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.blit(background, (0, 0))
    p.update(screen)
    pygame.display.update()
