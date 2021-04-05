# Импорт
import pygame

# Инициализация pygame
pygame.init()

# Высота/Ширина экрана
WIDTH = 1280
HEIGHT = 720

# Открытие файла на проверку настроек экрана
f = open("files/txts/screen.txt", "r")
screen_form = f.read()
f.close()

# Обработка найстройки экрана
try:
    screen_form = int(screen_form)
    if screen_form == 0:
        # FullScreen
        display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif screen_form == 1:
        # Window
        display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
# По умолчанию
except ValueError:
    display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen_form = 0

# Запись настроек экрана в файл
f = open("files/txts/screen.txt", "w")
f.write(str(screen_form))
f.close()

# Название окна
pygame.display.set_caption("Fantasy")

# FPS
clock = pygame.time.Clock()


# Кнопка
def button(x, y, width, height, message, color=0, activeColor=0, colorTitle=(0, 0, 0), activeColorTitle=0,
           hitBoxX=50, hitBoxY=10, font_size=25, image=None, withPlayer=False, player=None):  # Положение кнопки, размер кнопки,
                                                                                # Надпись, цвет, цвет при наведении,
                                                                                # Цвет текста, активный цвет текста,
                                                                                # Регуляровка хитбоксов, размер шрифта,
                                                                                # Картинка кнопки, индекс списка
    # Получение позиции мыши
    mouse = pygame.mouse.get_pos()
    # Получение нажатии мыши
    click = pygame.mouse.get_pressed()

    # Проверка цвета
    if color != 0:
        # Рисование кнопки
        pygame.draw.rect(display, color, (x, y, width, height))
    # Вывод текста
    printText(message, x + width // 2 - hitBoxX, y + (height // 2 - hitBoxY), colorTitle, font_size)
    # Проверка наличия картинки
    if image is not None:
        # Выведение картинки
        display.blit(image, (x, y))
    # Проверка положения мыши
    if x < mouse[0] < x + width:
        if y < mouse[1] < y + height:
            # Проверка цвета при наведении
            if activeColor != 0:
                # Вывод кнопки
                pygame.draw.rect(display, activeColor, (x, y, width, height))
            # Проверка цвета
            elif color != 0:
                # Вывод кнопки
                pygame.draw.rect(display, color, (x, y, width, height))
            # Проверка цвета текст при наведениии
            if activeColorTitle != 0:
                # Вывод текста
                printText(message, x + width // 2 - hitBoxX, y + (height // 2 - hitBoxY), (80, 80, 80),
                          font_size)
            # Если кнопка взаимодействует с игроком
            if withPlayer:
                # Если наведено на эту область, то менять картинку игрока на соответствующую будущему перемещению
                if x == player.get_coor()[0] + 114:
                    if y == player.get_coor()[1] - 45:
                        player.change_image(pygame.image.load("files/images/player/boy/boy_right.png"))
                    elif y == player.get_coor()[1] + 45:
                        player.change_image(pygame.image.load("files/images/player/boy/boy_right.png"))
                elif x == player.get_coor()[0] - 114:
                    if y == player.get_coor()[1] - 45:
                        player.change_image(pygame.image.load("files/images/player/boy/boy_left.png"))
                    elif y == player.get_coor()[1] + 45:
                        player.change_image(pygame.image.load("files/images/player/boy/boy_left.png"))
                elif x == player.get_coor()[0]:
                    if y == player.get_coor()[1] + 90:
                        player.change_image(pygame.image.load("files/images/player/boy/boy_forward.png"))
                    elif y == player.get_coor()[1] - 90:
                        player.change_image(pygame.image.load("files/images/player/boy/boy_behind.png"))

            # Проверка клика
            if click[0] == 1:
                # Задержка
                pygame.time.delay(120)
                # Возвращение факта нажатия клика
                return True

# Вывод текста
def printText(message, x, y, font_color=(0, 0, 0), font_size=25, background_color=None,
              font='files/fonts/RUSNeverwinter.ttf', antialiasing=True):    # Текст, положение, цвет, размер, фон,
                                                                            # Шрифт, сглаживаие
    # Инициализация шрифта
    font_type = pygame.font.Font(font, font_size)
    # Генерация текста
    text = font_type.render(message, antialiasing, font_color, background_color)
    # Вывод текста
    display.blit(text, (int(x), int(y)))
