
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class HeritageProfit(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ПОЛУЧАВАТЕ НАСЛЕДСТВО ОТ 100")

    def exec(self, renderer):
        renderer.current_player.money += 100