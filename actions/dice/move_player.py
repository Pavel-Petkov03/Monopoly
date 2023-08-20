import pygame

from actions.base_action import Action
from events.custom_types import ON_BOX


class MovePlayer(Action):
    def __init__(self, render, dices):
        super().__init__(render)
        self.current_player = self.render.current_player
        self.board = self.render.board
        self.board_index = None
        self.dices = dices
        self.on = False

    def execute(self):
        if self.on:
            current_board_map_card = self.board.sprites()[self.current_player.board_index]
            if self.board_index == self.current_player.board_index:
                current_board_map_card.remove_player_from_all_players(self.current_player)
            elif self.end_index() == self.current_player.board_index:
                pygame.event.post(pygame.event.Event(ON_BOX))
                current_board_map_card.add_player_to_all_players()
                self.on = False

            current_board_map_card
            self.remove_from_current_position()
            self.calculate_new_index()
            self.blit_to_new_index()


    def end_index(self):
        new_index = self.dices.thrown + self.board_index
        if new_index >= 39:
            new_index -= 39
        return new_index

    def check_end(self):
        return self.current_player.board_index == self.end_index()

    def calculate_new_index(self):
        self.current_player.board_index += 1
        if self.current_player.board_index >= 39:
            self.current_player.board_index -= 39

    def remove_from_current_position(self):
        self.render.board.sprites()[self.current_player.board_index].players.pop(self.current_player)

    def blit_to_new_index(self):
        self.render.board.sprites()[self.current_player.board_index].players[
            self.current_player] = self.current_player.piece_image

    def start(self):
        self.on = True
        self.board_index = self.current_player.board_index
