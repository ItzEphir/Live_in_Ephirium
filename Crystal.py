import pygame
from engine import display

pygame.init()

class Crystal:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def set(self):
        display.blit(self.image, (self.x, self.y))

    def transform(self, multx, multy):
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * multx, self.image.get_height() * multy))

    def get_position(self):
        return [self.x, self.y]
