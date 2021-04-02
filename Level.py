import pygame
from engine import display

class Level:
    def __init__(self, image, x, y, scheme):
        self.image = image
        self.x = x
        self.y = y
        self.scheme = scheme

    def set(self):
        display.blit(self.image, (self.x, self.y))

    def get(self):
        return [self.image, self.x, self.y]
