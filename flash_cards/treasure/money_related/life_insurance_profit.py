from flash_cards.treasure.base import TreasureCard


class LifeInsuranceProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ЗАСТРАХОВКА ЖИВОТ. ПОЛУЧАВАТЕ 100")

    def exec(self, renderer):
        renderer.current_player.money += 100