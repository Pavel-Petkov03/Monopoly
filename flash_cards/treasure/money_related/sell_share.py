
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class SellShare(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ПРОДАВАТЕ АКЦИИ И ПОЛУЧАВАТЕ 50")

    def exec(self, renderer):
        renderer.current_player.money += 50