
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class DoctorPayment(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ТАКСА ЗА ЛЕКАР. ПЛАТЕТЕ 50")

    def exec(self, renderer):
        renderer.current_player.money -= 50
