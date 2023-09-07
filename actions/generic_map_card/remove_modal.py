from actions.generic_map_card.base_action import GenericMapCardAction


class RemoveModalAction(GenericMapCardAction):
    def __init__(self, renderer, map_card_state, current_player):
        super().__init__(renderer, map_card_state, current_player)

    def execute(self):
        self.render.remove_texture()
        super().execute()
