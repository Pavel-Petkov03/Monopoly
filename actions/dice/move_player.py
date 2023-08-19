import pygame

from actions.base_action import Action
from events.custom_types import ON_BOX, ON_PLAYER_MOVEMENT


class MovePlayer(Action):
    def __init__(self, render, dices):
        super().__init__(render)
        self.current_player = self.render.current_player
        self.board = self.render.board
        self.board_index = self.current_player.board_index
        self.dices = dices

    def execute(self):
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
            self.current_player.board_index = 0

    def remove_from_current_position(self):
        if self.end_index() != self.current_player.board_index:
            self.render.board.sprites()[self.current_player.board_index].players.pop(self.current_player)

    def blit_to_new_index(self):
        if self.end_index() != self.current_player.board_index:
            self.render.board.sprites()[self.current_player.board_index].players[
                self.current_player] = self.current_player.piece_image
