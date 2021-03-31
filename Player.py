# Импорт
import pygame
from engine import display

# Инициализация pygame
pygame.init()

# Игрок
class Player:
    # Инициализация
    def __init__(self, image, x, y):
        self.image = image  # Картинка
        self.x = x          # Положение
        self.y = y

    # Вывод
    def set(self):
        display.blit(self.image, (self.x, self.y))

    # Определение движения
    def move(self, where, move_to):
        if where == "right_up":
            self.__move_right_up()
        elif where == "right_down":
            self.__move_right_down()
        elif where == "left_up":
            self.__move_left_up()
        elif where == "left_down":
            self.__move_left_down()
        elif where == "up":
            self.__move_up()
        elif where == "down":
            self.__move_down()

    def __move_right_up(self):
        pass

    def __move_left_up(self):
        pass

    def __move_right_down(self):
        pass

    def __move_left_down(self):
        pass

    def __move_down(self):
        pass

    def __move_up(self):
        pass

    def get(self):
        return [self.image, self.x, self.y]
