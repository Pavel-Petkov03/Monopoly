
from flash_cards.chance.money_related.base import MoneyRelatedChanceCard


class FineForFastDriving(MoneyRelatedChanceCard):
    def __init__(self):
        super().__init__("ГЛОБА ЗА ПРЕВИШЕНА СКОРОСТ 15")

    def exec(self, renderer):
        money_to_pay = 15
        current_player = renderer.current_player
        current_player.money -= money_to_pay