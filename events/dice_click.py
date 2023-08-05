import pygame

from events.base_event import Event


class DiceClickEvent(Event):
    @staticmethod
    def condition(event_type, texture):
        for dice in texture.dices:
            if event_type == pygame.MOUSEBUTTONDOWN and not texture.on_display and dice.rect.collidepoint(
                    *pygame.mouse.get_pos()):
                return True
        return False

    @staticmethod
    def execute(texture):
        texture.on_click()
