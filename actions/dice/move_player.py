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
            current_board_map_card = self.get_map_card()
            if self.board_index == self.current_player.board_index:
                current_board_map_card.remove_player_from_all_players(self.current_player)
                current_board_map_card.add_player_to_temporary(self.current_player)

            current_board_map_card.remove_player_from_temporary(self.current_player)
            self.calculate_new_index()
            current_board_map_card = self.get_map_card()
            current_board_map_card.add_player_to_temporary(self.current_player)
            if self.check_end():
                pygame.event.post(pygame.event.Event(ON_BOX))
                current_board_map_card.add_player_to_all_players(self.current_player)
                current_board_map_card.remove_player_from_temporary(self.current_player)
                self.on = False


    def get_map_card(self):
        return self.board.sprites()[self.current_player.board_index]

    def end_index(self):
        new_index = self.dices.thrown + self.board_index
        if new_index > 39:
            new_index -= 40
        return new_index

    def check_end(self):
        return self.current_player.board_index == self.end_index()

    def calculate_new_index(self):
        self.current_player.board_index += 1
        if self.current_player.board_index > 39:
            self.current_player.board_index -= 40


    def start(self):
        self.on = True
        self.board_index = self.current_player.board_index
