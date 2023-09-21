import pygame


class SingletonClass:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


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

    def word_splitter(self, text: str):
        words = text.split(" ")
        f = []
        s = ""
        i = 0
        for word in words:
            i += 1
            s += f" {word}"
            if i == 6 or len(s) >= 20:
                f.append(s)
                s = ""
                i = 0
        if s:
            f.append(s)
        return f
