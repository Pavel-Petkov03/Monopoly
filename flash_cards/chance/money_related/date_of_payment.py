
from flash_cards.chance.money_related.base import MoneyRelatedChanceCard


class DateOfPaymentProfit(MoneyRelatedChanceCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ЗАЕМА ВИ ЗА ИМОТ\n"
                         " 150")

    def exec(self, renderer):
        money_to_pay = 150
        current_player = renderer.current_player
        current_player.money -= money_to_pay