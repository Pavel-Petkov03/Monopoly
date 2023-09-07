
from flash_cards.chance.money_related.base import MoneyRelatedChanceCard


class PayForBuildings(MoneyRelatedChanceCard):
    def __init__(self):
        super().__init__("ОСНОВЕН РЕМОНТ НА ВСИЧКИТЕ ВИ СГРАДИ\n"
                         "ЗА ВСЯКА КЪЩА ПЛАТЕТЕ ПО 25\n"
                         "ЗА ВСЕКИ ХОТЕЛ ПЛАТЕТЕ ПО 100"
                         )

    def exec(self, renderer):
        accumulated_price = 0
        for sprite in renderer.board.sprites():
            if sprite.rect_type == "generic" and  sprite.owner == renderer.current_player:
                if sprite.houses == 5:
                    accumulated_price += 100
                else:
                    accumulated_price += 25 * sprite.houses
        renderer.current_player.money -= accumulated_price