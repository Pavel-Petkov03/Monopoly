from sprites.map_cards_types import CornerMapCard, GenericMapCard, SideImageMapCard
from sprites.texture import TextureGroup
from vars import border_data, screen_rect_size


class Board(TextureGroup):
    def __init__(self):
        super().__init__([])
        self.initialise_board()

    def initialise_board(self):
        previous_rects_width = 0
        previous_rects_height = 0
        counter = 0
        rotation_degrees = 0
        direction = "left"
        for entry in border_data:
            x, y = 0, 0
            rect_type = entry.pop("rect_type")
            entry["rotation"] = rotation_degrees
            rect_class = self.get_rect_class(rect_type)
            if direction == "left":
                previous_rects_width += rect_class.width
                x = screen_rect_size - previous_rects_width
                y = screen_rect_size - screen_rect_size / 16 * 2
            elif direction == "up":
                previous_rects_height += rect_class.width
                x = 0
                y = screen_rect_size - previous_rects_height
            elif direction == "right":
                x = previous_rects_width
                y = 0
                previous_rects_width += rect_class.width
            elif direction == "bottom":
                x = screen_rect_size - previous_rects_width
                y = previous_rects_height
                previous_rects_height += rect_class.width
            obj = rect_class(x, y, **entry)
            self.add([obj])

            if counter == 10:
                previous_rects_width = rect_class.width
                previous_rects_height = rect_class.height
                direction, rotation_degrees = self.get_direction(direction)
                counter = 0
            counter += 1

    def get_direction(self, direction):
        ds = {
            "left": "up",
            "up": "right",
            "right": "bottom"
        }
        rot = {
            "left": 270,
            "up": 180,
            "right": 90
        }
        return ds[direction], rot[direction]

    @staticmethod
    def get_rect_class(rect_type):
        data_classes = {
            "side_image": SideImageMapCard,
            "corner": CornerMapCard,
            "generic": GenericMapCard
        }

        return data_classes[rect_type]

