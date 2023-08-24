from flash_cards.treasure.base import TreasureCard


class PaySchoolFines(TreasureCard):
    def __init__(self):
        super().__init__("ПЛАТЕТЕ УЧИЛИЩНИ ТАКСИ 50")

    def exec(self, renderer):
        renderer.current_player.money -= 50