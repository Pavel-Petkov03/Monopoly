from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class BankMistake(TreasureCard):
    def __init__(self):
        super().__init__("БАНКОВА ГРЕШКА ВЪВ ВАША ПОЛЗА ПОЛУЧАВАТЕ 200")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 200

