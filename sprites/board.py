from sprites.map_cards_types import CornerMapCard, GenericMapCard, SideImageMapCard, screen_width, screen_height


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

    def display(self):
        for c in self.board:
            c.blit()
