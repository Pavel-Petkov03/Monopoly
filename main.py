import pygame
from renderers.board_render import BoardRenderer
from timer import Timer
from vars import screen, screen_rect_size


class Game:
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.renderer = BoardRenderer([])
        self.image = pygame.image.load("images/board/background.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_rect_size, screen_rect_size)).convert_alpha()

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
            pygame.display.flip()
            self.timer.set_fps()
            pygame.display.set_caption(f"Monopoly fps:{self.timer.get_fps()}")


if __name__ == "__main__":
    game = Game()
    game.run()
