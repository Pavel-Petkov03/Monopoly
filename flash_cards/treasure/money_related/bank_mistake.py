
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class BankMistake(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("БАНКОВА ГРЕШКА ВЪВ ВАША ПОЛЗА ПОЛУЧАВАТЕ 200")

    def exec(self, renderer):
        renderer.current_player.money += 200

