import ctypes
from collections import deque

import pygame

from player import Player
from renderers.base_renderer import Renderer
from sprites.board import Board
from sprites.dice import Dices
from vars import screen_rect_size, w, h,size, board_screen_x, board_screen_y, screen


class BoardRenderer(Renderer):
    def __init__(self, players):
        super().__init__()
        self.board = Board(self)
        self.screen = pygame.Surface((screen_rect_size, screen_rect_size))
        self.image = pygame.image.load("images/board/inner/background.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_rect_size, screen_rect_size)).convert_alpha()
        self.outer_image = pygame.image.load("images/board/outer/background.png").convert_alpha()
        self.outer_image =pygame.transform.scale(self.outer_image, (w, h))
        player1 = Player("pavkata", "car.png", "red")
        player2 = Player("jonkata", "dog.png", "green")
        self.board.sprites()[0].players = {
            player1: player1.piece_image,
            player2: player2.piece_image,
            # player3 : player3.piece_image,
            # player4 : player4.piece_image
        }
        self.players = deque([player1, player2])
        self.dices = Dices(self)
        self.textures = [
            self.board,
            self.dices
        ]

    @property
    def current_player(self):
        return self.players[0]

    def make_shift(self):
        self.players.append(self.players.popleft())
    
    def blit(self, window):
        screen.blit(self.outer_image, (0, 0))
        self.screen.blit(self.image, (0, 0))
        for texture in self.textures:
            texture.blit(self.screen)
            texture.update()
        window.blit(self.screen, (board_screen_x, board_screen_y))




