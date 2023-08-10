import pygame
import ctypes
import os

from neighborhood import Neighborhood

user32 = ctypes.windll.user32
size = min(user32.GetSystemMetrics(78), user32.GetSystemMetrics(79))
screen_rect_size = int(size - size / 8)
screen = pygame.display.set_mode((screen_rect_size, screen_rect_size))
GAME_NAME = "Monopoly"
pygame.display.set_caption(GAME_NAME)
BASE_DIR = os.path.dirname(__file__)

neighborhood_count_list = [2, 3, 3, 3, 3, 3, 3, 2]

neighborhoods = {str(i + 1): Neighborhood(i + 1, neighborhood_count_list[i]) for i in range(len(neighborhood_count_list))}
border_data = [
    {
        "rect_type": "corner",
        "inside_image_path": "start.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Ботевградско Шосе",
        "price": "120",
        "color": "brown",
        "neighborhood": "1"
    },
    {
        "rect_type": 'side_image',
        "caption": "Обществен Трезор",
        "inside_image_path": "treasure.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Цариградско Шосе",
        "price": "120",
        "color": "brown",
        "neighborhood": "1"
    },
    {
        "rect_type": 'side_image',
        "caption": "Данък",
        "price": "400",
        "inside_image_path": "treasure.png"
    },
    {
        "rect_type": 'side_image',
        "caption": "Гара София",
        "price": "200",
        "inside_image_path": "station.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Опълченска",
        "price": "120",
        "color": "blue",
        "neighborhood": "2"
    },
    {
        "rect_type": 'side_image',
        "caption": "Шанс",
        "inside_image_path": "chance.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Сливница",
        "price": "120",
        "color": "blue",
        "neighborhood": "2"
    },
    {
        "rect_type": 'generic',
        "caption": "Лъвов мост",
        "price": "120",
        "color": "blue",
        "neighborhood": "2"
    },
    {
        "rect_type": "corner",
        "inside_image_path": "in_jail.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Македония",
        "price": "120",
        "color": "pink",
        "neighborhood": "3"
    },
    {
        "rect_type": 'side_image',
        "caption": "НЕК",
        "price": "120",
        "inside_image_path": "lamp.png"
    },
    {
        "rect_type": 'generic',
        "caption": "улица Пиротска",
        "price": "120",
        "color": "pink",
        "neighborhood": "3"
    }, {
        "rect_type": 'generic',
        "caption": "булевард Христо Ботев",
        "price": "120",
        "color": "pink",
        "neighborhood": "3"
    }, {
        "rect_type": 'side_image',
        "caption": "Гара Пловдив",
        "price": "200",
        "inside_image_path": "station.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Евлоги Георгиев",
        "price": "120",
        "color": "orange",
        "neighborhood": "4"
    },
    {
        "rect_type": 'side_image',
        "caption": "Обществен трезор",
        "price": "200",
        "inside_image_path": "treasure.png"
    },
    {
        "rect_type": 'generic',
        "caption": "Орлов Мост",
        "price": "120",
        "color": "orange",
        "neighborhood": "4"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард България",
        "price": "120",
        "color": "orange",
        "neighborhood": "4"
    },
    {
        "rect_type": "corner",
        "inside_image_path": "parking.png"
    },
    {
        "rect_type": 'generic',
        "caption": "Сан Стефано",
        "price": "120",
        "color": "red",
        "neighborhood": "5"
    },
    {
        "rect_type": 'side_image',
        "caption": "Шанс",
        "inside_image_path": "chance.png"
    }, {
        "rect_type": 'generic',
        "caption": "ул Шипка",
        "price": "120",
        "color": "red",
        "neighborhood": "5"
    },
    {
        "rect_type": 'generic',
        "caption": "ул Оборище",
        "price": "120",
        "color": "red",
        "neighborhood": "5"
    },
    {
        "rect_type": 'side_image',
        "caption": "Гара Варна",
        "price": "200",
        "inside_image_path": "station.png"
    },
    {
        "rect_type": 'generic',
        "caption": "Патриарх Евтими",
        "price": "120",
        "color": "yellow",
        "neighborhood": "6"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Дондуков",
        "price": "120",
        "color": "yellow",
        "neighborhood": "6"
    },

    {
        "rect_type": 'side_image',
        "caption": "ВИК",
        "inside_image_path": "sink.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Васил Левски",
        "price": "120",
        "color": "yellow",
        "neighborhood": "6"
    },
    {
        "rect_type": 'corner',
        "inside_image_path": "police.png",
    },
    {
        "rect_type": 'generic',
        "caption": "ул Раковски",
        "price": "120",
        "color": "green",
        "neighborhood": "7"
    },
    {
        "rect_type": 'generic',
        "caption": "ул Граф Игнатиев",
        "price": "120",
        "color": "green",
        "neighborhood": "7"
    },
    {
        "rect_type": 'side_image',
        "caption": "Обществен Трезор",
        "inside_image_path": "treasure.png"
    },
    {
        "rect_type": 'generic',
        "caption": "ул Цар Освободител",
        "price": "120",
        "color": "green",
        "neighborhood": "7"
    },
    {
        "rect_type": 'side_image',
        "caption": "Гара Бургас",
        "price": "200",
        "inside_image_path": "station.png"
    },
    {
        "rect_type": 'side_image',
        "caption": "Шанс",
        "inside_image_path": "chance.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Витошка",
        "price": "120",
        "color": "purple",
        "neighborhood": "8"
    },
    {
        "rect_type": 'side_image',
        "caption": "Данък",
        "inside_image_path": "tax.png"
    },
    {
        "rect_type": 'generic',
        "caption": "Бояна",
        "price": "120",
        "color": "purple",
        "neighborhood": "8"
    },

]
