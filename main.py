import pygame
from random import randint as rand
from engine import *
from vars import *
from Player import *
from Crystal import *

pygame.init()

def load():
    global screen, loaded1, loaded2, background, loadFill, loadHalfFill
    display.blit(bg, (0, 0))

    if not loaded1 and not loaded2:
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        loadHalfFill = pygame.image.load("files/images/loadHalfFill.png")
        loadHalfFill = pygame.transform.scale(loadHalfFill,
                                              (loadHalfFill.get_width() * 2, loadHalfFill.get_height() * 2))
        loaded1 = True
        return 0
    elif loaded1 and not loaded2:
        display.blit(loadHalfFill, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        background = pygame.image.load("files/images/background.png")
        background = pygame.transform.scale(background, (background.get_width() * 2, background.get_height() * 2))
        loadFill = pygame.image.load("files/images/loadFill.png")
        loadFill = pygame.transform.scale(loadFill, (loadFill.get_width() * 2, loadFill.get_height() * 2))
        loaded2 = True
        return 0
    else:
        display.blit(loadFill, ((WIDTH - (WIDTH - 40)), HEIGHT - 200))
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        loaded1 = False
        loaded2 = False
        screen = "Меню"
        return 0

def loadingBeforePlay():
    global screen, player, gray, floorPart, loaded1, loaded2, player_image
    global crystals, crystalPlace, needCrystal, crystalImage
    display.blit(background, (0, 0))
    if not loaded1 and not loaded2:
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        pygame.time.delay(500)
        player_image = pygame.image.load("files/images/player.png")
        gray = pygame.image.load("files/images/Gray.png")
        gray = pygame.transform.scale(gray, (gray.get_width() * 2, gray.get_height() * 2))
        floorPart = pygame.image.load("files/images/floorPart.png")
        floorPart = pygame.transform.scale(floorPart, (floorPart.get_width() * 2, floorPart.get_height() * 2))
        loaded1 = True
        return 0
    elif loaded1 and not loaded2:
        display.blit(loadHalfFill, ((WIDTH - (WIDTH - 40)), HEIGHT - 200))
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        pygame.time.delay(500)
        crystalImage = pygame.image.load("files/images/crystal.png")
        player = Player(player_image, 40, 64)
        crystalPlace = [rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017), rand(1140, 1245),
                        rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017), rand(1140, 1245)]
        needCrystal = [rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5),
                       rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5)]
        crystals = []
        for i in range(0, 11):
            if i < 6:
                crystals.append(Crystal(crystalImage, crystalPlace[i], 0))
            else:
                crystals.append(Crystal(crystalImage, crystalPlace[i], 645))
        loaded2 = True
        return 0
    else:
        display.blit(loadFill, ((WIDTH - (WIDTH - 40)), HEIGHT - 200))
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        pygame.time.delay(500)
        loaded1 = False
        loaded2 = False
        screen = "Играть2"
        return 0


def menu():
    global screen, escapePressed
    display.blit(background, (0, 0))
    if button(WIDTH // 2 - 100, HEIGHT // 2 - 100, 100, 100, "Play"):
        screen = "Играть"
    if keys[pygame.K_ESCAPE]:
        if not escapePressed:
            escapePressed = True
            pygame.time.delay(120)
    else:
        if escapePressed:
            screen = "Хотите выйти?"
            escapePressed = False

def you_exit():
    global screen
    display.blit(background, (0, 0))

    printText("Do you want to exit?", WIDTH // 2 - 145, HEIGHT // 2 - 112)

    if button(WIDTH // 2 - 175, HEIGHT // 2 - 12, 75, 25, "Yes"):
        return True
    if button(WIDTH // 2 + 100, HEIGHT // 2 - 12, 75, 25, "No"):
        screen = "Меню"
        return False

def play():
    global screen, player, escapePressed
    display.blit(gray, (0, 0))

    printFloor()
    printCrystal()

    player.set()

    if keys[pygame.K_ESCAPE]:
        if not escapePressed:
            escapePressed = True
            pygame.time.delay(120)
    else:
        if escapePressed:
            screen = "Меню"
            escapePressed = False

def printCrystal():
    for i in range(0, 11):
        if needCrystal[i] == 1:
            crystals[i].set()


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
            loadingBeforePlay()
        elif screen == "Играть2":
            play()

        pygame.display.update()


game()
