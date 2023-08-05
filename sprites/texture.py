import pygame


class Texture(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.event_list = []

    def blit(self, window):
        pass

    def update(self, *args, **kwargs) -> None:
        pass

    def exec_events(self, event_type):
        for event in self.event_list:
            if event.condition(event_type, self):
                event.execute(self)


class TextureGroup(pygame.sprite.Group):
    def blit(self, window):
        for sprite in self.sprites():
            sprite.blit(window)

    def update(self, ) -> None:
        for sprite in self.sprites():
            sprite.update()

    def exec_events(self, event_type):
        for sprite in self.sprites():
            sprite.exec_events(event_type)
