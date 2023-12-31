import functools

import pygame
from events.custom_types import ON_PLAYER_MOVEMENT


class AnimationFrame:
    def __init__(self, delay):
        self.__start = None
        self.__end = None
        self.animation_on = False
        self.delay = delay

    def execute(self):
        if self.animation_on:
            if self.__start <= self.__end:
                self.__start = pygame.time.get_ticks()
                self.on_animation_func()
            else:
                self.animation_on = False
                self.clean_up_function()

    def start(self):
        self.__start = pygame.time.get_ticks()
        self.__end = self.__start + self.delay
        self.animation_on = True

    def clean_up_function(self):
        pass

    def on_animation_func(self):
        pass


class DiceAnimationFrameBase(AnimationFrame):
    def __init__(self, delay, dices_object):
        super().__init__(delay)
        self.dices_object = dices_object

    def on_animation_func(self):
        for dice in self.dices_object.dices:
            dice.on_animation()

    def clean_up_function(self):
        thrown = 0
        for dice in self.dices_object.dices:
            thrown += dice.calculate_num()
        self.dices_object.thrown = thrown
        self.add_additional_cleanup()

    def add_additional_cleanup(self):
        pass

    def start(self):
        super().start()
        dice_rolling_sound = pygame.mixer.Sound("sounds/dice_rolling_sound.mp3")
        pygame.mixer.Sound.play(dice_rolling_sound)


class DiceAnimationFrameMovement(DiceAnimationFrameBase):
    def add_additional_cleanup(self):
        pygame.event.post(pygame.event.Event(ON_PLAYER_MOVEMENT))


class DiceAnimationFramePublicServices(DiceAnimationFrameBase):
    def add_additional_cleanup(self):
        thrown = self.dices_object.thrown
        renderer = self.dices_object.renderer
        board = renderer.board
        current_player = renderer.current_player
        current_side_image = board.sprites()[current_player.board_index]
        if current_side_image.side_image_pack.all_neighborhood():
            mul = 10
        else:
            mul = 4
        current_player.money -= mul * thrown