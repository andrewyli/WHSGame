import pygame, sys, random, time, pygame.mixer, pygame.font
from Player import Player
from Escobro import Escobro
from nerd import Nerd
from Jock import Jock
from Preppy import Prep
from pygame.locals import *
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
pygame.init()
pygame.mixer.init()
pygame.font.init()
size = width, height = 640, 480

screen = pygame.display.set_mode(size)
title = pygame.image.load("title page.png")
room = pygame.image.load("Room1/Room1.bmp")
startButton = pygame.image.load("Buttons/Start.png")
PORTAL_SWAG = ((35, 30), (width - 70, 30), (35, height - 95), (width - 70, height - 95))
STORY_SWAG = (
"""
Escobro: Welcome to Freshman Year!\n
Come find me in the Guidance Office.\n
We need to discuss your classes! \n
Goal: get to the Physics classroom\n
before Escobro finds you
""",
"""
Escobro: You can't escape me!\n 
Mr. Davidson told me that \n
Dr. Korsunsky said that you\n
are a bad kid. Hah! We need\n
to talk about your classes!\n
Goal: run up to the Library \n
and seek the shelter of the \n
great Ms. Hanson at Res-Tech\n
""",
"""
Escobro: Fine. I admit, you\n
avoided me thus far. BUT NOT\n
FOR LONG! You didnt get \n
recommended for Honors English\n
from Ms. Chaimanis. So you have\n
to meet me in the guidance office\n
to get your form signed.\n
Goal: You have to go to the\n
Guidance Office to get signature,\n
but run immediately to\n
English/History office to get\n
Ms. Lemons' signature.\n
""",
"""
Escobro: How stupid can you\n
be? After you glued a mouse to\n
the ceiling of the Library,\n
Ms. Hanson hates you. Now, I\n
will have to find you and talk\n
about what and why you did.\n
WHY?!?!?!?!\n
Goal: Escape Mr. Escobar, \n
Ms. Hanson, Mr. Parker. . .\n
""",
"""
Escobro: Congratulations on\n 
completing Freshman Year! Dont\n
worry - Ill see you next year.\n

""")


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

quitButton = pygame.image.load("Buttons/QuitButton.png")

start = Button(startButton, width / 2, (6 * height / 7) - 46, 169, 46, 0)
quitGame = Button(quitButton, width / 2, 6 * height / 7, 169, 46, 0)

chars = []
buttons = []
previewNerd = pygame.image.load("Sprites/previewNerd.png")
previewJock = pygame.image.load("Sprites/previewJock.png")
previewPreppy = pygame.image.load("Sprites/previewPreppy.png")
nerdButton = pygame.image.load("Buttons/NerdButton.png")
jockButton = pygame.image.load("Buttons/JockButton.png")
prepButton = pygame.image.load("Buttons/PrepButton.png")


def displayStory(text, screen):
    swagfont = pygame.font.SysFont("trajan", 40)
    screen.fill((0, 0, 0))
    lines = text.splitlines()
    for i in range(len(lines)):
        line = lines[i]
        swag = swagfont.render(line, 1, (255, 255, 255))
        screen.blit(swag, (0, 18 * i))
    pygame.display.flip()
    pygame.time.delay(10000)


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


player_img = pygame.image.load("Sprites/Nerd.png")
background = pygame.image.load("Room1/Room1.bmp").convert()
escobroSprite = pygame.image.load("Sprites/Escobro.png")

menuButton = pygame.image.load("Buttons/MenuButton.png")
toMenu = Button(menuButton, width / 2, 3 * height / 5, 169, 46, 4)


"""
Beginning of the main loop of the game.
"""

swagfont = pygame.font.SysFont("trojan", 20)
while True:

    begin = False

    background = pygame.image.load("Room1/Room1.bmp").convert()

    pygame.mixer.music.load("title screen.ogg")
    pygame.mixer.music.play(-1)

    while not begin:
        screen.blit(title, (0, 0))
        screen.blit(start.image, start.rect)
        screen.blit(quitGame.image, quitGame.rect)
        if start.checkClick():
            begin = True
        if quitGame.checkClick():
            sys.exit()
        pygame.display.update()
        pygame.event.pump()

    characterSelected = ""
    endCharacterSelect = False

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

    if characterSelected == "Nerd":
        player_img = pygame.image.load("Sprites/Nerd.png")
        p = Nerd(player_img, [0, 0], 0, 2, True, False)
    if characterSelected == "Jock":
        player_img = pygame.image.load("Sprites/Jock.png")
        p = Jock(player_img, [0, 0], 0, 2, True, False)
    if characterSelected == "Prep":
        player_img = pygame.image.load("Sprites/Preppy.png")
        p = Prep(player_img, [0, 0], 0, 2, True, False)
    escobro = Escobro(40, 40, p, escobroSprite)
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("1st sem.ogg")
    pygame.mixer.music.play(-1)
    lost = False
    for i in range(5):
        displayStory(STORY_SWAG[i], screen)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            screen.blit(background, (0, 0))
            if i < 4:
                screen.blit(pygame.image.load("Portal.png"), PORTAL_SWAG[i])
                if p.isAtPortal(PORTAL_SWAG[i]):
                    break
            elif i == 4:
                break
            cooldown = swagfont.render(p.text, 1, (242, 100, 68))
            screen.blit(cooldown, (30, SCREEN_HEIGHT - 25))
            p.update(screen)
            e_contact = escobro.update(screen)
            if e_contact:
                lost = True
                break
            pygame.display.update()
        if lost:
            break
    if lost:
        background = pygame.image.load("end notice.jpg").convert()
        pygame.mixer.music.fadeout(2000)
        pygame.mixer.music.load("game over.ogg")
        pygame.mixer.music.play(-1)

        while True:
            screen.blit(background, (0, 0))
            screen.blit(toMenu.image, toMenu.rect)
            if toMenu.checkClick():
                break
            pygame.display.flip()
            pygame.event.pump()
        
    if characterSelected == "Nerd":
        winImage = pygame.image.load("nerd win.jpg")
    elif characterSelected == "Jock":
        winImage = pygame.image.load("jock win.jpg")
    else:
        winImage = pygame.image.load("prep win.jpg")
    if not lost:
        background = winImage
        screen.blit(background, (0, 0))
        pygame.display.flip()
        time.sleep(10)
    pygame.mixer.music.fadeout(200)
