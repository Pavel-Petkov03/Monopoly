from actions.generic_map_card.buy import GenericMapCardBuyAction
from modals.generic_map_card.base import GenericMapCardModal


class BuyGenericMapCardModal(GenericMapCardModal):
    def __init__(self, renderer, map_card_state, current_player):
        super().__init__(renderer, map_card_state, current_player)
        self.yes_button_action_class = GenericMapCardBuyAction
        self.add([self.get_yes_button(), self.get_no_button()])
        self.set_header(f"Искате ли да купите този имот за {self.map_card_state.price} $")