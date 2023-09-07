
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class VacationFondProfit(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ВАКАНЦИОНЕН ФОНД ПОЛУЧАВАТЕ 100")

    def exec(self, renderer):
        renderer.current_player.money += 100