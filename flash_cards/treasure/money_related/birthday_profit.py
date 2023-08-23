from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class BirthdayProfit(TreasureCard):
    def __init__(self):
        super().__init__("ИМАТЕ РОЖДЕН ДЕН. ПОЛУЧАВАТЕ ПО 10 ОТ ВСЕКИ ИГРАЧ")

    def exec(self, renderer: BoardRenderer):
        for player in renderer.players:
            if player != renderer.current_player:
                renderer.current_player.money += 10
                player.money -= 10