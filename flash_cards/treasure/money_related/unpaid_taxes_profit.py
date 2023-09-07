
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class UnpaidTaxesProfit(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ВРЪЩАТ ВИ НАДПЛАТЕНИ ДАНЪЦИ ПОЛУЧАВАТЕ 20")

    def exec(self, renderer):
        renderer.current_player.money += 20