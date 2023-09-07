
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class ConsultingProfit(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ПОЛУЧАВАТЕ ХОНОРОР ЗА КОНСУЛТАНТ 25")

    def exec(self, renderer):
        renderer.current_player.money += 25
