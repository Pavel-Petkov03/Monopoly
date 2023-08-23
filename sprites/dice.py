import random
import os
import pygame

from actions.dice.move_player import MovePlayer
from animations.animation_frame import DiceAnimationFrame
from animations.dice_animation import DiceAnimation
from events.dice_click import DiceClickEvent, PlayerMovementEvent
from sprites.texture import Texture
from vars import screen_rect_size, BASE_DIR


class Dice(Texture):
    ANIMATION_IMAGES = [os.path.join(BASE_DIR, "images", "dice", "animation", f"{i}.png") for i in range(1, 7)]

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = screen_rect_size / 24
        self.height = screen_rect_size / 24
        self.animation_images = self.load_images(self.ANIMATION_IMAGES)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image.fill("white")
        self.current_image = self.animation_images[1]
        self.calculated_dice = None
        self.dice_animation_class = DiceAnimation(x, y, self.width, self.height)

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
        self.image.fill("white")
        self.image.blit(self.current_image, (0,0))
        surface.blit(self.image, (self.x, self.y))

    def calculate_num(self):
        self.calculated_dice = random.randint(1, 6)
        self.current_image = self.animation_images[self.calculated_dice - 1]
        return self.calculated_dice


class Dices(Texture):

    def __init__(self, render_state):
        super().__init__()
        dice1 = Dice(screen_rect_size / 2, screen_rect_size / 2)
        dice2 = Dice(screen_rect_size / 2 + dice1.width, screen_rect_size / 2)
        self.thrown = 0
        self.render_state = render_state
        self.dices = (dice1, dice2)
        self.dice_animation_frame = DiceAnimationFrame(1000, self)
        self.move_player_animation = MovePlayer(render_state, self)
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
        for dice in self.dices:
            dice.blit(window)
