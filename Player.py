import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from engine import display

pygame.init()

class Player:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def set(self):
        display.blit(self.image, (self.x, self.y))

    def move(self, where):
        if where == "right_up":
            self.move_right_up()
        elif where == "right_down":
            self.move_right_down()
        elif where == "left_up":
            self.move_left_up()
        elif where == "left_down":
            self.move_left_down()
        elif where == "up":
            self.move_up()
        elif where == "down":
            self.move_down()

    def move_right_up(self):
        pass

    def move_left_up(self):
        pass

    def move_right_down(self):
        pass

    def move_left_down(self):
        pass

    def move_down(self):
        pass

    def move_up(self):
        pass
