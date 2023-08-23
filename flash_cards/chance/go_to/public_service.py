from flash_cards.chance.base import ChanceCard


class GoToPublicService(ChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО НАЙ - БЛИЗКАТА КОМПАНИЯ.\n"
                         "AКО НЕ Е КУПЕНА МОЖЕ ДА Я КУПИТЕ ОТ БАНКАТАA\n"
                         "AKO E КУПЕНА , ХВЪРЛЕТЕ ЗАРОВЕТЕ И ПЛАТЕТЕ НА СОБСТВЕНИКА НАЕМ, РАВЕН НА СБОРА ОТ ЗАРОВЕТЕ УМНОЖЕН ПО ДЕСЕТ"
                         )

    def exec(self, renderer):
        renderer.dices.move_player_animation.get_nearest_place("public_services")