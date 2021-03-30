import pygame

pygame.init()

screen = 0

loaded1 = False
loaded2 = False

escapePressed = False

loadScreen = pygame.image.load("files/images/loadScreen.png")
loadScreen = pygame.transform.scale(loadScreen, (loadScreen.get_width() * 2, loadScreen.get_height() * 2))
loadHalfFill = None
loadFill = None
bg = pygame.image.load("files/images/bg.png")
bg = pygame.transform.scale(bg, (bg.get_width() * 2, bg.get_height() * 2))

gray = None
floorPart = None
background = None
crystalImage = None
crystalPlace = None
needCrystal = None
player_image = None
player = None
keys = None
