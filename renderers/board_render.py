from collections import deque

from player import Player
from renderers.base_renderer import Renderer
from sprites.board import Board
from sprites.dice import Dices


class BoardRenderer(Renderer):
    def __init__(self, players):
        super().__init__()
        self.board = Board(self)

        player1 = Player("pavkata", "car.png")
        player2 = Player("pavkata", "dog.png")
        self.board.sprites()[0].players = {
            player1: player1.piece_image,
            player2: player2.piece_image,
            # player3 : player3.piece_image,
            # player4 : player4.piece_image
        }
        self.players = deque([player1, player2])
        self.current_player = self.players[0]
        self.dices = Dices(self)
        self.textures = [
            self.board,
            self.dices
        ]

