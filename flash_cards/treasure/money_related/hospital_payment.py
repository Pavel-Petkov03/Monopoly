
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class HospitalPayment(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ПЛАТЕТЕ 100 ЗА БОЛНИЧНИ ТАКСИ")

    def exec(self, renderer):
        renderer.current_player.money -= 100