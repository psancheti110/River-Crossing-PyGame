#config file
# import the pygame module
import pygame
import math
import os
import sys
import random
# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *

pygame.init()

#pygame.mixer.music.load('gm.ogg')
#pygame.mixer.music.play(-1)

over_font = pygame.font.Font('freesansbold.ttf', 64)
score_font = pygame.font.Font('freesansbold.ttf', 30)

p1_text = over_font.render("Player 1 Wins", True, (255, 255, 255))
p2_text = over_font.render("Player 2 Wins", True, (255, 255, 255))
tie_text = over_font.render("Tie", True, (255, 255, 255))

w1_text = over_font.render("Player 1 Wins: ", True, (255, 255, 255))
w2_text = over_font.render("Player 2 Wins: ", True, (255, 255, 255))

score_text = score_font.render("Time deduction: ", 1, (0, 0, 0))
score1_text = score_font.render("Player 1 Score: ", 1, (0, 0, 0))
score2_text = score_font.render("Player 2 Score: ", 1, (0, 0, 0))

start_text = score_font.render("Start", 1, (255, 255, 255))
end_text = score_font.render("End", 1, (255, 255, 255))