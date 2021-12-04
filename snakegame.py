import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()


# we will declare global constant definitions

speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE     # we will keep both food and size of snake game
SEPARATION = 10     # separation between two pixels
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP":1, "DOWN":2, "LEFT":3, "RIGHT":4}


# we will initialize screen
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH), pygame.HWSURFACE)
# we have used hw surface which stands for hardware surface refers to using memory on the video card for storing
# draws as opposed to main memory

# Resources
score_font = pygame.font.Font(None, 38)
score_numb_font = pygame.font.Font(None, 28)
game_over_font = pygame.font.Font(None, 48)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ", 1, pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0, 0 , 0)   # we will fill background color as black
black = pygame.Color(0, 0 ,0)

