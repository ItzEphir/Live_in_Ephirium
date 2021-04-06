# Импорт
import pygame

# Инициализация pygame
pygame.init()

# Экран
screen = 0

# Статус загрузки
loaded1 = False
loaded2 = False

# Нажатие escape
escapePressed = False

# Базовые загрузки: экран загрузки, фон
logo = pygame.image.load("files/images/logo.png").convert_alpha()
loadScreen = pygame.image.load("files/images/loadScreen.png").convert_alpha()
loadScreen = pygame.transform.scale(loadScreen, (loadScreen.get_width() * 2,
                                                 loadScreen.get_height() * 2)).convert_alpha()
loadHalfFill = None
loadFill = None
bg = pygame.image.load("files/images/bg.png").convert_alpha()
bg = pygame.transform.scale(bg, (bg.get_width() * 2, bg.get_height() * 2)).convert_alpha()

logo_counter = 0
logo_counter_set = 0

# Переменные, используемые в коде программы
gray = None     # Серый цвет
floorPart = None    # Часть пола
floor = None        # Пол
background = None   # Фон
crystalImage = None     # Картинка кристалла
crystalPlace = None     # Места кристаллов
needCrystal = None      # Нужен ли кристалл (я философ)
player_image = None     # Картинка игрока
player = None           # Игрок
enemy = None            # Враг
keys = None             # Нажатие клавиш
line = 0                # "Линия" пола
