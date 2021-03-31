# Импорт
import pygame
from random import randint as rand
from engine import *
from vars import *
from Player import *
from Crystal import *
from Floor_Part import *

# Инициализация pygame
pygame.init()

# Красивый логотип
def screenSaver():
    global screen, logo_counter, logo_counter_set
    # Белый фон
    display.fill((255, 255, 255))

    # Прозрачность
    logo.set_alpha(logo_counter)
    # Вывод лого
    display.blit(logo, (0, 0))
    # Изменение прозрачности
    if logo_counter_set == 1 and logo_counter < 255:
        logo_counter += 3
        logo_counter_set = 0
        return 0
    if logo_counter == 255 and logo_counter_set == 1:
        # Выход
        screen = "Загрузка"
        return 0
    logo_counter_set += 1
    return 0

# Загрузка перед началом игры
def load():
    global screen, loaded1, loaded2, background, loadFill, loadHalfFill
    # Фон
    display.blit(bg, (0, 0))

    # Первая половина загрузок
    if not loaded1 and not loaded2:
        # Экран загрузки
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))

        # Наполовину заполненная полоса загрузки
        loadHalfFill = pygame.image.load("files/images/loadHalfFill.png")
        loadHalfFill = pygame.transform.scale(loadHalfFill,
                                              (loadHalfFill.get_width() * 2, loadHalfFill.get_height() * 2))
        loaded1 = True
        return 0

    # Вторая половина загрузок
    elif loaded1 and not loaded2:
        # Экран загрузки
        display.blit(loadHalfFill, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))

        # Фон
        background = pygame.image.load("files/images/background.png")
        background = pygame.transform.scale(background, (background.get_width() * 2, background.get_height() * 2))
        # Заполненная строка загрузки
        loadFill = pygame.image.load("files/images/loadFill.png")
        loadFill = pygame.transform.scale(loadFill, (loadFill.get_width() * 2, loadFill.get_height() * 2))
        loaded2 = True
        return 0
    else:
        # Экран загрузки
        display.blit(loadFill, ((WIDTH - (WIDTH - 40)), HEIGHT - 200))
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        loaded1 = False
        loaded2 = False
        # Выход
        screen = "Меню"
        return 0

# Загрузка перед игрой
def loadingBeforePlay():
    global screen, player, gray, floorPart, loaded1, loaded2, player_image, floor
    global crystals, crystalPlace, needCrystal, crystalImage

    # Фон
    display.blit(background, (0, 0))

    # Первая половина загрузок
    if not loaded1 and not loaded2:
        # Экран загрузки
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))

        # Картинка игрока
        player_image = pygame.image.load("files/images/player.png")
        # Серый фон
        gray = pygame.image.load("files/images/Gray.png")
        gray = pygame.transform.scale(gray, (gray.get_width() * 2, gray.get_height() * 2))
        # Часть пола
        floorPart = pygame.image.load("files/images/floorPart.png")
        floorPart = pygame.transform.scale(floorPart, (floorPart.get_width() * 2, floorPart.get_height() * 2))
        # Часть пола
        floor1 = []
        floor2 = []
        # Запись всего поля
        for i in range(0, 6):
            for j in range(1, 7):
                floor1.append(Floor_Part(floorPart, 228 * i - 10, 90 * j))
        for i in range(0, 5):
            for j in range(0, 7):
                floor2.append(Floor_Part(floorPart, 114 + 228 * i - 10, 45 + 90 * j))
        floor = [floor1, floor2]
        loaded1 = True
        return 0

    # Вторая половина загрузок
    elif loaded1 and not loaded2:
        # Экран загрузки
        display.blit(loadHalfFill, ((WIDTH - (WIDTH - 40)), HEIGHT - 200))
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))

        # Картинка кристалла
        crystalImage = pygame.image.load("files/images/crystal.png")
        # Элемент класса Player (см. Player.py)
        player = Player(player_image, 40, 64)
        # Генерация расположения кристаллов
        crystalPlace = [rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017), rand(1140, 1245),
                        rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017), rand(1140, 1245)]
        # Генерация надобности кристаллов
        needCrystal = [rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5),
                       rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5)]
        # Добавление сведений о кристаллах в общий список
        crystals = []
        for i in range(0, 11):
            if i < 6:
                crystals.append(Crystal(crystalImage, crystalPlace[i], 0))
            else:
                crystals.append(Crystal(crystalImage, crystalPlace[i], 645))
        loaded2 = True
        return 0
    else:
        # Экран загрузки
        display.blit(loadFill, ((WIDTH - (WIDTH - 40)), HEIGHT - 200))
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        # scheme = []
        loaded1 = False
        loaded2 = False
        # Выход
        screen = "Играть2"
        return 0

