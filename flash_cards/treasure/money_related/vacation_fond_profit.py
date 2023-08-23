from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class VacationFondProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ВАКАНЦИОНЕН ФОНД ПОЛУЧАВАТЕ 100")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 100