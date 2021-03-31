import pygame
from engine import display

pygame.init()

class Floor_Part:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def set(self):
        display.blit(self.image, (self.x, self.y))

    def get(self):
        return [self.image, self.x, self.y]
