import pygame


class Texture(pygame.sprite.Sprite):
    def blit(self, window):
        pass

    def update(self, *args, **kwargs) -> None:
        pass


class TextureGroup(pygame.sprite.Group):
    def blit(self, window):
        for sprite in self.sprites():
            sprite.blit(window)

    def update(self, ) -> None:
        for sprite in self.sprites():
            sprite.update()
