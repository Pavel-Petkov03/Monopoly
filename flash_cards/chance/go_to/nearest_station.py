
from flash_cards.chance.go_to.base import GoToChanceCard


class GoToNearestStation(GoToChanceCard):
    def __init__(self):
        super().__init__(
            "ПРОДЪЛЖЕТЕ ДО НАЙ - БЛИЗКАТА ГАРА\n"
            "АКО НЕ Е КУПЕНА МОЖЕ ДА Я КУПИТE\n"
            "АКО НЕ Е КУПЕНА ПЛАТЕТЕ СЪОВЕТНАТА ЦЕНА НА СОБСТВЕНИКА"
        )

    def exec(self, renderer):
        renderer.dices.move_player_animation.get_nearest_place("station")