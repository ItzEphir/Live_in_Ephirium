# Импорт
import pygame
from engine import display

# Инициализация pygame
pygame.init()

# Игрок
class Player:
    # Инициализация
    def __init__(self, image, x, y, sex=0):
        self.__image = image  # Картинка
        self.__x = x          # Положение
        self.__y = y
        self.__sex = sex

    # Вывод
    def set(self):
        display.blit(self.__image, (self.__x, self.__y))

    # Определение движения
    def move(self, where):
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
        self.__x += 114
        self.__y -= 45
        self.change_image(pygame.image.load("files/images/player/boy/boy_right.png"))

    def __move_left_up(self):
        self.__x -= 114
        self.__y -= 45
        self.change_image(pygame.image.load("files/images/player/boy/boy_left.png"))

    def __move_right_down(self):
        self.__x += 114
        self.__y += 45
        self.change_image(pygame.image.load("files/images/player/boy/boy_right.png"))

    def __move_left_down(self):
        self.__x -= 114
        self.__y += 45
        self.change_image(pygame.image.load("files/images/player/boy/boy_left.png"))

    def __move_down(self):
        self.__y += 90
        self.change_image(pygame.image.load("files/images/player/boy/boy_forward.png"))

    def __move_up(self):
        self.__y -= 90
        self.change_image(pygame.image.load("files/images/player/boy/boy_behind.png"))

    # Изменить картинку
    def change_image(self, image):
        self.__image = image

    # Атака!!!!
    def attack(self):
        pass

    # Получение всей инофрмации
    def get(self):
        return [self.__image, self.__x, self.__y]

    # Получение только координат
    def get_coor(self):
        return self.__x, self.__y
