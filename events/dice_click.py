import pygame

from events.base_event import Event


class DiceClickEvent(Event):
    @staticmethod
    def condition(event_type, texture):
        return event_type == pygame.MOUSEBUTTONDOWN and not texture.on_display and texture.rect.collidepoint(
            *pygame.mouse.get_pos())
    @staticmethod
    def execute(texture):
        texture.on_click()