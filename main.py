import pygame
from renderers.board_render import BoardRender
from vars import screen, screen_rect_size


class Game:
    def __init__(self):
        self.render = BoardRender([])
        pygame.init()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for texture in self.render.textures:
                    texture.exec_events(event_type=event.type)

            self.set_background()
            for texture in self.render.textures:
                texture.blit(screen)
                texture.update()
            pygame.display.update()

    @staticmethod
    def set_background():
        image = pygame.image.load("images/board/background.jpg").convert_alpha()
        image = pygame.transform.scale(image, (screen_rect_size, screen_rect_size)).convert_alpha()
        screen.blit(image, (0, 0))


game = Game()
game.run()
