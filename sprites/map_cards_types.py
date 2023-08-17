import pygame

from sprites.base_map_card import BaseMapCard
from sprites.modal import GenericMapCardModal, ShowOwnerPropertyMapCardModal, BuyGenericMapCardModal, \
    BuildHouseOnOwnerPropertyMapCardModal, PayToOwnerMapCardModal
from vars import screen_rect_size, neighborhoods


class GenericMapCard(BaseMapCard):
    width = screen_rect_size / 12
    height = screen_rect_size / 16 * 2

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs)
        self.owner = None
        self.new_player_on = False
        self.houses = 0
        self.neighborhood = neighborhoods[self.neighborhood]
        self.neighborhood.add_generic_map_cards(self)

    def calculate_current_price(self, current_player):
        if self.neighborhood.check_all_map_cards_have_same_owner(current_player):
            return self.price * 2
        return self.price_dict[self.houses]

    def add_additional_data(self):
        pygame.draw.rect(self.image, self.color, self.top_inner_rect)
        self.set_caption(self.caption, self.width / 5, self.width / 2, self.height / 3)
        self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)

    def update(self, *args, **kwargs) -> None:
        if self.new_player_on and kwargs["state"].players[0] in self.players:
            renderer_state = kwargs["state"]
            current_player = renderer_state.players[0]
            modal_data = (self, renderer_state, current_player)
            self.get_proper_modal(current_player, modal_data)
            self.new_player_on = False
    
    def get_proper_modal(self, current_player, modal_data):
        if current_player == self.owner:
            if self.neighborhood.all_map_cards_available() and self.neighborhood.houses_same_count() or self.neighborhood.check_other_map_cards_have_more_houses_than_current_map_card(
                    self):
                modal = BuildHouseOnOwnerPropertyMapCardModal(*modal_data)
            else:
                modal = ShowOwnerPropertyMapCardModal(*modal_data)

        else:
            if self.owner is None:
                modal = BuyGenericMapCardModal(*modal_data)
            else:
                modal = PayToOwnerMapCardModal(*modal_data)
        modal_data[1].add_texture(modal)



class CornerMapCard(BaseMapCard):
    width = screen_rect_size / 16 * 2
    height = screen_rect_size / 16 * 2

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs, )

    def add_additional_data(self):
        self.image_load(0)


class SideImageMapCard(BaseMapCard):
    width = screen_rect_size / 12
    height = screen_rect_size / 16 * 2

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs)

    def add_additional_data(self):
        self.image_load(30)
        self.set_caption(self.caption, self.width / 5, self.width / 2, self.height / 6)
        if self.price:
            self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)
