import pygame, sys, random, time, pygame.mixer, pygame.font
from Player import Player
from Escobro import Escobro
from nerd import Nerd
from Jock import Jock
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.font.init()
size = width, height = 640, 480

screen = pygame.display.set_mode(size)
title = pygame.image.load("title page.png")
room = pygame.image.load("Room1/Room1.bmp")
startButton = pygame.image.load("Buttons/Start.png")
STORY_SWAG = (
"""
Escobro: Welcome to Freshman Year! Come find me in the Guidance Office.
We need to discuss your classes! 
Goal: get to the Physics classroom before Escobro finds you"
""",
"""
Escobro: You can't escape me! Mr. Davidson told me that Dr. Korsunsky said that you
are a bad kid. Hah! We need to talk about your classes!
Goal: run up to the Library and seek the shelter of the great Ms. Hanson at Res-Tech
""",
"""
Escobro: Fine. I admit, you avoided me thus far. BUT NOT FOR LONG! You didnt get 
recommended for Honors English from Ms. Chaimanis. So you have to meet me in the
guidance office to get your form signed.
Goal: You have to go to the Guidance Office to get signature, but run immediately to
English/History office to get Ms. Lemons' signature.
""",
"""
Escobro: How stupid can you be? After you glued a mouse to the ceiling of the Library,
Ms. Hanson hates you. Now, I will have to find you and talk about what and why you did.
WHY?!?!?!?!
Goal: Escape Mr. Escobar, Ms. Hanson, Mr. Parker. . .
""",
"""
Escobro: Congratulations on completing Freshman Year! Dont worry - Ill see you next year.

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
	swagfont = SysFont("trojan", 50)
	screen.fill((0, 0, 0))
	for i in range(256):
		swag = swagfont.render(text, 1, (255, 255, 255))
		swag.set_alphas(i)
		screen.blit(swag)
		pygame.display.flip()
		time.delay(5)
	time.delay(20000)
	for i in range(256):
		swag = swagfont.render(text, 1, (255, 255, 255))
		swag.set_alphas(255 - i)
		screen.blit(swag)
		pygame.display.flip()
		time.delay(55)
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

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

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

    p = Nerd(player_img, [0, 0], 0, 2, True, False)
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
        displayStory(STORY_SWAG[i])
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            screen.blit(background, (0, 0))
            cooldown = swagfont.render(p.text, 1, (242, 100, 68))
            screen.blit(cooldown, (30, SCREEN_HEIGHT - 25))
            p.update(screen)
            e_contact = escobro.update(screen)
            if e_contact:
                lost = True
            pygame.display.update()
            if lost:
                break
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
    pygame.time.delay(500)
