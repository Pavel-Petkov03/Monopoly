from flash_cards.chance.base import ChanceCard


class GoBackThreeSteps(ChanceCard):
    def __init__(self):
        super().__init__("ВЪРНЕТЕ СЕ ТРИ МЕСТА НАЗАД")

    def exec(self, renderer):
        index_to_go = renderer.current_player.board_index - 3
        renderer.dices.move_player_animation.animation_frame.forward = False
        renderer.dices.move_player_animation.get_fixed_place(index_to_go)