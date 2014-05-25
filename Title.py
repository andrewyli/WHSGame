import pygame
import sys
import random
import Title
from pygame.locals import *
pygame.init()

size = width, height = 640, 480

screen = pygame.display.set_mode(size)
title = pygame.image.load("Art/title page.png")
startButton = pygame.image.load("Art/startbutton.png")
begin = False


class Button:
    def __init__(self, image, x, y, width, height): 
        # x and y are center of button. width and height are width and height of button icon
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = image.get_rect().move(x - (width / 2), y - (height / 2))

    def checkClick(self):
        mousex, mousey = pygame.mouse.get_pos()
        m1, m2, m3 = pygame.mouse.get_pressed()
        if m1 and mousex - self.rect.left <= self.width and mousex - self.rect.left >= 0 and mousey - self.rect.top <= self.height and mousey - self.rect.top >= 0:
            return True


def run():
    start = Button(startButton, width / 2, 6 * height / 7, 169, 46)
    global begin
    while not begin:
        screen.blit(title, (0, 0))
        screen.blit(start.image, start.rect)
        start.checkClick()
        if start.checkClick():
            begin = True
        pygame.display.update()
        pygame.event.pump()

run()
