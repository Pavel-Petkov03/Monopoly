from flash_cards.treasure.base import TreasureCard


class HeritageProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПОЛУЧАВАТЕ НАСЛЕДСТВО ОТ 100")

    def exec(self, renderer):
        renderer.current_player.money += 100