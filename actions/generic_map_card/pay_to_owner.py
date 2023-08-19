
from actions.generic_map_card.base_action import GenericMapCardAction


class GenericMapCardPayToOwnerAction(GenericMapCardAction):
    def __init__(self, renderer, map_card_state, current_player):
        super().__init__(renderer, map_card_state, current_player)

    def execute(self):
        money_to_pay = self.map_card_state.calculate_current_price()
        self.current_player.money -= money_to_pay
        self.render.remove_texture()