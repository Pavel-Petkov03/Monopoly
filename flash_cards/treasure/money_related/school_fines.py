
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class PaySchoolFines(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ПЛАТЕТЕ УЧИЛИЩНИ ТАКСИ 50")

    def exec(self, renderer):
        renderer.current_player.money -= 50