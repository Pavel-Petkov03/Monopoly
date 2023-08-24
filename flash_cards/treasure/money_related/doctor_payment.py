from flash_cards.treasure.base import TreasureCard


class DoctorPayment(TreasureCard):
    def __init__(self):
        super().__init__("ТАКСА ЗА ЛЕКАР. ПЛАТЕТЕ 50")

    def exec(self, renderer):
        renderer.current_player.money -= 50
