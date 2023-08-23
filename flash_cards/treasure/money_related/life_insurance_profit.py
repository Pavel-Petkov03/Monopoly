from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class LifeInsuranceProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ЗАСТРАХОВКА ЖИВОТ. ПОЛУЧАВАТЕ 100")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 100