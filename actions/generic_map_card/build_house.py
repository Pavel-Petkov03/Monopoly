from actions.base_action import Action


class GenericMapCardBuildHouseOnOwnerPropertyAction(Action):
    def __init__(self, renderer, map_card_state, current_player):
        super().__init__(renderer, map_card_state, current_player)

    def execute(self):
        money_to_pay = self.map_card_state.house_price
        self.current_player.money -= money_to_pay
        self.map_card_state.houses += 1
        self.render.remove_texture()