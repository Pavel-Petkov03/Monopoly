from actions.generic_map_card.remove_modal import RemoveModalAction
from sprites.modals.base_modal import Modal
from sprites.button import Button
from sprites.map_card import GenericMapCard
from vars import board_screen_x, board_screen_y


class GenericMapCardModal(Modal):
    def __init__(self, renderer_state, map_card_state, current_player):
        self.inner_rect_color = map_card_state.color
        self.inner_rect_data = map_card_state.price_dict
        self.map_card_name = map_card_state.caption
        self.map_card_state = map_card_state
        self.renderer_state = renderer_state
        self.current_player = current_player
        self.yes_button_action_class = None
        self.ok_button_action_class = None

        super().__init__()
        self.map_card = GenericMapCard(
            self.width - 2 * self.x / 2,
            self.height - 2 * self.y / 4,
            self.inner_rect_color,
            self.map_card_name,
            self.inner_rect_data,
            (self.x / 2, self.y / 4)
        )
        self.add([self.map_card])

    def get_yes_button(self):
        return Button(
            width_and_height_tuple=(self.width / 4, self.height / 12),
            background="green",
            text="Да",
            text_size=20,
            text_color="black",
            blit_pos=(0, self.surface.get_height() - self.height / 12),
            hover_color="yellow",
            inherit_x=self.x + board_screen_x,
            inherit_y=self.y + board_screen_y,
            action_class=self.yes_button_action_class(self.renderer_state, self.map_card_state, self.current_player)
        )

    def get_no_button(self):
        return Button(
            width_and_height_tuple=(self.width / 4, self.height / 12),
            background="red",
            text="Не",
            text_size=20,
            text_color="black",
            blit_pos=(self.surface.get_width() - self.width / 4, self.surface.get_height() - self.height / 12),
            hover_color="yellow",
            inherit_x=self.x + board_screen_x,
            inherit_y=self.y + board_screen_y,
            action_class=RemoveModalAction(self.renderer_state, self.map_card_state, self.current_player)
        )

    def get_ok_button(self):
        return Button(
            width_and_height_tuple=(self.width / 4, self.height / 12),
            background="green",
            text="Ок",
            text_size=20,
            text_color="black",
            blit_pos=(self.surface.get_width() / 2 - self.width / 4 / 2, self.surface.get_height() - self.height / 12),
            hover_color="yellow",
            inherit_x=self.x + board_screen_x,
            inherit_y=self.y + board_screen_y,
            action_class=self.ok_button_action_class(self.renderer_state, self.map_card_state, self.current_player)
        )

    def blit(self, window):
        for sprite in self.sprites():
            sprite.blit(self.surface)
        super().blit(window)
