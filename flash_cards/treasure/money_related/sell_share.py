from chance_and_treasure import TreasureCard
from renderers.board_render import BoardRenderer


class SellShare(TreasureCard):
    def __init__(self):
        super().__init__("ПРОДАВАТЕ АКЦИИ И ПОЛУЧАВАТЕ 50")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 50