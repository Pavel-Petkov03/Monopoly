from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class ConsultingProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПОЛУЧАВАТЕ ХОНОРОР ЗА КОНСУЛТАНТ 25")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 25
