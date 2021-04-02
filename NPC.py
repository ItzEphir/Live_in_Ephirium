import pygame
from engine import display

pygame.init()

class NPC:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def set(self):
        display.blit(self.image, (self.x, self.y))

    def say(self):
        pass

    def defend(self):
        pass

    def go(self):
        pass
