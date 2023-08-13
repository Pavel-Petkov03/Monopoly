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
        self.surface.fill("white")

    def blit(self, window):
        window.blit(self.surface, (self.x, self.y))


class GenericMapCardModal(Modal):
    def __init__(self, inner_rect_color, inner_rect_data):
        self.inner_rect_color = inner_rect_color
        self.inner_rect_data = inner_rect_data
        super().__init__()
        border_color = (0, 0, 0)
        border_padding = 1
        inner_rect = pygame.Rect(self.x / 2 + border_padding, border_padding + self.y / 4,
                                 self.width - 2 * border_padding - 2 * self.x / 2,
                                 self.height - 2 * border_padding - 2 * self.y / 4)
        inner_fill_rect = pygame.Rect(inner_rect.x + inner_rect.width / 6,
                                      inner_rect.y + inner_rect.height / 10,
                                      inner_rect.width - 2 * inner_rect.width / 6,
                                      inner_rect.height - 2 * 4 * inner_rect.height / 10)

        pygame.draw.rect(self.surface, border_color, inner_rect, border_padding)
        pygame.draw.rect(self.surface, inner_rect_color, inner_fill_rect)
