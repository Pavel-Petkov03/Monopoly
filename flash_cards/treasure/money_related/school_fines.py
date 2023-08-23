from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class PaySchoolFines(TreasureCard):
    def __init__(self):
        super().__init__("ПЛАТЕТЕ УЧИЛИЩНИ ТАКСИ 50")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money -= 50