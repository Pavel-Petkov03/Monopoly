import random
import os
import pygame

from actions.dice.move_player import MovePlayer
from animations.animation_frame import DiceAnimationFrameMovement
from animations.dice_animation import DiceAnimation
from events.dice_click import DiceClickEvent, PlayerMovementEvent
from sprites.texture import Texture
from vars import screen_rect_size, BASE_DIR, board_screen_x, board_screen_y


class Dice(Texture):

    ANIMATION_IMAGES = [os.path.join(BASE_DIR, "images", "dice", "animation", f"{i}.png") for i in range(1, 7)]

    def __init__(self, x, y, renderer):
        super().__init__(screen_rect_size / 24, screen_rect_size / 24)
        self.x = x
        self.y = y
        self.animation_images = self.load_images(self.ANIMATION_IMAGES)
        self.rect = pygame.Rect(self.x + board_screen_x, self.y + board_screen_y, self.width, self.height)
        self.surface.fill("white")
        self.current_image = self.animation_images[1]
        self.calculated_dice = None
        self.dice_animation_class = DiceAnimation(self.x, self.y,  self.width, self.height, renderer)

    def load_images(self, location_array):
        res = []
        for location in location_array:
            image = pygame.image.load(location).convert_alpha()
            image = pygame.transform.scale(image, (self.width, self.height)).convert_alpha()
            res.append(image)
        return res

    def on_animation(self):
        self.dice_animation_class.animate()

    def blit(self, surface):
        self.surface.fill("white")
        self.surface.blit(self.current_image, (0, 0))
        surface.blit(self.surface, (self.x, self.y))

    def calculate_num(self):
        self.calculated_dice = random.randint(1, 6)
        self.current_image = self.animation_images[self.calculated_dice - 1]
        return self.calculated_dice


class Dices(Texture):

    def __init__(self, renderer):
        super().__init__(screen_rect_size / 12, screen_rect_size / 24)
        self.renderer = renderer
        dice1 = Dice(screen_rect_size / 2, screen_rect_size / 2,renderer)
        dice2 = Dice(screen_rect_size / 2 + dice1.width, screen_rect_size / 2, renderer)
        self.thrown = 0
        self.dices = (dice1, dice2)
        self.dice_animation_frame = DiceAnimationFrameMovement(1000, self)
        self.move_player_animation = MovePlayer(renderer, self)
        self.event_list = [
            DiceClickEvent,
            PlayerMovementEvent
        ]

    def update(self):
        self.dice_animation_frame.execute()
        self.move_player_animation.execute()

    def dice_equal_sign(self):
        return self.dices[0].calculated_dice == self.dices[1].calculated_dice

    def blit(self, window):
        if not self.dice_animation_frame.animation_on:
            for dice in self.dices:
                dice.blit(window)
