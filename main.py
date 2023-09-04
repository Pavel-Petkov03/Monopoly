import pygame
from renderers.board_render import BoardRenderer
from vars import screen, screen_rect_size


class Game:
    def __init__(self):
        self.renderer = BoardRenderer([])
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("images/board/background.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_rect_size, screen_rect_size)).convert_alpha()
        self.fps = 60
        pygame.init()

    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for texture in self.renderer.textures:
                    texture.exec_events(event_type=event.type)

            screen.blit(self.image, (0, 0))
            for texture in self.renderer.textures:
                texture.blit(screen)
                texture.update()
            pygame.display.update()
            self.clock.tick(self.fps)
            pygame.display.set_caption(f"Monopoly fps:{self.clock.get_fps()}")


game = Game()
game.run()
