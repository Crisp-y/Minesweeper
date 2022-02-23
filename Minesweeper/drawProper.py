import pygame


def drawGrid(array):  # !!! Adjustable based on a list or row and column values
    pygame.init()  # init modules
    screen = pygame.display.set_mode((1000, 1000))  # Width, height of screen
    blue = (0, 128, 255)
    orange = (255, 100, 0)
    screen.fill((255, 255, 255))
    rows = len(array)
    columns = len(array[0])
    pygame.time.wait(50)
    pygame.draw.rect(screen, blue, pygame.Rect(5, 5, 50*columns, 50*rows), 10)
    pygame.display.flip()
    for every in range(0, rows):  # Cycles through whole list to draw each box.
        for each in range(0, columns):
            pygame.draw.rect(screen, orange, pygame.Rect(each * 50 + 7, every * 50 + 7, 45, 45))  # Moves along for list
            # + 5 when outer thickness was 5 left weird gaps
            # + 7 with outer thickness as 10 seems good.
            # Might be issues when scaling up individual square sizes
            pygame.display.flip()
            pygame.time.wait(10)
    pygame.display.flip()
    pygame.draw.rect(screen, blue, pygame.Rect(5, 5, 50 * columns, 50 * rows), 10)
    pygame.display.flip()

    k = True
    while k:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                k = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    k = False
                    pygame.quit()
