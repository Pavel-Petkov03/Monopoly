from actions.base_action import Action


class GenericMapCardAction(Action):
    def __init__(self, renderer, map_card_state, current_player):
        super().__init__(renderer)
        self.map_card_state = map_card_state
        self.current_player = current_player

    def execute(self):
        self.render.make_shift()
