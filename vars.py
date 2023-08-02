import pygame
import ctypes

user32 = ctypes.windll.user32
size = min(user32.GetSystemMetrics(78), user32.GetSystemMetrics(79))
screen_rect_size = size - size / 8
screen = pygame.display.set_mode((screen_rect_size, screen_rect_size))
GAME_NAME = "Monopoly"
pygame.display.set_caption(GAME_NAME)

border_data = [
    {
        "rect_type": "corner",
        "inside_image_path": "images/start.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Ботевградско Шосе",
        "price": "120",
        "color": "brown",
    },
    {
        "rect_type": 'side_image',
        "caption": "Обществен Трезор",
        "inside_image_path": "images/treasure.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Цариградско Шосе",
        "price": "120",
        "color": "brown",
    },
    {
        "rect_type": 'side_image',
        "caption": "Данък",
        "price": "400",
        "inside_image_path": "images/treasure.png"
    },
    {
        "rect_type": 'side_image',
        "caption": "Гара София",
        "price": "200",
        "inside_image_path": "images/station.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Опълченска",
        "price": "120",
        "color": "blue",
    },
    {
        "rect_type": 'side_image',
        "caption": "Шанс",
        "inside_image_path": "images/chance.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Сливница",
        "price": "120",
        "color": "blue",
    },
    {
        "rect_type": 'generic',
        "caption": "Лъвов мост",
        "price": "120",
        "color": "blue",
    },
    {
        "rect_type": "corner",
        "inside_image_path": "images/parking.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Македония",
        "price": "120",
        "color": "pink",
    },
    {
        "rect_type": 'side_image',
        "caption": "НЕК",
        "price": "120",
        "inside_image_path": "images/parking.png"
    },
    {
        "rect_type": 'generic',
        "caption": "улица Пиротска",
        "price": "120",
        "color": "pink",
    }, {
        "rect_type": 'generic',
        "caption": "булевард Христо Ботев",
        "price": "120",
        "color": "brown",
    }, {
        "rect_type": 'side_image',
        "caption": "Гара Пловдив",
        "price": "200",
        "inside_image_path": "images/parking.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Евлоги Георгиев",
        "price": "120",
        "color": "orange",
    },
    {
        "rect_type": 'side_image',
        "caption": "Обществен трезор",
        "price": "200",
        "inside_image_path": "images/parking.png"
    },
    {
        "rect_type": 'generic',
        "caption": "Орлов Мост",
        "price": "120",
        "color": "orange",
    },
    {
        "rect_type": 'generic',
        "caption": "булевард България",
        "price": "120",
        "color": "orange",
    },
    {
        "rect_type": "corner",
        "inside_image_path": "images/parking.png"
    },
    {
        "rect_type": 'generic',
        "caption": "Сан Стефано",
        "price": "120",
        "color": "red",
    },
    {
        "rect_type": 'side_image',
        "caption": "Шанс",
        "inside_image_path": "images/chance.png"
    }, {
        "rect_type": 'generic',
        "caption": "ул Шипка",
        "price": "120",
        "color": "red",
    },



]
