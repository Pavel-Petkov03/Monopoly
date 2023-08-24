from flash_cards.treasure.base import TreasureCard


class BankMistake(TreasureCard):
    def __init__(self):
        super().__init__("БАНКОВА ГРЕШКА ВЪВ ВАША ПОЛЗА ПОЛУЧАВАТЕ 200")

    def exec(self, renderer):
        renderer.current_player.money += 200

