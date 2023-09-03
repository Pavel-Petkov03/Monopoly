from actions.side_map_card.chance_and_treasure import ChanceAction, TreasureAction
from flash_cards.decks import ChanceHolder, TreasureHolder
from sprites.button import Button
from sprites.modals.base_modal import Modal


class BaseChanceAndTreasureModal(Modal):
    ok_button_action_class = None

    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer
        self.set_header(self.ok_button_action_class.holder.get_card().header)
        self.add([self.get_ok_button()])

    def get_ok_button(self):
        return Button(
            width_and_height_tuple=(self.width / 4, self.height / 12),
            background="green",
            text="Ок",
            text_size=20,
            text_color="black",
            blit_pos=(self.surface.get_width() / 2 - self.width / 4 / 2, self.surface.get_height() - self.height / 12),
            hover_color="yellow",
            inherit_x=self.x,
            inherit_y=self.y,
            action_class=self.ok_button_action_class(self.renderer)
        )

    def blit(self, window):
        for sprite in self.sprites():
            sprite.blit(self.surface)
        super().blit(window)


class ChanceModal(BaseChanceAndTreasureModal):
    ok_button_action_class = ChanceAction


class TreasureModal(BaseChanceAndTreasureModal):
    ok_button_action_class = TreasureAction
