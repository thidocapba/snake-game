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


# for clock at the left corner
gameClock = pygame.time.Clock()


# we will define keys

def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            # for exit
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            # if we want to continue playing again
            elif event.key == pygame.K_y:
                return "yes"
            # if we don't want to play game
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)

def endGame():
    message = game_over_font.render("Game Over", 1, pygame.Color("white"))
    message_play_again = play_again_font.render("Play Again ? (Y/N)", 1, pygame.Color("green"))
    screen.blit(message, (320, 240))
    screen.blit(message_play_again, (320 + 12, 240 + 40))

    pygame.display.flip()
    pygame.display.update()

    mKey = getKey()
    while(mKey != "exit"):
        if(mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        mKey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)

def drawScore(score):
    score_numb = score_numb_font.render(str(score), 1, pygame.Color("red"))
    screen.blit(score_msg, (SCREEN_WIDTH - score_msg_size[0] - 60, 10))
    screen.blit(score_numb, (SCREEN_WIDTH - 45, 14))

def

