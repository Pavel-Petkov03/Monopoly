from sprites.map_cards_types import CornerMapCard, GenericMapCard, SideImageMapCard, screen_width, screen_height
from vars import border_data


class NeighborHood:
    def __init__(self, map_cards):
        self.map_cards = map_cards


class Board:
    def __init__(self):
        self.board = [

        ]

    def initialise_board(self):
        previous_rects_width = 0
        previous_rects_height = screen_height/6
        direction = "left"
        for entry in border_data:
            rect_type = entry.pop("rect_type")
            rect_class = self.get_rect_class(rect_type)
            previous_rects_width += rect_class.width
            x = screen_width - previous_rects_width
            y = screen_height - previous_rects_height
            obj = rect_class(x, y, **entry)
            self.board.append(obj)

    @staticmethod
    def get_rect_class(rect_type):
        data_classes = {
            "side_image": SideImageMapCard,
            "corner": CornerMapCard,
            "generic": GenericMapCard
        }

        return data_classes[rect_type]

    def display(self):
        for c in self.board:
            c.blit()
