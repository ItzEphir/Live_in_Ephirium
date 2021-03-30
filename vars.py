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
logo = pygame.image.load("files/images/logo.png")
loadScreen = pygame.image.load("files/images/loadScreen.png")
loadScreen = pygame.transform.scale(loadScreen, (loadScreen.get_width() * 2, loadScreen.get_height() * 2))
loadHalfFill = None
loadFill = None
bg = pygame.image.load("files/images/bg.png")
bg = pygame.transform.scale(bg, (bg.get_width() * 2, bg.get_height() * 2))

logo_counter = 0
logo_counter_set = 0

# Переменные, используемые в коде программы
gray = None     # Серый цвет
floorPart = None    # Часть пола
background = None   # Фон
crystalImage = None     # Картинка кристалла
crystalPlace = None     # Места кристаллов
needCrystal = None      # Нужен ли кристалл (я философ)
player_image = None     # Картинка игрока
player = None           # Игрок
keys = None             # Нажатие клавиш
