from flash_cards.chance.base import ChanceCard


class BordOwnerPayment(ChanceCard):
    def __init__(self):
        super().__init__("ИЗБРАН СТЕ ЗА ПРЕДСТЕДАТЕЛ НА БОРДА ПЛАТЕТЕ НА ВСЕКИ ИГРАЧ ПО 50")

    def exec(self, renderer):
        all_players = renderer.players
        for player in all_players:
            if player != renderer.current_player:
                renderer.current_player.money -= 50
                player.money += 50