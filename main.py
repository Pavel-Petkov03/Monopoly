import pygame
from sprites.board import Board, SideImageMapCard
from vars import screen, screen_height, screen_width

pygame.init()

b = Board()


class Game:
    def __init__(self):
        pass

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.set_background()
            b.display()
            pygame.display.update()

    @staticmethod
    def set_background():
        image = pygame.image.load("images/background.jpg").convert_alpha()
        image = pygame.transform.scale(image, (screen_width, screen_height)).convert_alpha()
        screen.blit(image, (0, 0))


game = Game()
game.run()
