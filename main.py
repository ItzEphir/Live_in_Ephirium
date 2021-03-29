import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from random import randint as rand
from engine import *
from vars import *
from Player import *

pygame.init()

def load():
    global screen, loaded1, loaded2, floorPart, background, crystal, player, gray, loadFill, loadHalfFill
    display.blit(bg, (0, 0))
    if loaded1 and not loaded2:
        display.blit(loadHalfFill, ((WIDTH - (WIDTH - 40)), HEIGHT - 200))
    elif loaded2:
        display.blit(loadFill, ((WIDTH - (WIDTH - 40)), HEIGHT - 200))
        screen = "Меню"
    display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))
    if loaded1 and not loaded2:
        # Загрузки 2:
        background = pygame.image.load("files/images/background.png")
        background = pygame.transform.scale(background, (background.get_width() * 2, background.get_height() * 2))
        loadFill = pygame.image.load("files/images/loadFill.png")
        loadFill = pygame.transform.scale(loadFill, (loadFill.get_width() * 2, loadFill.get_height() * 2))
        loaded2 = True
    elif not loaded1 and not loaded2:
        # Загрузки 1:
        loadHalfFill = pygame.image.load("files/images/loadHalfFill.png")
        loadHalfFill = pygame.transform.scale(loadHalfFill,
                                              (loadHalfFill.get_width() * 2, loadHalfFill.get_height() * 2))
        loaded1 = True

def loadingBeforePlay():
    global screen, player, gray, floorPart, crystal
    player_image = pygame.image.load("files/images/player.png")
    gray = pygame.image.load("files/images/Gray.png")
    gray = pygame.transform.scale(gray, (gray.get_width() * 2, gray.get_height() * 2))
    floorPart = pygame.image.load("files/images/floorPart.png")
    floorPart = pygame.transform.scale(floorPart, (floorPart.get_width() * 2, floorPart.get_height() * 2))
    crystal = pygame.image.load("files/images/crystal.png")
    player = Player(player_image, 40, 64)


def menu():
    global screen
    display.blit(background, (0, 0))
    if button(WIDTH // 2 - 100, HEIGHT // 2 - 100, 100, 100, "Play"):
        screen = "Играть"
    if keys[pygame.K_ESCAPE]:
        pygame.time.delay(120)
        screen = "Хотите выйти?"

def you_exit():
    global screen
    display.blit(background, (0, 0))

    printText("Do you want to exit?", WIDTH // 2 - 145, HEIGHT // 2 - 112)

    if button(WIDTH // 2 - 175, HEIGHT // 2 - 12, 75, 25, "Yes"):
        return True
    if button(WIDTH // 2 + 100, HEIGHT // 2 - 12, 75, 25, "No"):
        screen = "Меню"
        return False

def beforePlay():
    global screen
    crystalPlace = [rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017), rand(1140, 1245),
                    rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017), rand(1140, 1245)]
    needCrystal = [rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5),
                   rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5)]
    screen = "Играть2"
    return [crystalPlace, needCrystal]

def play(iNeed):
    global screen, player
    display.blit(gray, (0, 0))
    crystalPlace = iNeed[0]
    needCrystal = iNeed[1]
    printFloor()
    printCrystal(crystalPlace, needCrystal)

    player.set()

    if keys[pygame.K_ESCAPE]:
        pygame.time.delay(120)
        screen = "Меню"

def printCrystal(crystalPlace, needCrystal):
    if needCrystal[0] == 1:
        display.blit(crystal, (crystalPlace[0], 0))
    if needCrystal[1] == 1:
        display.blit(crystal, (crystalPlace[1], 0))
    if needCrystal[2] == 1:
        display.blit(crystal, (crystalPlace[2], 0))
    if needCrystal[3] == 1:
        display.blit(crystal, (crystalPlace[3], 0))
    if needCrystal[4] == 1:
        display.blit(crystal, (crystalPlace[4], 0))
    if needCrystal[5] == 1:
        display.blit(crystal, (crystalPlace[5], 0))

    if needCrystal[6] == 1:
        display.blit(crystal, (crystalPlace[6], 645))
    if needCrystal[7] == 1:
        display.blit(crystal, (crystalPlace[7], 645))
    if needCrystal[8] == 1:
        display.blit(crystal, (crystalPlace[8], 645))
    if needCrystal[9] == 1:
        display.blit(crystal, (crystalPlace[9], 645))
    if needCrystal[10] == 1:
        display.blit(crystal, (crystalPlace[10], 645))
    if needCrystal[11] == 1:
        display.blit(crystal, (crystalPlace[11], 645))

def printFloor():
    for i in range(0, 6):
        display.blit(floorPart, (228 * i, 90))
        display.blit(floorPart, (228 * i, 180))
        display.blit(floorPart, (228 * i, 270))
        display.blit(floorPart, (228 * i, 360))
        display.blit(floorPart, (228 * i, 450))
        display.blit(floorPart, (228 * i, 540))
    for i in range(0, 5):
        display.blit(floorPart, (114 + 228 * i, 45))
        display.blit(floorPart, (114 + 228 * i, 45 + 90))
        display.blit(floorPart, (114 + 228 * i, 45 + 180))
        display.blit(floorPart, (114 + 228 * i, 45 + 270))
        display.blit(floorPart, (114 + 228 * i, 45 + 360))
        display.blit(floorPart, (114 + 228 * i, 45 + 450))
        display.blit(floorPart, (114 + 228 * i, 45 + 540))

def game():
    global keys
    game_end = False
    iNeed = []
    while not game_end:
        clock.tick(60)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True

        if screen == 0:
            load()
        elif screen == "Меню":
            menu()
        elif screen == "Хотите выйти?":
            game_end = you_exit()
        elif screen == "Играть":
            iNeed = beforePlay()
        elif screen == "Играть2":
            play(iNeed)

        pygame.display.update()


game()
