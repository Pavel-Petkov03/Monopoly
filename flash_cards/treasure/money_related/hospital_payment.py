from flash_cards.treasure.base import TreasureCard


class HospitalPayment(TreasureCard):
    def __init__(self):
        super().__init__("ПЛАТЕТЕ 100 ЗА БОЛНИЧНИ ТАКСИ")

    def exec(self, renderer):
        renderer.current_player.money -= 100