from collections import deque

import pygame.event

from events.custom_types import ON_PLAYER_MOVEMENT
from renderers.board_render import BoardRenderer


class Card:
    def __init__(self, header_message):
        self.header_message = header_message

    def exec(self, renderer: BoardRenderer):
        pass
    


class TreasureCard(Card):
    pass


class ChanceCard(Card):
    pass


class GoToStartChanceCard(ChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО НАЧАЛО И (ПОЛУЧАВАТЕ 200)")

    def exec(self, renderer):
        renderer.dices.move_player_animation.get_fixed_place(0)


class GoToPublicService(ChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО НАЙ - БЛИЗКАТА КОМПАНИЯ.\n"
                         "AКО НЕ Е КУПЕНА МОЖЕ ДА Я КУПИТЕ ОТ БАНКАТАA\n"
                         "AKO E КУПЕНА , ХВЪРЛЕТЕ ЗАРОВЕТЕ И ПЛАТЕТЕ НА СОБСТВЕНИКА НАЕМ, РАВЕН НА СБОРА ОТ ЗАРОВЕТЕ УМНОЖЕН ПО ДЕСЕТ"
                         )

    def exec(self, renderer):
        renderer.dices.move_player_animation.get_nearest_place("public_services")


class GoToNearestStation(ChanceCard):
    def __init__(self):
        super().__init__(
            "ПРОДЪЛЖЕТЕ ДО НАЙ - БЛИЗКАТА ГАРА\n"
            "АКО НЕ Е КУПЕНА МОЖЕ ДА Я КУПИТE\n"
            "АКО НЕ Е КУПЕНА ПЛАТЕТЕ СЪОВЕТНАТА ЦЕНА НА СОБСТВЕНИКА"
        )

    def exec(self, renderer: BoardRenderer):
        renderer.dices.move_player_animation.get_nearest_place("station")


class GetDividends(ChanceCard):
    def __init__(self):
        super().__init__("БАНКАТА ВИ ИЗПЛАЩА ДИВИДЕНТ ОТ 50")

    def exec(self, renderer: BoardRenderer):
        money_to_get = 50
        current_player = renderer.current_player
        current_player.money += money_to_get


class GoToRedLast(ChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО УЧЛИЦА ОБОРИЩЕ\n"
                         "АКО ПРЕМИНЕТЕ ПРЕЗ НАЧАЛОТО ПОЛУЧАВАТЕ 200"
                         )

    def exec(self, renderer: BoardRenderer):
        renderer.dices.move_player_animation.get_fixed_place(2)


class FineForFastDriving(ChanceCard):
    def __init__(self):
        super().__init__("ГЛОБА ЗА ПРЕВИШЕНА СКОРОСТ 15")

    def exec(self, renderer: BoardRenderer):
        money_to_pay = 15
        current_player = renderer.current_player
        current_player.money -= money_to_pay

class GoToFirstPink(ChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО ПЛОЩАД МАКЕДОНИЯ\n"
                         "АКО ПРЕМИНЕТЕ ПРЕЗ НАЧАЛОТО ПОЛУЧАВАТЕ 200"
                         )

    def exec(self, renderer: BoardRenderer):
        renderer.dices.move_player_animation.get_fixed_place(2)

class GoToFirstStation(ChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО ГАРА СОФИЯ\n"
                         "АКО ПРЕМИНЕТЕ ПРЕЗ НАЧАЛОТО ПОЛУЧАВАТЕ 200"
                         )

    def exec(self, renderer: BoardRenderer):
        renderer.dices.move_player_animation.get_fixed_place(4)

class DateOfPaymentProfit(ChanceCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ЗАЕМА ВИ ЗА ИМОТ\n"
                         "ПОЛУЧАВАТЕ 150")
    
    def exec(self, renderer: BoardRenderer):
        money_to_pay = 150
        current_player = renderer.current_player
        current_player.money -= money_to_pay


class BordOwner(ChanceCard):
    def __init__(self):
        super().__init__("ИЗБРАН СТЕ ЗА ПРЕДСТЕДАТЕЛ НА БОРДА ПЛАТЕТЕ НА ВСЕКИ ИГРАЧ ПО 50")

    def exec(self, renderer: BoardRenderer):
        all_players = renderer.players
        for player in all_players:
            if player != renderer.current_player:
                renderer.current_player.money -= 50
                player.money += 50

class GoToLastPurple(ChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО БОЯНА")

    def exec(self, renderer: BoardRenderer):
        renderer.dices.move_player_animation.get_fixed_place(39)






treasure_cards = [

]

chance_cards = [

]


class Holder:
    def __init__(self):
        self.cards = deque()


class TreasureHolder(Holder):
    pass


class ChanceHolder(Holder):
    pass
