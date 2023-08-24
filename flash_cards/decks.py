import random
from collections import deque

from flash_cards.chance.go_to.back_tree_steps import GoBackThreeSteps
from flash_cards.chance.go_to.first_pink import GoToFirstPink
from flash_cards.chance.go_to.first_station import GoToFirstStation
from flash_cards.chance.go_to.go_to_prison import GoToPrison
from flash_cards.chance.go_to.go_to_red_last import GoToRedLast
from flash_cards.chance.go_to.last_purple import GoToLastPurple
from flash_cards.chance.go_to.nearest_station import GoToNearestStation
from flash_cards.chance.go_to.public_service import GoToPublicService
from flash_cards.chance.go_to.start import GoToStart
from flash_cards.chance.money_related.board_owner import BordOwnerPayment
from flash_cards.chance.money_related.date_of_payment import DateOfPaymentProfit
from flash_cards.chance.money_related.fine_for_fast_driving import FineForFastDriving
from flash_cards.chance.money_related.get_dividents import GetDividends
from flash_cards.chance.money_related.pay_for_building import PayForBuildings

from flash_cards.treasure.money_related.bank_mistake import BankMistake
from flash_cards.treasure.money_related.beauty_tax import BeautyTax
from flash_cards.treasure.money_related.birthday_profit import BirthdayProfit
from flash_cards.treasure.money_related.consulting_profit import ConsultingProfit
from flash_cards.treasure.money_related.doctor_payment import DoctorPayment
from flash_cards.treasure.money_related.heritage_profit import HeritageProfit
from flash_cards.treasure.money_related.hospital_payment import HospitalPayment
from flash_cards.treasure.money_related.life_insurance_profit import LifeInsuranceProfit
from flash_cards.treasure.money_related.pay_all_houses_and_hotels import PayAllHousesAndHotels
from flash_cards.treasure.money_related.school_fines import PaySchoolFines
from flash_cards.treasure.money_related.unpaid_taxes_profit import UnpaidTaxesProfit
from flash_cards.treasure.money_related.vacation_fond_profit import VacationFondProfit


class Holder:
    def __init__(self):
        self.cards = deque()
        self.current_card = None

    
    def get_card(self):
        current_card = self.cards.pop()
        self.make_shift(current_card)
        self.current_card = current_card
        return current_card
    def make_shift(self, current_card):
        self.cards.appendleft(current_card)
    
    

class ChanceHolder(Holder):
    def __init__(self):
        super().__init__()
        self.cards = deque([
            GoBackThreeSteps(),
            GoToFirstPink(),
            GoToFirstStation(),
            GoToPrison(),
            GoToRedLast(),
            GoToLastPurple(),
            GoToNearestStation(),
            GoToPublicService(),
            GoToStart(),
            BordOwnerPayment(),
            DateOfPaymentProfit(),
            FineForFastDriving(),
            GetDividends(),
            PayForBuildings()
        ])
        
        random.shuffle(self.cards)


class TreasureHolder(Holder):
    def __init__(self):
        super().__init__()
        self.cards = deque([
            BankMistake(),
            BeautyTax(),
            BirthdayProfit(),
            ConsultingProfit(),
            DoctorPayment(),
            HeritageProfit(),
            HospitalPayment(),
            LifeInsuranceProfit(),
            PayAllHousesAndHotels(),
            PaySchoolFines(),
            UnpaidTaxesProfit(),
            VacationFondProfit()
        ])

        random.shuffle(self.cards)