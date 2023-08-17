class Renderer:
    def __init__(self):
        self.textures = []

    def remove_texture(self):
        self.textures.pop()

    def add_texture(self, texture):
        self.textures.append(texture)