import pygame.sprite

from sprites.texture import Texture
from vars import screen_rect_size


class Modal(Texture):
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
    def __init__(self, inner_rect_color, map_card_name, inner_rect_data):
        self.inner_rect_color = inner_rect_color
        self.inner_rect_data = inner_rect_data
        super().__init__()
        border_padding = 1
        inner_rect_x = self.x / 2 + border_padding
        inner_rect_y = border_padding + self.y / 4
        inner_surface = pygame.Surface((self.width - 2 * border_padding - 2 * self.x / 2,
                                        self.height - 2 * border_padding - 2 * self.y / 4))
        inner_surface.fill("white")

        inner_fill_rect_x = inner_surface.get_width() / 6
        inner_fill_rect_y = inner_surface.get_height() / 10

        inner_fill_surface = pygame.Surface((
            inner_surface.get_width() - 2 * inner_surface.get_width() / 6,
            inner_surface.get_height() - 2 * 4 * inner_surface.get_height() / 10))

        padding = inner_fill_surface.get_height() / 5
        padding_counter = inner_fill_surface.get_height() / 3
        print(map_card_name)

        inner_fill_surface.fill(self.inner_rect_color)

        for word in map_card_name.split(" "):
            text_surface = self.create_font(word, 25, (0, 0, 0))
            text_rect = text_surface.get_rect(
                center=(inner_fill_surface.get_width() / 2, padding_counter))
            inner_fill_surface.blit(text_surface, text_rect)
            padding_counter += padding

        padding_counter += inner_surface.get_height() / 5
        for key, value in inner_rect_data.items():
            if key == "0":
                text_surface = self.create_font(f"Наем: {value} $", 25, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(inner_surface.get_width() / 2, padding_counter))
                inner_surface.blit(text_surface, text_rect)
                padding_counter += inner_surface.get_height() / 8
            else:
                text_surface_left = self.create_font(f"{key} {'Къща' if key == '1' else 'Къщи'}", 20, (0, 0, 0))
                text_surface_right = self.create_font(f"{value} $", 20, (0, 0, 0))
                text_rect_left = text_surface_left.get_rect(
                    center=(inner_surface.get_width() / 4, padding_counter))
                text_rect_right = text_surface_right.get_rect(
                    center=(inner_surface.get_width() * 3 / 4, padding_counter))
                inner_surface.blit(text_surface_left, text_rect_left)
                inner_surface.blit(text_surface_right, text_rect_right)
            padding_counter += padding

        inner_surface.blit(inner_fill_surface, (inner_fill_rect_x, inner_fill_rect_y))

        button_yes = pygame.Surface((self.width / 4, self.height / 12))
        button_yes.fill("green")
        button_yes_text_surface = self.create_font("Да", 20, "white")
        button_yes_text_rect = button_yes_text_surface.get_rect(
            center=(button_yes.get_width() / 2, button_yes.get_height() / 2))

        button_yes.blit(button_yes_text_surface, button_yes_text_rect)
        inner_surface.blit(button_yes, (inner_surface.get_width() / 4, inner_surface.get_height() / 8 * 7))
        self.surface.blit(inner_surface, (inner_rect_x, inner_rect_y))

    @staticmethod
    def create_font(text, size, color):
        font = pygame.font.Font(None, int(size))
        text_surface = font.render(text, True, color)
        return text_surface
