# Импорт
import pygame
from engine import display

# Инициализация pygame
pygame.init()

# Кристалл
class Crystal:
    # Инициализация
    def __init__(self, image, x, y):
        self.image = image  # Картинка
        self.x = x          # Положение
        self.y = y

    # Вывод
    def set(self):
        display.blit(self.image, (self.x, self.y))

    # Изменить размер
    def transform(self, multx, multy):
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * multx, self.image.get_height() * multy))

    # Получение информации
    def get(self):
        return [self.image, self.x, self.y]

    # Получение позиции
    def get_position(self):
        return [self.x, self.y]
