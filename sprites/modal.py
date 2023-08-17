import pygame.sprite

from events.button_events import ButtonHoverEvent, ButtonClickEvent
from sprites.texture import TextureGroup, Texture
from vars import screen_rect_size


class Modal(TextureGroup):
    def __init__(self):
        super().__init__()
        self.x = screen_rect_size / 16 * 4
        self.y = screen_rect_size / 16 * 4
        self.width = screen_rect_size - screen_rect_size / 16 * 8
        self.height = screen_rect_size - screen_rect_size / 16 * 8
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill("black")

    def blit(self, window):
        window.blit(self.surface, (self.x, self.y))


class MapCard(Texture):
    def __init__(self, width, height, inner_surface_fill_color, map_card_name, map_card_data, blit_pos):
        super().__init__()
        self.width = width
        self.height = height
        self.inner_surface_fill_color = inner_surface_fill_color
        self.map_card_name = map_card_name
        self.map_card_data = map_card_data
        self.blit_pos = blit_pos

        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill("white")
        self.inner_fill_surface = pygame.Surface((2 / 3 * self.width, 1 / 5 * self.height))
        self.inner_fill_surface.fill(self.inner_surface_fill_color)
        self.blit_text()

    def blit_text(self):
        padding = self.inner_fill_surface.get_height() / 5
        padding_counter = self.inner_fill_surface.get_height() / 3
        for word in self.map_card_name.split(" "):
            self.create_text_and_blit(self.inner_fill_surface, word, 25, (0, 0, 0),
                                      (self.inner_fill_surface.get_width() / 2, padding_counter))
            padding_counter += padding
        padding_counter += self.height / 5
        self.surface.blit(self.inner_fill_surface, (self.width / 6, self.height / 10))

        for key, value in self.map_card_data.items():
            if key == "0":
                self.create_text_and_blit(self.surface, f"Наем: {value} $", 25, (0, 0, 0),
                                          (self.width / 2, padding_counter))
                padding_counter += self.height / 8
            else:
                self.create_text_and_blit(self.surface, f"{key} {'Къща' if key == '1' else 'Къщи'}", 20, (0, 0, 0),
                                          (self.width / 4, padding_counter))
                self.create_text_and_blit(self.surface, f"{value} $", 20, (0, 0, 0),
                                          (self.width * 3 / 4, padding_counter))
            padding_counter += padding

    def blit(self, window):
        window.blit(self.surface, self.blit_pos)


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


class GenericMapCardModal(Modal):
    def __init__(self, inner_rect_color, map_card_name, inner_rect_data, price):
        self.inner_rect_color = inner_rect_color
        self.inner_rect_data = inner_rect_data
        self.map_card_name = map_card_name
        super().__init__()
        self.map_card = MapCard(
            self.width - 2 * self.x / 2,
            self.height - 2 * self.y / 4,
            self.inner_rect_color,
            self.map_card_name,
            self.inner_rect_data,
            (self.x / 2, self.y / 4)
        )
        self.button_yes = Button(
            width_and_height_tuple=(self.width / 4, self.height / 12),
            background="green",
            text="Да",
            text_size=20,
            text_color="black",
            blit_pos=(0, self.surface.get_height() - self.height / 12),
            hover_color="yellow",
            inherit_x=self.x,
            inherit_y=self.y
        )
        self.button_no = Button(
            width_and_height_tuple=(self.width / 4, self.height / 12),
            background="red",
            text="Не",
            text_size=20,
            text_color="black",
            blit_pos=(self.surface.get_width() - self.width / 4, self.surface.get_height() - self.height / 12),
            hover_color="yellow",
            inherit_x=self.x,
            inherit_y=self.y
        )

        self.add([self.map_card, self.button_no, self.button_yes])
        self.create_text_and_blit(self.surface, f"Искате ли да купите този имот за {price} $", 30, "white",
                                  (self.width / 2, self.height / 10))

    def blit(self, window):
        for sprite in self.sprites():
            sprite.blit(self.surface)
        super().blit(window)
