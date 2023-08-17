from events.base_event import Event
import pygame


class ButtonHoverEvent(Event):

    @staticmethod
    def condition(event_type, texture):
        texture.is_hovered = texture.rect.collidepoint(*pygame.mouse.get_pos())
        return False


class ButtonClickEvent(Event):
    @staticmethod
    def condition(event_type, texture):
        return event_type == pygame.MOUSEBUTTONDOWN and texture.rect.collidepoint(*pygame.mouse.get_pos())

    @staticmethod
    def execute(texture):
        texture.activate_action()
