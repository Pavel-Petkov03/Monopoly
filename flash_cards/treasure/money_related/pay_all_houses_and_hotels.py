from flash_cards.treasure.base import TreasureCard
from renderers.board_render import BoardRenderer


class PayAllHousesAndHotels(TreasureCard):
    def __init__(self):
        super().__init__("ПЛАЩАТЕ ЗА РЕМОНТ НА УЛИЦИ. 40 ЗА ВСЯКА КЪЩА. 115 ЗА ВСЕКИ ХОТЕЛ")

    def exec(self, renderer: BoardRenderer):
        accumulated_price = 0
        for sprite in renderer.board.sprites():
            if sprite.rect_type == "generic":
                if sprite.houses == 5:
                    accumulated_price += 115
                else:
                    accumulated_price += 40 * sprite.houses
