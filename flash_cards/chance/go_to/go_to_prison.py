
from flash_cards.chance.go_to.base import GoToChanceCard


class GoToPrison(GoToChanceCard):
    def __init__(self):
        super().__init__("ОТИВАТЕ ДИРЕКТНО В ЗАТВОРА.НЕ ПРЕМИНАВАТЕ ПРЕЗ НАЧАЛО И НЕ ПОЛУЧАВАТЕ 200")

    def exec(self, renderer):
        renderer.dices.move_player_animation.forward = False
        renderer.current_player.in_prison = True
        renderer.dices.move_player_animation.get_fixed_place(10)
