import pygame  # Doesn't work because don't have pygame

pygame.init()  # init modules
screen = pygame.display.set_mode((400, 300))  # Width, height of screen
done = False  # Just to quit

while not done:
    for event in pygame.event.get():  # Empties queue list?
        if event.type == pygame.QUIT:  # When you click the x in the corner
            done = True

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    # Where to draw, RGB, specific shape with corner coordinates
    pygame.display.flip()  # Updates screen with changes

# http://www.nerdparadise.com/programming/pygame/part1
# Interactivity

is_blue = True

if is_blue: color = (0, 128, 255)
else: color = (255, 100, 0)
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))



if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    is_blue = not is_blue
