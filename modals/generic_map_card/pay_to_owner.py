from actions.generic_map_card.pay_to_owner import GenericMapCardPayToOwnerAction
from modals.generic_map_card.base import GenericMapCardModal


class PayToOwnerMapCardModal(GenericMapCardModal):
    def __init__(self,renderer, map_card_state, current_player):
        super().__init__(renderer, map_card_state, current_player)
        self.ok_button_action_class = GenericMapCardPayToOwnerAction
        self.add([self.get_ok_button()])

        self.set_header(f"Имотът принадлежи на {current_player.name} и престоят в него струва {map_card_state.calculate_current_price(current_player)} $")