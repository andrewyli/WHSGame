import pygame, sys, random, time
from Player import Player
from Escobro import Escobro
from pygame.locals import *
pygame.init()

size = width, height = 640, 480

screen = pygame.display.set_mode(size)
title = pygame.image.load("title page.png")
room = pygame.image.load("Room1/Room1.bmp")
startButton = pygame.image.load("Buttons/Start.png")
begin = False


class Button:
    def __init__(self, image, x, y, width, height, num):
    # x and y are center of button. width and height are width and height of button icon
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = image.get_rect().move(x - (width / 2), y - (height / 2))
        self.num = num

    def checkClick(self):
        mousex, mousey = pygame.mouse.get_pos()
        m1, m2, m3 = pygame.mouse.get_pressed()
        if m1 and mousex - self.rect.left <= self.width and mousex - self.rect.left >= 0 and mousey - self.rect.top <= self.height and mousey - self.rect.top >= 0:
            return True

    def beginClass(self):
        if self.num == 1:
            return "Nerd"
        elif self.num == 2:
            return "Jock"
        elif self.num == 3:
            return "Prep"


start = Button(startButton, width / 2, 6 * height / 7, 169, 46, 0)

while not begin:
    screen.blit(title, (0, 0))
    screen.blit(start.image, start.rect)
    if start.checkClick():
        begin = True
    pygame.display.update()
    pygame.event.pump()

chars = []
buttons = []
previewNerd = pygame.image.load("Sprites/previewNerd.png")
previewJock = pygame.image.load("Sprites/previewJock.png")
previewPreppy = pygame.image.load("Sprites/previewPreppy.png")
nerdButton = pygame.image.load("Buttons/NerdButton.png")
jockButton = pygame.image.load("Buttons/JockButton.png")
prepButton = pygame.image.load("Buttons/PrepButton.png")
characterSelected = ""
endCharacterSelect = False


def classImageChoose(num):
    if num == 0:
        return previewNerd
    elif num == 1:
        return previewJock
    else:
        return previewPreppy


def buttonImageChoose(num):
    if num == 0:
        return nerdButton
    elif num == 1:
        return jockButton
    else:
        return prepButton


class CharacterSelect:
    def __init__(self, image, num):
        self.image = image
        self.x = (num + 1) * width / 4
        self.y = height / 2
        self.rect = image.get_rect().move(self.x - 50, self.y - 50)

for c in range(3):
    sel = CharacterSelect(classImageChoose(c), c)
    chars.append(sel)

for b in range(3):
    but = Button(buttonImageChoose(b), ((b + 1) * width / 4), height / 3, 169, 46, b + 1)
    buttons.append(but)

while not endCharacterSelect:
    screen.blit(room, (0, 0))
    for i in chars:
        screen.blit(i.image, i.rect)
    for i in buttons:
        screen.blit(i.image, i.rect)
        if i.checkClick():
            characterSelected = i.beginClass()
            endCharacterSelect = True
    pygame.display.flip()
    pygame.event.pump()

print "You chose " + characterSelected

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

"""if characterSelected == "Nerd":
    player_img = pygame.image.load("Sprites/Nerd.png")
if characterSelected == "Jock":
    player_img = pygame.image.load("Sprites/Jock.png")
if characterSelected == "Prep":
    player_img = pygame.image.load("Sprites/Preppy.png")"""

player_img = pygame.image.load("Sprites/Nerd.png")
background = pygame.image.load("Room1/Room1.bmp").convert()
escobroSprite = pygame.image.load("Sprites/Escobro Placeholder.png")

p = Player(player_img, [0, 0], 0, 2, True)
escobro = Escobro(40, 40, p, escobroSprite)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.blit(background, (0, 0))
    p.update(screen)
    e_contact = escobro.update(screen)
    if e_contact:
        break
    pygame.display.update()

background = pygame.image.load("end notice.png").convert()

while True:
    screen.blit(background, (0, 0))
