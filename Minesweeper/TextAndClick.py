import pygame  # Doesn't work because don't have pygame

pygame.init()  # init modules
screen = pygame.display.set_mode((640, 480))

font = pygame.font.SysFont("comicsansms", 72)  # Use comic san
# font = pygame.font.Font(None, size)  gets default text
text = font.render("Hello, World", True, (0, 128, 0))
# Creates an image to blip on a surface
# text to show, True for smoth edges? (Antialiasing), colour as usual, opt background)

screen.fill((255, 255, 255))
screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
# Source (variable or coords), dest (coords of corner), area rect for it to draw - haven't got to work
pygame.display.flip()
pygame.time.wait(100)

text2 = font.render("5, 4, 3, 2, 1", True, (0, 128, 0))
screen.blit(text2, (0, 0))  # Put in the top left (0, 0). Adjust size at the start
pygame.display.flip()
pygame.time.wait(100)

# !!! Cached text so only make it once
_cached_text = {}


def create_text(text1, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text1)))
    image = _cached_text.get(key, None)
    if image is None:
        font1 = pygame.font.Font(None, size)
        image = font1.render(text1, True, color)
        _cached_text[key] = image
    return image

# !!! Click mouse for it to happen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:  # If mouse is pressed
            First = create_text('click', "comicsansms", 72, (0, 128, 0))
            screen.fill((255, 255, 255))
            screen.blit(First, (0, 0))  # Put in the top left now. Just adjust size at the start
            pygame.display.flip()
            pygame.time.wait(100)
# event.button 1 is left click, 2 mid, 3 right.
# pygame.MOUSEMOTION is movement
# event.pos is coords of mouse
