import pygame

from events.base_event import Event
from events.custom_types import ON_PLAYER_MOVEMENT


class DiceClickEvent(Event):
    @staticmethod
    def condition(event_type, texture):
        for dice in texture.dices:
            if event_type == pygame.MOUSEBUTTONDOWN and dice.rect.collidepoint(
                    *pygame.mouse.get_pos()):
                return True
        return False

    @staticmethod
    def execute(texture):
        texture.dice_animation_frame.start()


class PlayerMovementEvent(Event):

    @staticmethod
    def condition(event_type, texture):
        return event_type == ON_PLAYER_MOVEMENT

    @staticmethod
    def execute(texture):
        texture.move_player_animation.start()
