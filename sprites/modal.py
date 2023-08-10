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
    def __init__(self):
        super().__init__()





