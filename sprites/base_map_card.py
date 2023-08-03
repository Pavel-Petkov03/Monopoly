import pygame
from vars import screen, screen_rect_size


class BaseMapCard(pygame.sprite.Sprite):
    width = 0
    height = 0

    def __init__(self, x, y, color=None, caption=None, inside_image_path=None, price=None, rotation=None):
        super().__init__()
        self.image = None
        self.x = x
        self.y = y
        self.inside_image_path = f"images/board/{inside_image_path}"
        self.caption = caption
        self.color = color
        self.price = price
        self.rotation = rotation

    def set_rect(self):
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("white")
        pygame.draw.rect(self.image, "black", self.image.get_rect(), 1)
        self.add_additional_data()

    def add_additional_data(self):
        pass

    def image_load(self, padding_percent):
        padding_top = int(self.height * (padding_percent / 100))
        padding_bottom = int(self.height * (padding_percent / 100))
        new_height = self.height - padding_top - padding_bottom
        inside_image = pygame.image.load(self.inside_image_path).convert_alpha()
        scale_factor = new_height / inside_image.get_height()
        new_width = int(inside_image.get_width() * scale_factor)
        scaled_image = pygame.transform.scale(inside_image, (new_width, new_height)).convert_alpha()
        x_offset = (self.width - new_width) // 2
        self.image.blit(scaled_image, (x_offset, padding_top))

    def set_caption(self, text, size, width, height):
        words = text.split(" ")
        padding = self.height / 12
        padding_counter = 0
        for word in words:
            font = pygame.font.Font(None, int(size))
            text_surface = font.render(word, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(width, height + padding_counter))
            padding_counter += padding
            self.image.blit(text_surface, text_rect)

    def blit(self):
        self.set_rect()
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        rect = rotated_image.get_rect()
        rect.x = self.x
        rect.y = self.y
        screen.blit(rotated_image, rect)
