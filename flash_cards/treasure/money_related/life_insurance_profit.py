
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class LifeInsuranceProfit(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ЗАСТРАХОВКА ЖИВОТ. ПОЛУЧАВАТЕ 100")

    def exec(self, renderer):
        renderer.current_player.money += 100