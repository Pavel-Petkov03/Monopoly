import pygame

from events.button_events import ButtonHoverEvent, ButtonClickEvent
from sprites.texture import Texture


class Button(Texture):
    def __init__(self, width_and_height_tuple=None, background=None, text=None, text_size=None, text_color=None,
                 blit_pos=None, hover_color=None,
                 action_class=None, inherit_x=None, inherit_y=None):
        super().__init__()
        self.blit_pos = blit_pos
        self.action_class = action_class
        self.hover_color = hover_color
        self.background = background
        self.is_hovered = False
        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.surface = pygame.Surface(width_and_height_tuple)
        self.rect = pygame.Rect(inherit_x + self.blit_pos[0], inherit_y + self.blit_pos[1], width_and_height_tuple[0],
                                width_and_height_tuple[1])
        self.surface.fill(background)
        self.text_pos = (width_and_height_tuple[0] / 2, width_and_height_tuple[1] / 2)
        self.event_list = [
            ButtonHoverEvent,
            ButtonClickEvent
        ]

    def blit(self, window):
        window.blit(self.surface, self.blit_pos)

    def activate_action(self):
        if self.action_class:
            self.action_class.execute()

    def update(self, *args, **kwargs) -> None:
        if self.is_hovered:
            self.surface.fill(self.hover_color)
        else:
            self.surface.fill(self.background)
        self.create_text_and_blit(self.surface, self.text, self.text_size, self.text_color, self.text_pos)