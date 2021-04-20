# Импорт
import pygame
from files.pys.engine import display

# Инициализация pygame
pygame.init()

# Уровень
class Level:
    # Инициализация
    def __init__(self, image, x, y, scheme):    # Картинка, положение, схема
        self.image = image
        self.x = x
        self.y = y
        self.scheme = scheme

    # Вывод на экран
    def set(self):
        display.blit(self.image, (self.x, self.y))

    # Получение информации
    def get(self):
        return [self.image, self.x, self.y, self.scheme]
