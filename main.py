# Импорт
import pygame
from random import randint as rand
from engine import *
from vars import *
from Player import *
from Crystal import *
from Floor_Part import *
from Enemy import *
from NPC import *

# Инициализация pygame
pygame.init()


# Красивый логотип
def screenSaver():
    global screen, logo_counter, logo_counter_set
    # Белый фон
    display.fill((255, 255, 255))

    # Прозрачность
    logo.set_alpha(int(logo_counter))
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
        loadHalfFill = pygame.image.load("files/images/loadHalfFill.png").convert_alpha()
        loadHalfFill = pygame.transform.scale(loadHalfFill,
                                              (loadHalfFill.get_width() * 2,
                                               loadHalfFill.get_height() * 2)).convert_alpha()
        loaded1 = True
        return 0

    # Вторая половина загрузок
    elif loaded1 and not loaded2:
        # Экран загрузки
        display.blit(loadHalfFill, (WIDTH - (WIDTH - 40), HEIGHT - 200))
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))

        # Фон
        background = pygame.image.load("files/images/background.png").convert_alpha()
        background = pygame.transform.scale(background, (background.get_width() * 2,
                                                         background.get_height() * 2)).convert_alpha()

        # Заполненная строка загрузки
        loadFill = pygame.image.load("files/images/loadFill.png").convert_alpha()
        loadFill = pygame.transform.scale(loadFill, (loadFill.get_width() * 2,
                                                     loadFill.get_height() * 2)).convert_alpha()
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
    global crystals, crystalPlace, needCrystal, crystalImage, enemy

    # Фон
    display.blit(background, (0, 0))

    # Первая половина загрузок
    if not loaded1 and not loaded2:
        # Экран загрузки
        display.blit(loadScreen, (WIDTH - (WIDTH - 40), HEIGHT - 200))

        # Картинка игрока
        player_image = pygame.image.load("files/images/player_girl.png").convert_alpha()
        # Серый фон
        gray = pygame.image.load("files/images/Gray.png").convert_alpha()
        gray = pygame.transform.scale(gray, (gray.get_width() * 2,
                                             gray.get_height() * 2)).convert_alpha()
        # Часть пола
        floorPart = pygame.image.load("files/images/floorPart.png").convert_alpha()
        floorPart = pygame.transform.scale(floorPart, (floorPart.get_width() * 2,
                                                       floorPart.get_height() * 2)).convert_alpha()
        # Часть пола
        floor1 = []
        floor2 = []
        enemy = Enemy(player_image, 264, 90)
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
        crystalImage = pygame.image.load("files/images/crystal.png").convert_alpha()
        # Элемент класса Player (см. Player.py)
        player = Player(player_image, 36, 90, 1)
        # Генерация расположения кристаллов
        crystalPlace = [rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017), rand(1140, 1245),
                        rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017), rand(1140, 1245)]
        # Генерация надобности кристаллов
        needCrystal = [rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5),
                       rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5)]
        # Если кристаллов вообще нет
        if (needCrystal[0] != 1 and needCrystal[1] != 1 and needCrystal[2] != 1 and needCrystal[3] != 1 and
                needCrystal[4] != 1 and needCrystal[5] != 1 and needCrystal[6] != 1 and needCrystal[7] != 1 and
                needCrystal[8] != 1 and needCrystal[9] != 1 and needCrystal[10] != 1 and needCrystal[11] != 1):
            needCrystal[rand(0, 11)] = 1
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

    # Вывод врага
    enemy.set()

    # Координаты игрока
    coor_player = player.get_coor()

    # Координаты врага
    coor_enemy = enemy.get_coor()

    # Возможность перемещения
    if button(coor_player[0] + 114, coor_player[1] - 45, 72, 90, "", 0, 0, (0, 0, 0), 0, 50, 10, 25, None,
              True, player) and coor_player[0] + 114 <= 1244 and coor_player[1] - 45 >= 45:
        if not(coor_player[0] + 114 == coor_enemy[0] and coor_player[1] - 45 == coor_enemy[1]):
            player.move("right_up")
        else:
            player.attack(enemy)
    elif button(coor_player[0] - 114, coor_player[1] - 45, 72, 90, "", 0, 0, (0, 0, 0), 0, 50, 10, 25, None,
                True, player) and coor_player[0] - 114 >= -10 and coor_player[1] - 45 >= 45:
        if not(coor_player[0] - 114 == coor_enemy[0] and coor_player[1] - 45 == coor_enemy[1]):
            player.move("left_up")
        else:
            player.attack(enemy)
    elif button(coor_player[0] + 114, coor_player[1] + 45, 72, 90, "", 0, 0, (0, 0, 0), 0, 50, 10, 25, None,
                True, player) and coor_player[0] + 114 <= 1244 and coor_player[1] + 45 <= 585:
        if not(coor_player[0] + 114 == coor_enemy[0] and coor_player[1] + 45 == coor_enemy[1]):
            player.move("right_down")
        else:
            player.attack(enemy)
    elif button(coor_player[0] - 114, coor_player[1] + 45, 72, 90, "", 0, 0, (0, 0, 0), 0, 50, 10, 25, None,
                True, player) and coor_player[0] - 114 >= -10 and coor_player[1] + 45 <= 585:
        if not(coor_player[0] - 114 == coor_enemy[0] and coor_player[1] + 45 == coor_enemy[1]):
            player.move("left_down")
        else:
            player.attack(enemy)
    elif button(coor_player[0], coor_player[1] + 90, 72, 90, "", 0, 0, (0, 0, 0), 0, 50, 10, 25, None,
                True, player) and coor_player[1] + 90 <= 585:
        if not(coor_player[0] == coor_enemy[0] and coor_player[1] + 90 == coor_enemy[1]):
            player.move("down")
        else:
            player.attack(enemy)
    elif button(coor_player[0], coor_player[1] - 90, 72, 90, "", 0, 0, (0, 0, 0), 0, 50, 10, 25, None,
                True, player) and coor_player[1] - 90 >= 45:
        if not(coor_player[0] == coor_enemy[0] and coor_player[1] - 90 == coor_enemy[1]):
            player.move("up")
        else:
            player.attack(enemy)

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
    global needCrystal, crystalPlace, crystals
    # Цикл обеспечивает нам проверку надобности кристаллов в конкретной позиции, всего позиций - 12
    for i in range(0, 11):
        if needCrystal[i] == 1:
            # Вывод кристаллов (см. Crystal.py)
            crystals[i].set()
            # Перегенерация кристаллов
            if button(crystals[i].get_position()[0], crystals[i].get_position()[1], 75, 75, ""):
                # Генерация расположения кристаллов
                crystalPlace = [rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017),
                                rand(1140, 1245),
                                rand(0, 105), rand(228, 333), rand(456, 561), rand(684, 789), rand(912, 1017),
                                rand(1140, 1245)]
                # Генерация надобности кристаллов
                needCrystal = [rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5),
                               rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5), rand(0, 5)]
                # Если кристаллов нет
                if (needCrystal[0] != 1 and needCrystal[1] != 1 and needCrystal[2] != 1 and needCrystal[3] != 1 and
                        needCrystal[4] != 1 and needCrystal[5] != 1 and needCrystal[6] != 1 and needCrystal[7] != 1 and
                        needCrystal[8] != 1 and needCrystal[9] != 1 and needCrystal[10] != 1 and needCrystal[11] != 1):
                    needCrystal[rand(0, 11)] = 1
                # Добавление сведений о кристаллах в общий список
                crystals = []
                for x in range(0, 11):
                    if x < 6:
                        crystals.append(Crystal(crystalImage, crystalPlace[x], 0))
                    else:
                        crystals.append(Crystal(crystalImage, crystalPlace[x], 645))

# Вывод пола
def printFloor():
    floor1 = floor[0]
    floor2 = floor[1]
    for partFloor in floor1:
        partFloor.set()
    for partFloor in floor2:
        partFloor.set()

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

        # Обновение экрана
        pygame.display.update()


# Вызов главного цикла
game()
