from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class HeritageProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПОЛУЧАВАТЕ НАСЛЕДСТВО ОТ 100")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 100