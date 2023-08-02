from sprites.map_cards_types import CornerMapCard, GenericMapCard, SideImageMapCard, screen_width, screen_height
from vars import border_data


class NeighborHood:
    def __init__(self, map_cards):
        self.map_cards = map_cards


class Board:
    def __init__(self):
        self.board = [
            CornerMapCard(
                screen_width - screen_width / 6,
                screen_height - screen_height / 6,
                "images/parking.png"
            ),
            GenericMapCard(
                screen_width - screen_width / 6 - screen_width / 12,
                screen_height - screen_height / 6,
                "brown",
                "Something",
                "123"
            ),
            SideImageMapCard(
                screen_width - screen_width / 6 - 2 * screen_width / 12,
                screen_height - screen_height / 6,
                "Something",
                "images/treasure.png",
                "123"
            ),
            GenericMapCard(
                screen_width - screen_width / 6 - 3 * screen_width / 12,
                screen_height - screen_height / 6,
                "brown",
                "Something",
                "123"
            ),
            SideImageMapCard(
                screen_width - screen_width / 6 - 4 * screen_width / 12,
                screen_height - screen_height / 6,
                "Something",
                "images/a.jpg",
                "123"
            ),
            GenericMapCard(
                screen_width - screen_width / 6 - 5 * screen_width / 12,
                screen_height - screen_height / 6,
                "blue",
                "Something",
                "123"
            ),
            SideImageMapCard(
                screen_width - screen_width / 6 - 4 * screen_width / 12,
                screen_height - screen_height / 6,
                "Something",
                "images/parking.png",
                "123"
            ),
        ]


    def initialise_board(self):
        for entry in border_data:
            rect_type = entry["rect_type"]
            rect_class = self.get_rect_class(rect_type)


     @staticmethod
    def get_rect_class(rect_type):
        data_classes = {
            "side_image" : SideImageMapCard,
            "corner" : CornerMapCard,
            "generic" : GenericMapCard
        }

        return data_classes[rect_type]
    def display(self):
        for c in self.board:
            c.blit()
