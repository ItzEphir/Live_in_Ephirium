# Импорт
import pygame
from engine import display

# Инициализация pygame
pygame.init()

# Враг
class Enemy:
    # Инициализация
    def __init__(self, image, x, y, sex=0, hp=100):    # Картинка, положение
        self.__image = image
        self.__x = x
        self.__y = y
        self.__sex = sex
        self.__hp = hp

    def set(self):
        display.blit(self.__image, (self.__x, self.__y))

    def move(self, where):
        if where == "right-up":
            self.__move_right_up()
        elif where == "right-down":
            self.__move_right_down()
        elif where == "down":
            self.__move_down()
        elif where == "left-down":
            self.__move_left_down()
        elif where == "left-up":
            self.__move_left_up()
        elif where == "up":
            self.__move_up()

    def __move_right_up(self):
        self.__x += 114
        self.__y -= 45
        if self.__sex == 0:
            self.change_image(pygame.image.load("files/images/player/boy/boy_right.png"))
        elif self.__sex == 1:
            self.change_image(pygame.image.load("files/images/player/girl/girl_right.png"))

    def __move_left_up(self):
        self.__x -= 114
        self.__y -= 45
        if self.__sex == 0:
            self.change_image(pygame.image.load("files/images/player/boy/boy_left.png"))
        elif self.__sex == 1:
            self.change_image(pygame.image.load("files/images/player/girl/girl_left.png"))

    def __move_right_down(self):
        self.__x += 114
        self.__y += 45
        if self.__sex == 0:
            self.change_image(pygame.image.load("files/images/player/boy/boy_right.png"))
        elif self.__sex == 1:
            self.change_image(pygame.image.load("files/images/player/girl/girl_right.png"))

    def __move_left_down(self):
        self.__x -= 114
        self.__y += 45
        if self.__sex == 0:
            self.change_image(pygame.image.load("files/images/player/boy/boy_left.png"))
        elif self.__sex == 1:
            self.change_image(pygame.image.load("files/images/player/girl/girl_left.png"))

    def __move_down(self):
        self.__y += 90
        if self.__sex == 0:
            self.change_image(pygame.image.load("files/images/player/boy/boy_forward.png"))
        elif self.__sex == 1:
            self.change_image(pygame.image.load("files/images/player/girl/girl_forward.png"))

    def __move_up(self):
        self.__y -= 90
        if self.__sex == 0:
            self.change_image(pygame.image.load("files/images/player/boy/boy_behind.png"))
        elif self.__sex == 1:
            self.change_image(pygame.image.load("files/images/player/girl/girl_behind.png"))

    # Изменить картинку
    def change_image(self, image):
        self.__image = image

    def change_hp(self, change):
        self.__hp += change

    def get(self):
        return self.__image, self.__x, self.__y

    def get_coor(self):
        return self.__x, self.__y
