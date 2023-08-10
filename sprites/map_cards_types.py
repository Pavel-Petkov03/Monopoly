import pygame

from events.base_event import Event
from sprites.base_map_card import BaseMapCard
from vars import screen_rect_size



class GenericMapCardEvent(Event):


    @staticmethod
    def condition(texture, event_type):
        return True

    @staticmethod
    def execute(texture):
        texture.new_player_on = True


class GenericMapCard(BaseMapCard):
    width = screen_rect_size / 12
    height = screen_rect_size / 16 * 2

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs)
        self.owner = None
        self.new_player_on = False
        self.event_list = [
            GenericMapCardEvent
        ]

    def add_additional_data(self):
        pygame.draw.rect(self.image, self.color, self.top_inner_rect)
        self.set_caption(self.caption, self.width / 5, self.width / 2, self.height / 3)
        self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)

    def update(self, *args, **kwargs) -> None:
        if self.new_player_on:
            current_player = kwargs["current_player"]
            if current_player == self.owner:
                pass
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
