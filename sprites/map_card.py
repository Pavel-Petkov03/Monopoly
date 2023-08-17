import pygame

from sprites.texture import Texture


class GenericMapCard(Texture):
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