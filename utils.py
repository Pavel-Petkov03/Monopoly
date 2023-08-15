import pygame


class TextureMixin:

    @staticmethod
    def create_font(text, size, color):
        font = pygame.font.Font(None, int(size))
        text_surface = font.render(text, True, color)
        return text_surface

    def create_text_and_blit(self, surface, text_name, text_size, text_color, text_center):
        text_surface = self.create_font(text_name, text_size, text_color)
        text_rect = text_surface.get_rect(center=text_center)
        surface.blit(text_surface, text_rect)