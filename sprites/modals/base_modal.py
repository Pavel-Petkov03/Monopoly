import pygame

from sprites.texture import TextureGroup
from vars import screen_rect_size, size, w


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

    def set_header(self, header):
        print(header)
        words = self.word_splitter(header)
        padding = 0
        for row in words:
            self.create_text_and_blit(
                self.surface,
                row,
                30 - len(row.split(" ")),
                "white",
                (self.width / 2, self.height / 10 + padding)
            )
            padding += self.height / 15


