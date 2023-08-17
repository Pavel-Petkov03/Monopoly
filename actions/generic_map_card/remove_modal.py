from actions.base_action import Action


class RemoveModalAction(Action):
    def __init__(self,renderer,map_card_state, current_player):
        super().__init__(renderer,map_card_state, current_player)

    def execute(self):
        self.render.remove_texture()