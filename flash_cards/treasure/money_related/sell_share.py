from flash_cards.treasure.base import TreasureCard


class SellShare(TreasureCard):
    def __init__(self):
        super().__init__("ПРОДАВАТЕ АКЦИИ И ПОЛУЧАВАТЕ 50")

    def exec(self, renderer):
        renderer.current_player.money += 50