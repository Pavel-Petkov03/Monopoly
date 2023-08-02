from sprites.base_map_card import BaseMapCard, screen_width, screen_height


class GenericMapCard(BaseMapCard):
    def __init__(self, x, y, color, caption, price):
        super().__init__(x, y, "generic", color=color, caption=caption, price=price)


class CornerMapCard(BaseMapCard):
    def __init__(self, x, y, inside_image_path):
        super().__init__(x, y, "corner", inside_image_path=inside_image_path, )


class SideImageMapCard(BaseMapCard):
    def __init__(self, x, y, caption, inside_image_path, price):
        super().__init__(x, y, "side_image", caption=caption, inside_image_path=inside_image_path, price=price)
