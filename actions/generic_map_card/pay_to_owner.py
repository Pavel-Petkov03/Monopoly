from actions.base_action import Action


class GenericMapCardPayToOwnerAction(Action):
    def __init__(self, renderer, map_card_state, current_player):
        super().__init__(renderer, map_card_state, current_player)

    def execute(self):
        money_to_pay = self.map_card_state.calculate_current_price()
        self.current_player.money -= money_to_pay
        self.render.remove_texture()