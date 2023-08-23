from flash_cards.chance.base import ChanceCard
from renderers.board_render import BoardRenderer


class DateOfPaymentProfit(ChanceCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ЗАЕМА ВИ ЗА ИМОТ\n"
                         "ПОЛУЧАВАТЕ 150")

    def exec(self, renderer: BoardRenderer):
        money_to_pay = 150
        current_player = renderer.current_player
        current_player.money -= money_to_pay