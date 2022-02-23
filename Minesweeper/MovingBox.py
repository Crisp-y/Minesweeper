# http://www.nerdparadise.com/programming/pygame/part1

import pygame  # Doesn't work because don't have pygame

pygame.init()  # init modules
screen = pygame.display.set_mode((400, 300))  # Width, height of screen
done = False  # Just to quit
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()  # To slow frame rate

while not done:
    for event in pygame.event.get():  # Empties queue list or runs through it
        if event.type == pygame.QUIT:  # When you click the x in the corner
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # If key is pressed and it is the space bar
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()  # Which key is pressed
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3

    if is_blue:  # To change colour of rectangle
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    screen.fill((0, 0, 0))  # Resets screen to RGB
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    # Where to draw, RGB, specific shape with corner coordinates

    pygame.display.flip()  # Updates screen with changes
    clock.tick(60)  # Won't do next thing until 1/60 secs since last clock.tick

# filter(lambda x:'K_' in x, dir(pygame))  To see all the keys that can be pressed
