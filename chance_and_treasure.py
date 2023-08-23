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


class GoToStart(ChanceCard):
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
        renderer.dices.move_player_animation.get_fixed_place(24)


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
        renderer.dices.move_player_animation.get_fixed_place(11)

class GoToFirstStation(ChanceCard):
    def __init__(self):
        super().__init__("ПРОДЪЛЖЕТЕ ДО ГАРА СОФИЯ\n"
                         "АКО ПРЕМИНЕТЕ ПРЕЗ НАЧАЛОТО ПОЛУЧАВАТЕ 200"
                         )

    def exec(self, renderer: BoardRenderer):
        renderer.dices.move_player_animation.get_fixed_place(5)

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


class GoBackThreeSteps(ChanceCard):
    def __init__(self):
        super().__init__("ВЪРНЕТЕ СЕ ТРИ МЕСТА НАЗАД")

    def exec(self, renderer: BoardRenderer):
        index_to_go = renderer.current_player.board_index - 3
        renderer.dices.move_player_animation.forward = False
        renderer.dices.move_player_animation.get_fixed_place(index_to_go)

class PayForBuildings(ChanceCard):
    def __init__(self):
        super().__init__("ОСНОВЕН РЕМОНТ НА ВСИЧКИТЕ ВИ СГРАДИ\n"
                         "ЗА ВСЯКА КЪЩА ПЛАТЕТЕ ПО 25\n"
                         "ЗА ВСЕКИ ХОТЕЛ ПЛАТЕТЕ ПО 100"
                         )

    def exec(self, renderer: BoardRenderer):
        accumulated_price = 0
        for sprite in renderer.board.sprites():
            if sprite.rect_type == "generic" and  sprite.owner == renderer.current_player:
                if sprite.houses == 5:
                    accumulated_price += 100
                else:
                    accumulated_price += 25 * sprite.houses
        renderer.current_player -= accumulated_price


class GoToPrison(ChanceCard):
    def __init__(self):
        super().__init__("ОТИВАТЕ ДИРЕКТНО В ЗАТВОРА.НЕ ПРЕМИНАВАТЕ ПРЕЗ НАЧАЛО И НЕ ПОЛУЧАВАТЕ 200")

    def exec(self, renderer: BoardRenderer):
        renderer.dices.move_player_animation.forward = False
        renderer.current_player.in_prison = True
        renderer.dices.move_player_animation.get_fixed_place(10)


class PaySchoolFines(TreasureCard):
    def __init__(self):
        super().__init__("ПЛАТЕТЕ УЧИЛИЩНИ ТАКСИ 50")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money -= 50


class SellShare(TreasureCard):
    def __init__(self):
        super().__init__("ПРОДАВАТЕ АКЦИИ И ПОЛУЧАВАТЕ 50")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 50

class BeautyTax(TreasureCard):
    def __init__(self):
        super().__init__("ПЕЧЕЛИТЕ КОНКУРС ПО КРАСОТА И ПОЛУЧАВАТЕ 10")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 10


class ConsultingProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПОЛУЧАВАТЕ ХОНОРОР ЗА КОНСУЛТАНТ 25")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 25

class BankMistake(TreasureCard):
    def __init__(self):
        super().__init__("БАНКОВА ГРЕШКА ВЪВ ВАША ПОЛЗА ПОЛУЧАВАТЕ 200")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 200


class HeritageProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПОЛУЧАВАТЕ НАСЛЕДСТВО ОТ 100")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 100


class HospitalPayment(TreasureCard):
    def __init__(self):
        super().__init__("ПЛАТЕТЕ 100 ЗА БОЛНИЧНИ ТАКСИ")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money -= 100



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


class BirthdayProfit(TreasureCard):
    def __init__(self):
        super().__init__("ИМАТЕ РОЖДЕН ДЕН. ПОЛУЧАВАТЕ ПО 10 ОТ ВСЕКИ ИГРАЧ")

    def exec(self, renderer: BoardRenderer):
        for player in renderer.players:
            if player != renderer.current_player:
                renderer.current_player.money += 10
                player.money -= 10


class DoctorPayment(TreasureCard):
    def __init__(self):
        super().__init__("ТАКСА ЗА ЛЕКАР. ПЛАТЕТЕ 50")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money -= 50


class LifeInsuranceProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ЗАСТРАХОВКА ЖИВОТ. ПОЛУЧАВАТЕ 100")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 100


class UnpaidTaxesProfit(TreasureCard):
    def __init__(self):
        super().__init__("ВРЪЩАТ ВИ НАДПЛАТЕНИ ДАНЪЦИ ПОЛУЧАВАТЕ 20")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 20

class VacationFondProfit(TreasureCard):
    def __init__(self):
        super().__init__("ПАДЕЖ НА ВАКАНЦИОНЕН ФОНД ПОЛУЧАВАТЕ 100")

    def exec(self, renderer: BoardRenderer):
        renderer.current_player.money += 100

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
