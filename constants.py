from enum import Enum

import pygame
pygame.font.init()

win = pygame.display.set_mode((1280, 720))

verdana16 = pygame.font.SysFont('Verdana', 16)
verdana24 = pygame.font.SysFont('Verdana', 24)
verdana30 = pygame.font.SysFont('Verdana', 30)

color_dark_blue = (0, 0, 255)
color_light_blue = (105, 152, 255)
color_white = (250, 250, 250)
color_red = (229, 42, 60)

circle_position = [
    (850, 88),  # Sorting algorithm buttons
    (850, 118),
    (850, 148),
    (1050, 88),
    (1050, 118),
    (1050, 148),

    (90, 88),  # Speed buttons
    (90, 118),
    (90, 148),

    (290, 88),
    (290, 119),
    (290, 148)  # Size buttons

]
button_position = [
    (520, 10, 240, 70),
    (520, 90, 240, 70)
]


class arraySize(Enum):  # default, 80 = large, 40 = Medium, 20 = small
    LARGE = 80
    Medium = 40
    SMALL = 20


class sortingSpeed(Enum):  # 0 = fast, 1 = Medium, 2 = slow
    FAST = 0
    MEDIUM = 1
    SLOW = 2

class algorithms(Enum):  # 0 = bubble sort, 1 = Selection Sort, 2 = Insertion Sort,
     BUBBLE_SORT = 0     # 3 = Bucket Sort, 4 = Merge Sort, 5 = Quick Sort
     SELECTION_SORT = 1
     INSERTION_SORT = 2
     BUCKET_SORT = 3
     MERGE_SORT = 4
     QUICK_SORT = 5

