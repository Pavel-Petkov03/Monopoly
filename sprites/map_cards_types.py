import pygame

from sprites.modals.generic_map_card.show_owner_property import ShowOwnerPropertyMapCardModal
from sprites.modals.generic_map_card.build_house import BuildHouseOnOwnerPropertyMapCardModal
from sprites.modals.generic_map_card.buy import BuyGenericMapCardModal
from sprites.modals.generic_map_card.pay_to_owner import PayToOwnerMapCardModal
from sprites.base_map_card import BaseMapCard

from vars import screen_rect_size, neighborhoods


class GenericMapCard(BaseMapCard):
    width = screen_rect_size / 12
    height = screen_rect_size / 16 * 2

    def __init__(self, x, y, renderer, **kwargs):
        super().__init__(x, y, **kwargs)
        self.owner = None
        self.new_player_on = False
        self.houses = 0
        self.neighborhood = neighborhoods[self.neighborhood]
        self.neighborhood.add_generic_map_cards(self)
        self.house_image = self.get_house_image()
        self.renderer = renderer

    def calculate_current_price(self):
        if self.neighborhood.check_all_map_cards_have_same_owner(self.owner):
            return self.price * 2
        return self.price_dict[self.houses]

    def add_additional_data(self):
        pygame.draw.rect(self.image, self.color, self.top_inner_rect)
        self.draw_houses()
        self.set_caption(self.caption, self.width / 5, self.width / 2, self.height / 3)
        self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)

    def draw_houses(self):
        if self.houses == 5:
            current_location_image = "images/board/hotel.png"
        else:
            current_x = 0
            for i in range(self.houses):
                self.image.blit(self.house_image, (current_x, self.top_inner_rect.height / 2))
                current_x += self.house_image.get_width()

    def get_house_image(self):
        image = pygame.image.load("images/board/house.png")
        return pygame.transform.scale(image, (self.top_inner_rect.width / 4, self.top_inner_rect.height / 2))

    def get_hotel_image(self):
        image = pygame.image.load("images/board/hotel.png")
        return pygame.transform.scale(image, (self.top_inner_rect.width / 2, self.top_inner_rect.height / 2))

    def update(self, *args, **kwargs) -> None:
        if self.new_player_on and self.renderer.current_player in self.players:
            current_player = self.renderer.current_player
            modal_data = (self, self.renderer, current_player)
            self.get_proper_modal(current_player, modal_data)
            self.new_player_on = False

    def get_proper_modal(self, current_player, modal_data):
        if current_player == self.owner:
            if self.neighborhood.check_all_map_cards_have_same_owner(current_player) and (
                    self.neighborhood.houses_same_count() or self.neighborhood.check_other_map_cards_have_more_houses_than_current_map_card(
                self)):
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

    def __init__(self, x, y, renderer, **kwargs):
        super().__init__(x, y, renderer, **kwargs)

    def add_additional_data(self):
        self.image_load(0)


class SideImageMapCard(BaseMapCard):
    width = screen_rect_size / 12
    height = screen_rect_size / 16 * 2

    def __init__(self, x, y, renderer, **kwargs):
        super().__init__(x, y, renderer, **kwargs)

    def add_additional_data(self):
        self.image_load(30)
        self.set_caption(self.caption, self.width / 5, self.width / 2, self.height / 6)
        if self.price:
            self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)
