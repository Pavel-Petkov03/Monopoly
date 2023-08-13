import pygame

from sprites.base_map_card import BaseMapCard
from sprites.modal import GenericMapCardModal
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

    def add_additional_data(self):
        pygame.draw.rect(self.image, self.color, self.top_inner_rect)
        self.set_caption(self.caption, self.width / 5, self.width / 2, self.height / 3)
        self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)

    def update(self, *args, **kwargs) -> None:
        if self.new_player_on and kwargs["state"].players[0] in self.players:
            renderer_state = kwargs["state"]
            current_player = renderer_state.players[0]
            if current_player == self.owner:
                if self.neighborhood.all_map_cards_available():
                    if self.neighborhood.houses_same_count() or self.neighborhood.check_other_map_cards_have_more_houses_than_current_map_card(
                            self):
                        self.houses += 1
            else:
                if self.owner is None:
                    modal = GenericMapCardModal(self.color, self.price_dict)
                    self.add_modal_to_renderer(modal, renderer_state)
                else:
                    pass

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
