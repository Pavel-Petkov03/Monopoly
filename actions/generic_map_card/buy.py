
from actions.generic_map_card.base_action import GenericMapCardAction


class GenericMapCardBuyAction(GenericMapCardAction):
    def __init__(self, renderer, map_card_state, current_player):
        super().__init__(renderer,map_card_state, current_player)

    def execute(self):
        self.map_card_state.owner = self.current_player
        self.current_player.money -= int(self.map_card_state.price)
        print(f"current player became owner and lost {self.map_card_state.price} to buy {self.map_card_state.caption}")
        self.renderer.remove_texture()
        super().execute()