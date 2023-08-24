from collections import deque

from renderers.board_render import BoardRenderer


class Card:
    def __init__(self, header_message):
        self.header_message = header_message

    def exec(self, renderer: BoardRenderer):
        pass



