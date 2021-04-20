# Импорт
import pygame
from files.pys.engine import display

# Инициализация pygame
pygame.init()

class NPC:
    # Инициализация
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    # Вывод на экран
    def set(self):
        display.blit(self.image, (self.x, self.y))

    # Возможность говорить
    def say(self):
        pass

    # Возможность защищаться
    def defend(self):
        pass

    # Возможность ходить
    def go(self):
        pass
