
from flash_cards.chance.go_to.base import GoToChanceCard


class GoToStart(GoToChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО НАЧАЛО И (ПОЛУЧАВАТЕ 200)")

    def exec(self, renderer):
        renderer.dices.move_player_animation.get_fixed_place(0)
