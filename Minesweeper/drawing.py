import pygame

pygame.init()  # init modules
screen = pygame.display.set_mode((1000, 1000))  # Width, height of screen
blue = (0, 128, 255)
orange = (255, 100, 0)
pygame.time.wait(50)
grid = [[['A1'], ['A2'], ['A2'], ['A2']], [['B1'], ['B2']], [['C1'], ['C2']], [['C1'], ['C2']]]
rows = len(grid)
columns = len(grid[0])
# Testing outlines and grids

screen.fill((255, 255, 255))
pygame.draw.rect(screen, blue, pygame.Rect(5, 5, 100, 100), 10)  # 10 for thickness for an outline. Large grid
pygame.display.flip()
pygame.time.wait(50)
pygame.draw.rect(screen, blue, pygame.Rect(5, 5, 50, 50), 10)  # Top left, overlaps outer
pygame.draw.rect(screen, blue, pygame.Rect(55, 5, 50, 50), 10)  # Top right, overlaps first
pygame.draw.rect(screen, blue, pygame.Rect(5, 55, 50, 50), 10)  # Bottom Left
pygame.draw.rect(screen, blue, pygame.Rect(55, 55, 50, 50), 10)  # Bottom Right
pygame.display.flip()
pygame.time.wait(200)

# !!! Explosion shape in red
screen.fill((255, 255, 255))
points = [(20, 5), (25, 20), (35, 5), (35, 15), (50, 15), (45, 25), (55, 30), (40, 40), (45, 50), (35, 40), (30, 55), (25, 35), (15, 45), (20, 35), (5, 30), (20, 25)]
pygame.draw.polygon(screen, (255, 0, 0), points)
pygame.display.flip()
pygame.time.wait(400)
# Will be issuse if changing size.
# JPG saved for reference


def drawGrid(array):  # !!! Adjustable based on a list or row and column values
    screen.fill((255, 255, 255))
    rows = len(array)
    columns = len(array[0])

    pygame.draw.rect(screen, blue, pygame.Rect(5, 5, 50*columns, 50*rows), 10)
    pygame.display.flip()
    for every in range(0, rows):  # Cycles through whole list to draw each box.
        for each in range(0, columns):
            pygame.draw.rect(screen, orange, pygame.Rect(each * 50 + 7, every * 50 + 7, 45, 45))  # Moves along for list
            # + 5 when outer thickness was 5 left weird gaps
            # + 7 with outer thickness as 10 seems good.
            # Might be issues when scaling up individual square sizes
            pygame.display.flip()
            pygame.time.wait(200)
    pygame.display.flip()
    pygame.time.wait(200)

# !!! Draws the explosion in the first square
pygame.draw.polygon(screen, (255, 0, 0), points)
pygame.display.flip()
pygame.time.wait(400)
drawGrid(grid)
pygame.draw.circle()
k = True
while k:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, blue, pygame.Rect(5, 5, 50 * columns, 50 * rows), 10)
            pygame.display.flip()
            print("Mouse click")
            print(pygame.mouse.get_pos())
        elif event.type == pygame.QUIT:
            k = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                k = False
                pygame.quit()
print('Out of while')
quit()
exit()
