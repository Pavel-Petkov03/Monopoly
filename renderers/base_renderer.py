from utils import SingletonClass


class Renderer:
    def __init__(self):
        self.textures = []
        self.cached = []

    def remove_texture(self, cache=False):
        data = self.textures.pop()
        if cache:
            self.cached.append(data)

    def add_texture(self, texture):
        self.textures.append(texture)

    def add_cached_texture(self):
        self.textures.append(self.cached.pop())