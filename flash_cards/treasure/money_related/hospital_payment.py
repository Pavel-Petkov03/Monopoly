from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class HospitalPayment(TreasureCard):
    def __init__(self):
        super().__init__("ПЛАТЕТЕ 100 ЗА БОЛНИЧНИ ТАКСИ")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money -= 100