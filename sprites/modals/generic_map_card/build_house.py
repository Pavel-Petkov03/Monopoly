from actions.generic_map_card.build_house import GenericMapCardBuildHouseOnOwnerPropertyAction
from sprites.modals.generic_map_card.base import GenericMapCardModal


class BuildHouseOnOwnerPropertyMapCardModal(GenericMapCardModal):
    def __init__(self, renderer, map_card_state, current_player):
        super().__init__(renderer, map_card_state, current_player)
        self.yes_button_action_class = GenericMapCardBuildHouseOnOwnerPropertyAction
        self.add([self.get_yes_button(), self.get_no_button()])
        self.set_header(f"Искате ли да построите къща на този имот за {self.map_card_state.price} $")