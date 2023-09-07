from flash_cards.chance.go_to.base import GoToChanceCard


class GoToFirstStation(GoToChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО ГАРА СОФИЯ\n"
                         "АКО ПРЕМИНЕТЕ ПРЕЗ НАЧАЛОТО ПОЛУЧАВАТЕ 200"
                         )

    def exec(self, renderer):
        renderer.dices.move_player_animation.get_fixed_place(5)