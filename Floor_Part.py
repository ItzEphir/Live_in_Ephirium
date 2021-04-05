# Импорт
import pygame
from engine import display

# Инициализация pygame
pygame.init()

class Floor_Part:
    # Инициализация
    def __init__(self, image, x, y):    # Картинка, положение
        self.image = image
        self.x = x
        self.y = y

    # Вывод на экран
    def set(self):
        display.blit(self.image, (self.x, self.y))

    # Получение информации
    def get(self):
        return [self.image, self.x, self.y]
