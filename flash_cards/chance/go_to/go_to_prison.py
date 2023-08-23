from flash_cards.chance.base import ChanceCard
from renderers.board_render import BoardRenderer


class GoToPrison(ChanceCard):
    def __init__(self):
        super().__init__("ОТИВАТЕ ДИРЕКТНО В ЗАТВОРА.НЕ ПРЕМИНАВАТЕ ПРЕЗ НАЧАЛО И НЕ ПОЛУЧАВАТЕ 200")

    def exec(self, renderer: BoardRenderer):
        renderer.dices.move_player_animation.forward = False
        renderer.current_player.in_prison = True
        renderer.dices.move_player_animation.get_fixed_place(10)
