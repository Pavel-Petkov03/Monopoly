from sprites.map_cards_types import CornerMapCard, GenericMapCard, SideImageMapCard
from sprites.texture import TextureGroup
from vars import border_data, screen_rect_size


class Board(TextureGroup):
    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer
        self.initialise_board()

    def initialise_board(self):
        previous_rects_width = 0
        previous_rects_height = 0
        counter = 0
        rotation_degrees = 0
        street_index = 0
        house_price = 50
        for entry in border_data:
            x, y = 0, 0
            rect_type = entry["rect_type"]
            entry["rotation"] = rotation_degrees
            entry["house_price"] = house_price
            rect_class = self.get_rect_class(rect_type)
            if street_index == 0:
                previous_rects_width += rect_class.width
                x = screen_rect_size - previous_rects_width
                y = screen_rect_size - screen_rect_size / 16 * 2
            elif street_index == 1:
                previous_rects_height += rect_class.width
                x = 0
                y = screen_rect_size - previous_rects_height
            elif street_index == 2:
                x = previous_rects_width
                y = 0
                previous_rects_width += rect_class.width
            elif street_index == 3:
                x = screen_rect_size - previous_rects_width
                y = previous_rects_height
                previous_rects_height += rect_class.width
            obj = rect_class(x, y, self.renderer,  **entry)
            self.add([obj])

            if counter == 10:
                previous_rects_width = rect_class.width
                previous_rects_height = rect_class.height
                street_index += 1
                rotation_degrees, house_price = self.street_data(street_index)
                counter = 0
            counter += 1

    def blit_player_to_generic_map_card(self, current_player):
        self.sprites()[current_player.board_index].players[current_player] = current_player.piece_image

    def remove_player_from_current_position(self, current_player):
        self.sprites()[current_player.board_index].players.pop(current_player)

    def street_data(self, street_index):
        rot = {
            1: 270,
            2: 180,
            3: 90
        }
        house_price = street_index * 50
        return rot[street_index], house_price

    @staticmethod
    def get_rect_class(rect_type):
        data_classes = {
            "side_image": SideImageMapCard,
            "corner": CornerMapCard,
            "generic": GenericMapCard
        }

        return data_classes[rect_type]
