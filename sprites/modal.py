import pygame.sprite

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


class GenericMapCardModal(Modal):
    def __init__(self, inner_rect_color, map_card_name, inner_rect_data, price):
        self.inner_rect_color = inner_rect_color
        self.inner_rect_data = inner_rect_data
        super().__init__()
        inner_rect_x = self.x / 2
        inner_rect_y = self.y / 4
        inner_surface = pygame.Surface((self.width - 2 * self.x / 2,
                                        self.height - 2 * self.y / 4))
        inner_surface.fill("white")

        self.buttons = [
            Button(
                width_and_height_tuple=(self.width / 4, self.height / 12),
                background="green",
                text="Да",
                text_size=20,
                text_color="black",
                blit_pos=(0, self.surface.get_height() - self.height / 12)
            ),
            Button(
                width_and_height_tuple=(self.width / 4, self.height / 12),
                background="red",
                text="Не",
                text_size=20,
                text_color="black",
                blit_pos=(self.surface.get_width() - self.width / 4, self.surface.get_height() - self.height / 12)
            )
        ]
        for button in self.buttons:
            button.blit(self.surface)

        inner_fill_rect_x = inner_surface.get_width() / 6
        inner_fill_rect_y = inner_surface.get_height() / 10
        self.create_text_and_blit(self.surface, f"Искате ли да купите този имот за {price} $", 30, "white",
                                  (self.width / 2, self.height / 10))

        inner_fill_surface = pygame.Surface((
            inner_surface.get_width() - 2 * inner_surface.get_width() / 6,
            inner_surface.get_height() - 2 * 4 * inner_surface.get_height() / 10))

        padding = inner_fill_surface.get_height() / 5
        padding_counter = inner_fill_surface.get_height() / 3

        inner_fill_surface.fill(self.inner_rect_color)

        for word in map_card_name.split(" "):
            self.create_text_and_blit(inner_fill_surface, word, 25, (0, 0, 0),
                                      (inner_fill_surface.get_width() / 2, padding_counter))
            padding_counter += padding

        padding_counter += inner_surface.get_height() / 5
        for key, value in inner_rect_data.items():
            if key == "0":
                self.create_text_and_blit(inner_surface, f"Наем: {value} $", 25, (0, 0, 0),
                                          (inner_surface.get_width() / 2, padding_counter))
                padding_counter += inner_surface.get_height() / 8
            else:
                self.create_text_and_blit(inner_surface, f"{key} {'Къща' if key == '1' else 'Къщи'}", 20, (0, 0, 0),
                                          (inner_surface.get_width() / 4, padding_counter))
                self.create_text_and_blit(inner_surface, f"{value} $", 20, (0, 0, 0),
                                          (inner_surface.get_width() * 3 / 4, padding_counter))
            padding_counter += padding

        inner_surface.blit(inner_fill_surface, (inner_fill_rect_x, inner_fill_rect_y))

        self.surface.blit(inner_surface, (inner_rect_x, inner_rect_y))

    def create_button(self):
        pass

    def blit(self, window):
        for sprite in self.sprites():
            sprite.blit(self.surface)



class Button(Texture):
    def __init__(self, width_and_height_tuple=None, background=None, text=None, text_size=None, text_color=None,
                 blit_pos=None, hover_color=None,
                 action_class=None):
        super().__init__()
        self.blit_pos = blit_pos
        self.action_class = action_class
        self.hover_color = hover_color
        self.surface = pygame.Surface(width_and_height_tuple)
        self.surface.fill(background)
        text_pos = (width_and_height_tuple[0] / 2, width_and_height_tuple[1] / 2)
        self.create_text_and_blit(self.surface, text, text_size, text_color, text_pos)
        self.event_list = [

        ]

    def blit(self, window):
        window.blit(self.surface, self.blit_pos)


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

    def blit_text(self):
        padding = self.height / 5
        padding_counter = self.height / 3
        for word in self.map_card_name.split(" "):
            self.create_text_and_blit(self.surface, word, 25, (0, 0, 0), (self.width / 2, padding_counter))
            padding_counter += padding
        padding_counter += self.height / 5

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

