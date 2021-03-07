#import libraries
import pygame
from pygame.locals import *
import time
import math

#initializing pygame
pygame.init()

#initializing pygame window
WIDTH = 600
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Corgi Fest")

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

##loading the images
opening = pygame.image.load('startScreen.png')
room = pygame.image.load('room.png')

#setting fonts
END_FONT = pygame.font.SysFont('courier', 40)

#define functions
#start screen
def game_opening():
    win.blit(opening,(0,0))
    pygame.display.update()
    time.sleep(1)

#end screen
def display_message(content):
    pygame.time.delay(500)
    win.fill(BLACK)
    end_text = END_FONT.render(content, 1, RED)
    win.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)

#main loop
def main():
    game_opening()

    global images

    images = []
    

    run = True


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)

        render()



while True:
    if __name__ == '__main__':
        main()