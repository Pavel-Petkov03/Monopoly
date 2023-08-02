import pygame

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
GAME_NAME = "Monopoly"
pygame.display.set_caption(GAME_NAME)

border_data = [
    {
        "rect_type" : "generic",
        "color" : "red",
        "caption" : 'Something',
        "price" : "123"
    },
    {
        "rect_type" : 'corner',
        "inside_image_path" : "something"
    },
    {
        "rect_type" : "side_image",
        "caption" : "Sometjfeds",
        "inside_image_path" : "something",
        "price" : "2qfew"
    }
]