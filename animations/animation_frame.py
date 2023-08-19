import pygame

from actions.dice.move_player import MovePlayer
from events.custom_types import ON_PLAYER_MOVEMENT, ON_BOX


class AnimationFrame:
    def __init__(self, delay):
        self.__start = None
        self.__end = None
        self.__animation_on = False
        self.delay = delay

    def execute(self):
        if self.__animation_on:
            if self.__start <= self.__end:
                self.__start = pygame.time.get_ticks()
                self.on_animation_func()
            else:
                self.clean_up_function()
                self.__animation_on = False

    def start(self):
        self.__start = pygame.time.get_ticks()
        self.__end = self.__start + self.delay
        self.__animation_on = True

    def clean_up_function(self):
        pass

    def on_animation_func(self):
        pass


class DiceAnimationFrame(AnimationFrame):
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
        pygame.event.post(pygame.event.Event(ON_PLAYER_MOVEMENT))


class PlayerMovementAnimationFrame(AnimationFrame):
    def __init__(self, delay, renderer, dices):
        super().__init__(delay)

        self.on_animation_class = MovePlayer(renderer, dices)

    def on_animation_func(self, **kwargs):
        self.on_animation_class.execute()

    def clean_up_function(self, **kwargs):
        pygame.event.post(pygame.event.Event(ON_BOX))
