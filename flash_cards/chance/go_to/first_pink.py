from flash_cards.chance.base import ChanceCard
from renderers.board_render import BoardRenderer


class GoToFirstPink(ChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО ПЛОЩАД МАКЕДОНИЯ\n"
                         "АКО ПРЕМИНЕТЕ ПРЕЗ НАЧАЛОТО ПОЛУЧАВАТЕ 200"
                         )

    def exec(self, renderer: BoardRenderer):
        renderer.dices.move_player_animation.get_fixed_place(11)