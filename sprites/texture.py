import pygame

from utils import TextureMixin


class Texture(pygame.sprite.Sprite, TextureMixin):
    def __init__(self):

        super().__init__()
        self.event_list = []
        self.update_kwargs = {}

    def blit(self, window):
        pass

    def update(self, *args, **kwargs) -> None:
        pass

    def exec_events(self, event_type=None):
        for event in self.event_list:
            if event.condition(event_type, self):
                event.execute(self)


class TextureGroup(pygame.sprite.Group, TextureMixin):
    def __init__(self):
        super().__init__()
        self.update_kwargs = {}

    def blit(self, window):
        for sprite in self.sprites():
            sprite.blit(window)

    def update(self, *args, **kwargs) -> None:
        for sprite in self.sprites():
            sprite.update(*args, **kwargs)

    def exec_events(self, event_type=None):
        for sprite in self.sprites():
            sprite.exec_events(event_type)
