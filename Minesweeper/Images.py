# Part 2 of nerd paradise.

import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
screen.fill((255, 255, 255))  # White screen
image = pygame.image.load('Spoopy2.png')  # Loads picture, not case sens on windows
screen.blit(image, (10, 10))  # Puts picture on screen
pygame.display.flip()  # Refreshes screen
