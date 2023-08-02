import pygame

from sprites.base_map_card import BaseMapCard
from vars import screen_width, screen_height


class GenericMapCard(BaseMapCard):
    width = screen_width / 12
    height = screen_height / 6

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs)

    def add_additional_data(self):
        inner_rect = pygame.Rect(0, 0, self.width, self.height / 4)
        pygame.draw.rect(self.image, self.color, inner_rect)
        self.set_caption(self.caption, self.width / 5, self.width / 2, self.height / 3)
        self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)


class CornerMapCard(BaseMapCard):
    width = screen_width / 6
    height = screen_height / 6

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs, )
        self.width, self.height = (screen_width / 6, screen_height / 6)

    def add_additional_data(self):
        self.image_load(0)


class SideImageMapCard(BaseMapCard):
    width = screen_width / 12
    height = screen_height / 6

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs)

    def add_additional_data(self):
        self.image_load(30)
        self.set_caption(self.caption, self.width / 5, self.width / 2, self.height / 6)
        if self.price:
            self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)
