from events.base_event import Event
from events.custom_types import ON_BOX


class MapCardEvent(Event):


    @staticmethod
    def condition(event_type, texture):
        return event_type == ON_BOX

    @staticmethod
    def execute(texture):
        texture.new_player_on = True