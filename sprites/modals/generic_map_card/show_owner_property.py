from actions.generic_map_card.remove_modal import RemoveModalAction
from sprites.modals.generic_map_card.base import GenericMapCardModal


class ShowOwnerPropertyMapCardModal(GenericMapCardModal):
    def __init__(self, renderer, map_card_state, current_player):
        super().__init__(renderer, map_card_state, current_player)
        self.ok_button_action_class = RemoveModalAction
        self.add([self.get_ok_button()])
        self.set_header(f"Добре дошъл в твоят имот {current_player.name}")