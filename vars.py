import pygame

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
GAME_NAME = "Monopoly"
pygame.display.set_caption(GAME_NAME)

border_data = [
    {
        "rect_type": "corner",
        "inside_image_path": "images/parking.png"
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
        "inside_image_path": "images/treasure.png"
    },
    {
        "rect_type": 'generic',
        "caption": "булевард Опълченска",
        "price": "120",
        "color": "blue",
    },
    {
        "rect_type": 'side_image',
        "caption": "Обществен Трезор",
        "inside_image_path": "images/treasure.png"
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
]
