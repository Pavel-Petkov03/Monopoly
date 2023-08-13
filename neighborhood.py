class Neighborhood:
    def __init__(self, _id, count):
        self.id = _id
        self.count = count
        self.generic_map_cards = []

    def add_generic_map_cards(self, generic_map_card):
        self.generic_map_cards.append(generic_map_card)

    def houses_same_count(self):
        house_count = self.generic_map_cards[0].houses
        for map_card in self.generic_map_cards:
            if house_count != map_card.houses:
                return False
        return True

    def all_map_cards_available(self):
        return self.count == len(self.generic_map_cards)

    def check_other_map_cards_have_more_houses_than_current_map_card(self, map_card):
        f = [m for m in self.generic_map_cards if m.count < map_card.count]
        return len(f) == self.count - 1