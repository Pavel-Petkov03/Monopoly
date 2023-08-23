from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class BeautyTax(TreasureCard):
    def __init__(self):
        super().__init__("ПЕЧЕЛИТЕ КОНКУРС ПО КРАСОТА И ПОЛУЧАВАТЕ 10")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 10
