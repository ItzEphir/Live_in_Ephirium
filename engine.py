import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720

f = open("files/txts/screen.txt", "r")
screen_form = f.read()
f.close()

try:
    screen_form = int(screen_form)
    if screen_form == 0:
        display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif screen_form == 1:
        display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
except ValueError:
    display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen_form = 0

f = open("files/txts/screen.txt", "w")
f.write(str(screen_form))
f.close()

pygame.display.set_caption("Fantasy")

clock = pygame.time.Clock()


def button(x, y, width, height, message, color=0, activeColor=0, colorTitle=(0, 0, 0), activeColorTitle=0,
           hitBoxX=50, hitBoxY=10, font_size=25, image=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if color != 0:
        pygame.draw.rect(display, color, (x, y, width, height))
    printText(message, x + width // 2 - hitBoxX, y + (height // 2 - hitBoxY), colorTitle, font_size)
    if image is not None:
        display.blit(image, (x, y))
    if x < mouse[0] < x + width:
        if y < mouse[1] < y + height:
            if activeColor != 0:
                pygame.draw.rect(display, activeColor, (x, y, width, height))
            elif color != 0:
                pygame.draw.rect(display, color, (x, y, width, height))
            if activeColorTitle != 0:
                printText(message, x + width // 2 - hitBoxX, y + (height // 2 - hitBoxY), (80, 80, 80),
                          font_size)
            if click[0] == 1:
                pygame.time.delay(120)
                return True


def printText(message, x, y, font_color=(0, 0, 0), font_size=25, background_color=None, font='files/fonts/RUSNeverwinter.ttf', antialiasing=True):
    font_type = pygame.font.Font(font, font_size)
    text = font_type.render(message, antialiasing, font_color, background_color)
    display.blit(text, (int(x), int(y)))
