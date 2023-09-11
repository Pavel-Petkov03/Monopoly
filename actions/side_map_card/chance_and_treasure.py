from actions.base_action import Action
from flash_cards.decks import ChanceHolder, TreasureHolder


class BaseChanceAndTreasureAction(Action):
    holder = None

    def execute(self):
        self.holder.get_card().exec(self.renderer)
        self.holder.make_shift()
        self.renderer.remove_texture()


class ChanceAction(BaseChanceAndTreasureAction):
    holder = ChanceHolder()


class TreasureAction(BaseChanceAndTreasureAction):
    holder = TreasureHolder()
