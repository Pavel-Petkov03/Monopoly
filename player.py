import os.path
from vars import BASE_DIR
import pygame.image

from client import Client


class Player:
    def __init__(self, name, piece_image_location):
        self.name = name
        self.board_index = 0
        self.money = 1000
        self.piece_image_location = piece_image_location
        self.piece_image = pygame.image.load(os.path.join(BASE_DIR, "images", "pieces", self.piece_image_location))
        self.client = Client()
        self.in_prison = False
        self.prison_attempt_throw = 0
        self.prison_cards = 0





