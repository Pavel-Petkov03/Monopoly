from flash_cards.chance.base import ChanceCard
from flash_cards.chance.go_to.base import GoToChanceCard


class GoToRedLast(GoToChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО УЧЛИЦА ОБОРИЩЕ\n"
                         "АКО ПРЕМИНЕТЕ ПРЕЗ НАЧАЛОТО ПОЛУЧАВАТЕ 200"
                         )

    def exec(self, renderer):
        renderer.dices.move_player_animation.get_fixed_place(24)
