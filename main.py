import pygame
from sprites.board import Board
from sprites.dice import Dice
from vars import screen, screen_rect_size


class Game:
    def __init__(self):
        pygame.init()
        self.board = Board()
        self.board.initialise_board()
        self.d = Dice(screen_rect_size / 2, screen_rect_size / 2)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.d.on_display and self.d.rect.collidepoint(*pygame.mouse.get_pos()):
                    self.d.on_display = True
                    self.d.start = pygame.time.get_ticks()
                    self.d.end = pygame.time.get_ticks() + 1000
            self.set_background()
            self.board.display()
            self.d.blit(screen)
            self.d.update()
            pygame.display.update()

    @staticmethod
    def set_background():
        image = pygame.image.load("images/board/background.jpg").convert_alpha()
        image = pygame.transform.scale(image, (screen_rect_size, screen_rect_size)).convert_alpha()
        screen.blit(image, (0, 0))


game = Game()
game.run()
