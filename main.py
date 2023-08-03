import pygame
from sprites.board import Board
from vars import screen, screen_rect_size





class Game:
    def __init__(self):
        pygame.init()
        self.board = Board()
        self.board.initialise_board()


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.set_background()
            self.board.display()
            pygame.display.update()

    @staticmethod
    def set_background():
        image = pygame.image.load("images/board/background.jpg").convert_alpha()
        image = pygame.transform.scale(image, (screen_rect_size, screen_rect_size)).convert_alpha()
        screen.blit(image, (0, 0))


game = Game()
game.run()
