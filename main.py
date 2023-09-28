import pygame
from renderers.board_render import BoardRenderer
from timer import Timer
from vars import screen, screen_rect_size


class Game:
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.renderer = BoardRenderer([])


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for texture in self.renderer.textures:
                    texture.exec_events(event_type=event.type)
            self.renderer.blit(screen)
            pygame.display.flip()
            self.timer.set_fps()
            pygame.display.set_caption(f"Monopoly fps:{self.timer.get_fps()}")


if __name__ == "__main__":
    game = Game()
    game.run()