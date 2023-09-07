import pygame

from flash_cards.decks import ChanceHolder, TreasureHolder
from sprites.texture import Texture


class GenericMapCard(Texture):
    def __init__(self, width, height, inner_surface_fill_color, map_card_name, map_card_data, blit_pos):
        super().__init__(width, height)
        self.inner_surface_fill_color = inner_surface_fill_color
        self.map_card_name = map_card_name
        self.map_card_data = map_card_data
        self.blit_pos = blit_pos
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


class TreasureAndChanceCardDesign(Texture):
    def __init__(self, width, height, side_image_type, holder):
        super().__init__(width, height)
        self.surface.fill("white")
        x = self.width / 17
        pygame.draw.line(self.surface, "black", (x, x), (self.width - x, x))
        pygame.draw.line(self.surface, "black", (x, x), (x, self.height - x))
        pygame.draw.line(self.surface, "black", (self.width - x, x), (self.width - x, self.height - x))
        pygame.draw.line(self.surface, "black", (self.width - x, self.height - x), (x, self.height - x))
        padding = 2 * x
        self.create_text_and_blit(self.surface, side_image_type, 30, "black", (self.width / 2, padding))



class SideImageMapCard(Texture):
    def __init__(self, width, height, side_image_type, map_card_name, image_path):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.side_image_type = side_image_type
        self.map_card_name = map_card_name
        self.surface = pygame.Surface((self.width, self.height))
        self.image_path = image_path
        self.padding_counter = 0
        self.chance_holder = ChanceHolder()
        self.treasure_holder = TreasureHolder()
        self.surface.fill("white")

    def header_data(self):
        self.padding_counter = self.surface.get_height() / 20
        padding = self.surface.get_height() / 20
        self.create_text_and_blit(self.surface, self.map_card_name, 25, (0, 0, 0),
                                  (self.surface.get_width() / 2, self.padding_counter))
        self.padding_counter += padding
        image = self.load_image()
        self.surface.blit(image, (self.surface.get_width() / 2, self.padding_counter))

    def station(self):
        for key, value in {str(i): int(i) * 50 for i in range(1, 5)}.items():
            self.create_text_and_blit(self.surface, f"{f'Наем за {key}'}", 20, (0, 0, 0),
                                      (self.width / 4, self.padding_counter))
            self.create_text_and_blit(self.surface, f"{value} $", 20, (0, 0, 0),
                                      (self.width * 3 / 4, self.padding_counter))
            self.padding_counter += self.surface.get_height() / 20

    def chance(self):
        self.padding_counter += self.surface.get_height() / 5
        card = self.chance_holder.get_card()
        self.create_text_and_blit(self.surface, card.header_message, 25, (0, 0, 0),
                                  (self.surface.get_width() / 2, self.padding_counter))

    def treasure(self):
        self.padding_counter += self.surface.get_height() / 5
        card = self.treasure_holder.get_card()
        self.create_text_and_blit(self.surface, card.header_message, 25, (0, 0, 0),
                                  (self.surface.get_width() / 2, self.padding_counter))

    def public_services(self):
        pass

    def load_image(self):
        image = pygame.image.load(self.image_path)
        return pygame.transform.scale(image, (self.surface.get_width() / 10, self.surface.get_height() / 10))