# Меню
def menu():
    global screen, escapePressed
    # Фон
    display.blit(background, (0, 0))

    # Кнопка начала игры
    if button(WIDTH // 2 - 100, HEIGHT // 2 - 100, 100, 100, "Play"):
        screen = "Играть"

    # Выход нажатием клавиши escape
    if keys[pygame.K_ESCAPE]:
        # Проверка на долговременное нажатие (если убрать - баги)
        if not escapePressed:
            escapePressed = True
            pygame.time.delay(120)
    else:
        # Продолжение проверки на долговременное нажатие
        if escapePressed:
            screen = "Хотите выйти?"
            escapePressed = False

# АВЫТОЧНОХОТИТЕВЫЙТИ??????
def you_exit():
    global screen
    # Фон
    display.blit(background, (0, 0))

    printText("Do you want to exit?", WIDTH // 2 - 145, HEIGHT // 2 - 112)

    if button(WIDTH // 2 - 175, HEIGHT // 2 - 12, 75, 25, "Yes"):
        return True
    if button(WIDTH // 2 + 100, HEIGHT // 2 - 12, 75, 25, "No"):
        screen = "Меню"
        return False

# Сама игра
def play():
    global screen, player, escapePressed
    # Фон
    display.blit(gray, (0, 0))

    # Вывод кристаллов и пола
    printFloor()
    printCrystal()

    # Вывод игрока
    player.set()

    # Возможность выхода нажатием escape
    if keys[pygame.K_ESCAPE]:
        # Проверка на долговременное нажатие (если убрать - баги)
        if not escapePressed:
            escapePressed = True
            pygame.time.delay(120)
    else:
        # Продолжение проверки на долговременное нажатие
        if escapePressed:
            screen = "Меню"
            escapePressed = False

# Вывод кристаллов
def printCrystal():
    # Цикл обеспечивает нам проверку надобности кристаллов в конкретной позиции, всего позиций - 12
    for i in range(0, 11):
        if needCrystal[i] == 1:
            # Вывод кристаллов (см. Crystal.py)
            crystals[i].set()

# Вывод пола
def printFloor():
    floor1 = floor[0]
    floor2 = floor[1]
    for partFloor in floor1:
        partFloor.set()
    for partFloor in floor2:
        partFloor.set()

def changeMove():
    global line
    a = player.get()
    positionPlayer = [a[1], a[2]]
    floor1 = floor[0]
    floor2 = floor[1]
    positionFloorFirstType = []
    positionFloorSecondType = []
    for partFloorFirstType in floor1:
        positionFloorFirstType.append([partFloorFirstType.get()[1], partFloorFirstType.get()[2]])
    for partFloorSecondType in floor2:
        positionFloorSecondType.append([partFloorSecondType.get()[1], partFloorSecondType.get()[2]])

    for part in positionFloorFirstType:
        if positionPlayer == part:
            line = 1
    for part in positionFloorSecondType:
        if positionPlayer == part:
            line = 2

    print(positionFloorFirstType)
    print(positionFloorSecondType)

    around = []
    if line == 1:
        if player.x - 114 >= 104 and player.y - 45 >= 45:
            around.append([player.x - 114, player.y - 45])
        else:
            around.append([None, None])
        if player.x + 114 <= 1016 and player.y - 45 >= 45:
            around.append([player.x + 114, player.y - 45])
        else:
            around.append([None, None])
        if player.x + 228 <= 1130:
            around.append([player.x + 114, player.y])
        else:
            around.append([None, None])
        if player.x + 114 <= 1016 and player.y + 45 <= 585:
            around.append([player.x + 114, player.y + 45])
        else:
            around.append([None, None])
        if player.x - 114 >= 104 and player.y + 45 <= 585:
            around.append([player.x - 114, player.y + 45])
        else:
            around.append([None, None])
        if player.x - 228 >= -10:
            around.append([player.x - 288, player.y])
        else:
            around.append([None, None])
    elif line == 2:
        if player.x - 114 >= -10 and player.y - 45 >= 90:
            around.append([player.x - 114, player.y - 45])
        else:
            around.append([None, None])
        if player.x + 114 <= 1130 and player.y - 45 >= 90:
            around.append([player.x + 114, player.y - 45])
        else:
            around.append([None, None])
        if player.x + 228 <= 1016:
            around.append([player.x + 90])
        else:
            around.append([None, None])
        if player.x + 114 <= 1130 and player.y + 45 <= 540:
            around.append([player.x + 114, player.y + 45])
        else:
            around.append([None, None])
        if player.x - 114 >= -0 and player.y + 45 <= 540:
            around.append([player.x - 114, player.y + 45])
        else:
            around.append([None, None])
        if player.x - 228 >= 104:
            around.append([player.x - 288, player.y])
        else:
            around.append([None, None])

# Цикл игры
def game():
    global keys
    # Конец игры
    game_end = False

    # Главный цикл
    while not game_end:
        # FPS
        clock.tick(60)

        # Ввод с клавиатуры
        keys = pygame.key.get_pressed()

        # Выход с программы
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True

        # Экраны
        if screen == 0:
            screenSaver()
        elif screen == "Загрузка":
            load()
        elif screen == "Меню":
            menu()
        elif screen == "Хотите выйти?":
            game_end = you_exit()
        elif screen == "Играть":
            loadingBeforePlay()
        elif screen == "Играть2":
            play()
            changeMove()

        # Обновение экрана
        pygame.display.update()


# Вызов главного цикла
game()
