import pygame.sprite

from sprites.texture import TextureGroup
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

        inner_fill_rect_x = inner_surface.get_width() / 6
        inner_fill_rect_y = inner_surface.get_height() / 10
        self.create_text_and_blit(self.surface, f"Искате ли да купите този имот за {price} $", 30, "white",
                                  (self.width / 2, self.height / 10))

        inner_fill_surface = pygame.Surface((
            inner_surface.get_width() - 2 * inner_surface.get_width() / 6,
            inner_surface.get_height() - 2 * 4 * inner_surface.get_height() / 10))

        padding = inner_fill_surface.get_height() / 5
        padding_counter = inner_fill_surface.get_height() / 3
        print(map_card_name)

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

        button_yes = pygame.Surface((self.width / 4, self.height / 12))
        button_no = pygame.Surface((self.width / 4, self.height / 12))
        button_yes.fill("green")
        button_no.fill("red")

        self.create_text_and_blit(button_yes, "Да", 20, "white",
                                  (button_yes.get_width() / 2, button_yes.get_height() / 2))
        self.create_text_and_blit(button_no, "Не", 20, "white",
                                  (button_yes.get_width() / 2, button_yes.get_height() / 2))

        self.surface.blit(button_yes, (0, self.surface.get_height() - button_yes.get_height()))
        self.surface.blit(button_no, (
            self.surface.get_width() - button_no.get_width(), self.surface.get_height() - button_yes.get_height()))
        self.surface.blit(inner_surface, (inner_rect_x, inner_rect_y))

    def create_button(self):
        pass
