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

neighborhoods = {str(i + 1): Neighborhood(i + 1, neighborhood_count_list[i]) for i in
                 range(len(neighborhood_count_list))}
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
        "neighborhood": "1",
        "price_dict": {
            "0": "2",
            "1": "10",
            "2": "30",
            "3": "90",
            "4": "160",
            "5": "250",
        }
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
        "neighborhood": "1",
        "price_dict": {
            "0": "4",
            "1": "20",
            "2": "60",
            "3": "180",
            "4": "320",
            "5": "450",
        }

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
        "neighborhood": "2",
        "price_dict": {
            "0": "6",
            "1": "30",
            "2": "90",
            "3": "270",
            "4": "400",
            "5": "550",
        }
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
        "neighborhood": "2",
        "price_dict": {
            "0": "6",
            "1": "30",
            "2": "90",
            "3": "270",
            "4": "400",
            "5": "550",
        }
    },
    {
        "rect_type": 'generic',
        "caption": "Лъвов мост",
        "price": "120",
        "color": "blue",
        "neighborhood": "2",
        "price_dict": {
            "0": "8",
            "1": "40",
            "2": "100",
            "3": "300",
            "4": "450",
            "5": "600",
        }
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
        "neighborhood": "3",
        "price_dict": {
            "0": "10",
            "1": "50",
            "2": "150",
            "3": "450",
            "4": "625",
            "5": "750",
        }
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
        "neighborhood": "3",
        "price_dict": {
            "0": "10",
            "1": "50",
            "2": "150",
            "3": "450",
            "4": "625",
            "5": "750",
        }
    }, {
        "rect_type": 'generic',
        "caption": "булевард Христо Ботев",
        "price": "120",
        "color": "pink",
        "neighborhood": "3",
        "price_dict": {
            "0": "12",
            "1": "60",
            "2": "180",
            "3": "500",
            "4": "700",
            "5": "900",
        }
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
        "neighborhood": "4",
        "price_dict": {
            "0": "14",
            "1": "70",
            "2": "200",
            "3": "550",
            "4": "750",
            "5": "950",
        }
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
        "neighborhood": "4",
        "price_dict": {
            "0": "14",
            "1": "70",
            "2": "200",
            "3": "550",
            "4": "750",
            "5": "950",
        }
    },
    {
        "rect_type": 'generic',
        "caption": "булевард България",
        "price": "120",
        "color": "orange",
        "neighborhood": "4",
        "price_dict": {
            "0": "16",
            "1": "80",
            "2": "220",
            "3": "600",
            "4": "800",
            "5": "1000",
        }
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
        "neighborhood": "5",
        "price_dict": {
            "0": "18",
            "1": "90",
            "2": "250",
            "3": "700",
            "4": "875",
            "5": "1050",
        }
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
        "neighborhood": "5",
        "price_dict": {
            "0": "18",
            "1": "90",
            "2": "250",
            "3": "700",
            "4": "875",
            "5": "1050",
        }
    },
    {
        "rect_type": 'generic',
        "caption": "ул Оборище",
        "price": "120",
        "color": "red",
        "neighborhood": "5",
        "price_dict": {
            "0": "20",
            "1": "100",
            "2": "300",
            "3": "750",
            "4": "925",
            "5": "1100",
        }
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
        "neighborhood": "6",
        "price_dict": {
            "0": "22",
            "1": "110",
            "2": "330",
            "3": "800",
            "4": "975",
            "5": "1150",
        }
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Дондуков",
        "price": "120",
        "color": "yellow",
        "neighborhood": "6",
        "price_dict": {
            "0": "22",
            "1": "110",
            "2": "330",
            "3": "800",
            "4": "975",
            "5": "1150",
        }
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
        "neighborhood": "6",
        "price_dict": {
            "0": "24",
            "1": "120",
            "2": "360",
            "3": "850",
            "4": "1025",
            "5": "1200",
        }
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
        "neighborhood": "7",
        "price_dict": {
            "0": "26",
            "1": "130",
            "2": "390",
            "3": "900",
            "4": "1100",
            "5": "1275",
        }
    },
    {
        "rect_type": 'generic',
        "caption": "улица Граф Игнатиев",
        "price": "120",
        "color": "green",
        "neighborhood": "7",
        "price_dict": {
            "0": "26",
            "1": "130",
            "2": "390",
            "3": "900",
            "4": "1100",
            "5": "1275",
        }
    },
    {
        "rect_type": 'side_image',
        "caption": "Обществен Трезор",
        "inside_image_path": "treasure.png"
    },
    {
        "rect_type": 'generic',
        "caption": "улица Цар Освободител",
        "price": "120",
        "color": "green",
        "neighborhood": "7",
        "price_dict": {
            "0": "28",
            "1": "150",
            "2": "450",
            "3": "1000",
            "4": "1200",
            "5": "1400",
        }
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
        "neighborhood": "8",
        "price_dict": {
            "0": "35",
            "1": "175",
            "2": "500",
            "3": "1100",
            "4": "1300",
            "5": "1500",
        }
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
        "neighborhood": "8",
        "price_dict": {
            "0": "50",
            "1": "200",
            "2": "600",
            "3": "1400",
            "4": "1700",
            "5": "2000",
        }
    },
]
