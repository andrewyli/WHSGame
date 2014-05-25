import pygame, sys, pygame.mixer
import time
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init()
pygame.init() #turn all of pygame on.



pygame.mixer.music.load("laugh.wav")

pygame.mixer.music.play()
time.sleep(10)
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)