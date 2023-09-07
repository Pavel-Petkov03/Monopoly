
from flash_cards.treasure.money_related.base import MoneyRelatedTreasureCard


class BirthdayProfit(MoneyRelatedTreasureCard):
    def __init__(self):
        super().__init__("ИМАТЕ РОЖДЕН ДЕН. ПОЛУЧАВАТЕ ПО 10 ОТ ВСЕКИ ИГРАЧ")

    def exec(self, renderer):
        for player in renderer.players:
            if player != renderer.current_player:
                renderer.current_player.money += 10
                player.money -= 10