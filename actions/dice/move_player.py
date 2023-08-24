import pygame

from actions.base_action import Action
from events.custom_types import ON_BOX, ON_PLAYER_MOVEMENT


class MovePlayer(Action):
    def __init__(self, render, dices):
        super().__init__(render)
        self.current_player = self.render.current_player
        self.board = self.render.board
        self.board_index = None
        self.dices = dices
        self.on = False
        self.forward = True

    def execute(self):
        if self.on:
            if (not self.current_player.in_prison) or self.dices.dice_equal_sign():
                self.current_player.in_prison = False
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
                    self.forward = True
                    self.on = False
            else:
                self.current_player.prison_attempt_throw += 1
                if self.current_player.prison_attempt_throw == 3:
                    self.current_player.prison_attempt_throw = 0
                    self.current_player.in_prison = False


    def get_map_card(self):
        return self.board.sprites()[self.current_player.board_index]

    def get_nearest_place(self, rect_type):
        current_index = self.current_player.board_index
        for i in range(1, 41):
            new_index = current_index + 1
            new_index = self.end_index(new_index)
            if self.board.sprites()[new_index].side_image_type == rect_type:
                self.get_fixed_place(new_index)
                return

    def get_fixed_place(self, index):
        if self.current_player.board_index > index:
            index += 40
        self.dices.thrown = index
        pygame.event.post(pygame.event.Event(ON_PLAYER_MOVEMENT))

    def end_index(self, index):
        if index > 39:
            index -= 40
        elif index < 0:
            index += 40
        return index

    def check_end(self):
        return self.current_player.board_index == self.end_index(self.dices.thrown + self.board_index)

    def calculate_new_index(self):
        if self.forward:
            self.current_player.board_index += 1
        else:
            self.current_player.board_index -= 1

        self.current_player.board_index = self.end_index(self.current_player.board_index)

    def start(self):
        self.on = True
        self.board_index = self.current_player.board_index
