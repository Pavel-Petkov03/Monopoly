import pygame

from events.map_card_event import MapCardEvent
from sprites.texture import Texture


class BaseMapCard(Texture):
    width = 0
    height = 0

    def __init__(self, x, y, color=None, caption=None, inside_image_path=None, price=None, rotation=None,
                 price_dict=None, neighborhood=None, house_price=None, side_image_type=None, rect_type=None):
        super().__init__(self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))
        self.x = x
        self.y = y
        self.neighborhood = neighborhood
        self.inside_image_path = inside_image_path
        self.inside_image_picture = None
        self.load_inside_image()
        self.caption = caption
        self.color = color
        self.price = price
        self.price_dict = price_dict
        self.rotation = rotation
        self.players = {}
        self.temporary_players = {}
        self.temporary_image = None
        self.owner = None
        self.owner_circle = None
        self.owner_circle_pos = self.get_circle_pos()
        self.house_price = house_price
        self.top_inner_rect = pygame.Rect(0, 0, self.width, self.height / 4)
        self.side_image_type = side_image_type
        self.rect_type = rect_type
        self.event_list = [
            MapCardEvent
        ]

    def get_circle_pos(self):
        if self.rotation == 0:
            current_x = self.x + self.width / 2
            current_y = self.y - self.height / 10

        elif self.rotation == 270:
            current_x = self.height + self.height / 10
            current_y = self.y + self.width / 2
        elif self.rotation == 180:
            current_x = self.x + self.width / 2
            current_y = self.height + self.height / 10
        else:
            current_x = self.x - self.height / 10
            current_y = self.y + self.width / 2
        return current_x, current_y

    def load_inside_image(self):
        if self.inside_image_path:
            self.inside_image_picture = pygame.image.load(f"images/board/{self.inside_image_path}").convert_alpha()

    def set_rect(self):
        self.image.fill("white")
        pygame.draw.rect(self.image, "black", self.image.get_rect(), 1)
        self.add_additional_data()

    def load_pieces(self):
        self.temporary_image = self.image.copy()
        scaled_width = self.top_inner_rect.width
        concatenated_dict = {**self.temporary_players, **self.players}
        scaled_height = self.height / (len(concatenated_dict) + 1)
        x = self.top_inner_rect.x
        y = self.top_inner_rect.y
        for player in concatenated_dict:
            image = player.piece_image
            image = pygame.transform.scale(image, (scaled_width, scaled_height))
            y += scaled_height
            self.temporary_image.blit(image, (x, y))

    def remove_player_from_all_players(self, player):
        self.players.pop(player)

    def remove_player_from_temporary(self, player):
        self.temporary_players.pop(player)

    def add_player_to_all_players(self, player):
        self.players[player] = player.piece_image

    def add_player_to_temporary(self, player):
        self.temporary_players[player] = player.piece_image

    def add_additional_data(self):
        pass

    def image_load(self, padding_percent):
        padding_top = int(self.height * (padding_percent / 100))
        padding_bottom = int(self.height * (padding_percent / 100))
        new_height = self.height - padding_top - padding_bottom
        scale_factor = new_height / self.inside_image_picture.get_height()
        new_width = int(self.inside_image_picture.get_width() * scale_factor)
        scaled_image = pygame.transform.scale(self.inside_image_picture, (new_width, new_height)).convert_alpha()
        x_offset = (self.width - new_width) // 2
        self.image.blit(scaled_image, (x_offset, padding_top))

    def set_caption(self, text, size, width, height):
        words = text.split(" ")
        padding = self.height / 12
        padding_counter = 0
        for word in words:
            self.create_text_and_blit(self.image, word, size, (0, 0, 0), (width, height + padding_counter))
            padding_counter += padding

    def draw_houses(self):
        pass

    def blit(self, window):
        self.load_pieces()
        self.draw_circle(window)
        self.draw_houses()
        rotated_image = pygame.transform.rotate(self.temporary_image, self.rotation)
        rect = rotated_image.get_rect()
        rect.x = self.x
        rect.y = self.y
        window.blit(rotated_image, rect)

    def draw_circle(self, window):
        if self.owner:
            pygame.draw.circle(window, self.owner.color, self.owner_circle_pos, 10)
