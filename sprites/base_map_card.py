import pygame
from vars import screen, screen_height, screen_width


class BaseMapCard(pygame.sprite.Sprite):
    def __init__(self, x, y, rect_type, color=None, caption=None, inside_image_path=None, price=None):
        super().__init__()
        self.width = None
        self.height = None
        self.image = None
        self.x = x
        self.y = y
        self.rect_type = rect_type
        self.inside_image_path = inside_image_path
        self.caption = caption
        self.color = color
        self.price = price

    def set_rect(self):
        width_and_height_dict = {
            "generic": (screen_width / 12, screen_height / 6),
            "corner": (screen_width / 6, screen_height / 6),
            "side_image": (screen_width / 12, screen_height / 6)
        }
        self.width = width_and_height_dict[self.rect_type][0]
        self.height = width_and_height_dict[self.rect_type][1]
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("white")
        pygame.draw.rect(self.image, "black", self.image.get_rect(), 1)
        self.add_additional_data()

    def add_additional_data(self):
        if self.rect_type == "generic":
            inner_rect = pygame.Rect(0, 0, self.width, self.height / 4)
            pygame.draw.rect(self.image, self.color, inner_rect)
            self.set_caption(self.caption, self.width / 4, self.width / 2, self.height / 3)
            self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)
        elif self.rect_type == "corner":
            self.image_load(0)
        elif self.rect_type == "side_image":
            self.image_load(30)
            self.set_caption(self.caption, self.width / 4, self.width / 2, self.height / 6)
            if self.price:
                self.set_caption(f"${self.price}", self.width / 6, self.width / 2, self.height * 7 / 8)

    def image_load(self , padding_percent):
        padding_top = int(self.height * (padding_percent / 100))
        padding_bottom = int(self.height * (padding_percent / 100))
        new_height = self.height - padding_top - padding_bottom
        inside_image = pygame.image.load(self.inside_image_path).convert_alpha()
        scale_factor = new_height / inside_image.get_height()
        new_width = int(inside_image.get_width() * scale_factor)
        scaled_image = pygame.transform.scale(inside_image, (new_width, new_height)).convert_alpha()
        x_offset = (self.width - new_width) // 2
        self.image.blit(scaled_image, (x_offset,padding_top))

    def set_caption(self, text, size, width, height):
        words = text.split(" ")
        padding = self.width / 4
        padding_counter = 0
        for word in words:
            font = pygame.font.Font(None, int(size))
            text_surface = font.render(word, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(width, height + padding_counter))
            padding_counter += padding
            self.image.blit(text_surface, text_rect)

    def blit(self):
        self.set_rect()
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        screen.blit(self.image, rect)

