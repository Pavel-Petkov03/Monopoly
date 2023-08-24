from flash_cards.treasure.base import TreasureCard


class BeautyTax(TreasureCard):
    def __init__(self):
        super().__init__("ПЕЧЕЛИТЕ КОНКУРС ПО КРАСОТА И ПОЛУЧАВАТЕ 10")

    def exec(self, renderer):
        renderer.current_player.money += 10
