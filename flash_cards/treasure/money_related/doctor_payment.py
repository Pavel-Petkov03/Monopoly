from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class DoctorPayment(TreasureCard):
    def __init__(self):
        super().__init__("ТАКСА ЗА ЛЕКАР. ПЛАТЕТЕ 50")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money -= 50
