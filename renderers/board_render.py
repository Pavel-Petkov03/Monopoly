from player import Player
from renderers.base_renderer import Renderer
from sprites.board import Board
from sprites.dice import Dice
from vars import screen_rect_size


class BoardRender(Renderer):
    def __init__(self, players):
        self.players = players
        super().__init__()
        self.board = Board()
        self.d = Dice(screen_rect_size / 2, screen_rect_size / 2)
        self.textures = [
            self.board,
            self.d
        ]

        player = Player("pavkata", "car.png")
        player2 = Player("pavkata", "ship.png")
        player3 = Player("pavkata", "dog.png")
        player4 = Player("pavkata", "truck.png")
        self.board.sprites()[0].players = {
            player: player.piece_image,
            # player2 : player2.piece_image,
            # player3 : player3.piece_image,
            # player4 : player4.piece_image
        }