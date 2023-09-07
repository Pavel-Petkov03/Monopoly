
from flash_cards.chance.money_related.base import MoneyRelatedChanceCard


class GetDividends(MoneyRelatedChanceCard):
    def __init__(self):
        super().__init__("БАНКАТА ВИ ИЗПЛАЩА ДИВИДЕНТ ОТ 50")

    def exec(self, renderer):
        money_to_get = 50
        current_player = renderer.current_player
        current_player.money += money_to_get