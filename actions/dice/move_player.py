import pygame

from actions.base_action import Action
from animations.animation_frame import AnimationFrame
from events.custom_types import ON_BOX, ON_PLAYER_MOVEMENT


class MovePlayerAnimationFrame(AnimationFrame):
    def __init__(self, delay, renderer, dices):
        super().__init__(delay)
        self.on = False
        self.forward = True
        self.renderer = renderer
        self.board_index = None
        self.current_player = None
        self.dices = dices
        self.board = self.renderer.board


    def clean_up_function(self):
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

        movement_sound = pygame.mixer.Sound("sounds/movement_sound.mp3")
        pygame.mixer.Sound.play(movement_sound)
        super().start()


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

    def execute(self):
        if self.on:
            super().execute()

    def start(self):
        super().start()
        self.on = True
        self.current_player = self.renderer.current_player
        self.board_index = self.current_player.board_index

    def get_map_card(self):
        return self.board.sprites()[self.current_player.board_index]


class MovePlayer(Action):
    def __init__(self, renderer, dices):
        super().__init__(renderer)
        self.board = self.renderer.board
        self.dices = dices
        self.current_player = None
        self.animation_frame = MovePlayerAnimationFrame(250, renderer, dices)

    def execute(self):
        self.animation_frame.execute()

    def get_nearest_place(self, rect_type):
        current_index = self.current_player.board_index
        for i in range(1, 41):
            new_index = current_index + i
            new_index = self.end_index(new_index)
            if self.board.sprites()[new_index].side_image_type == rect_type:
                self.get_fixed_place(new_index)
                return

    def get_fixed_place(self, index):
        if self.current_player.board_index > index:
            index += 40 - self.current_player.board_index
        else:
            index -= self.current_player.board_index
        self.dices.thrown = index
        pygame.event.post(pygame.event.Event(ON_PLAYER_MOVEMENT))

    def end_index(self, index):
        if index > 39:
            index -= 40
        elif index < 0:
            index += 40
        return index

    def start(self):
        self.animation_frame.start()
        self.current_player = self.renderer.current_player
