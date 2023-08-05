import random
import os
import pygame

from events.dice_click import DiceClickEvent
from sprites.texture import Texture, TextureGroup
from vars import screen_rect_size, BASE_DIR


class Dice(Texture):
    ANIMATION_IMAGES = [os.path.join(BASE_DIR, "images", "dice", "animation", f"{i}.png") for i in range(1, 7)]

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = screen_rect_size / 12
        self.height = screen_rect_size / 12
        self.animation_images = self.load_images(self.ANIMATION_IMAGES)
        self.image = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.image.fill("white")
        self.current_image = self.animation_images[5]
        self.calculated_dice = None


    def load_images(self, location_array):
        res = []
        for location in location_array:
            image = pygame.image.load(location)
            image = pygame.transform.scale(image, (self.width, self.height))
            res.append(image)
        return res

    def on_animation(self):
        index = random.randint(0, 5)
        self.image.fill("white")
        self.current_image = self.animation_images[index]

    def blit(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def calculate_num(self):
        self.calculated_dice = random.randint(1, 6)
        print(self.calculated_dice)
        self.current_image = self.animation_images[self.calculated_dice - 1]


class Dices(Texture):

    def __init__(self):
        super().__init__()
        dice1 = Dice(screen_rect_size / 2, screen_rect_size / 2)
        dice2 = Dice(screen_rect_size / 2 + dice1.width, screen_rect_size / 2)
        self.on_display = False
        self.animation_on = True
        self.start = None
        self.end = None
        self.dices = (dice1, dice2)
        self.event_list = [
            DiceClickEvent
        ]

    def update(self):

        if self.on_display:
            if self.animation_on:
                if self.start <= self.end:
                    self.start = pygame.time.get_ticks()
                    for sprite in self.dices:
                        sprite.on_animation()
                else:
                    self.animation_on = False
            else:
                for sprite in self.dices:
                    sprite.calculate_num()
                self.on_display = False
                self.animation_on = True
        for sprite in self.dices:
            sprite.image.blit(sprite.current_image, (0, 0))

    def on_click(self):
        self.on_display = True
        self.start = pygame.time.get_ticks()
        self.end = pygame.time.get_ticks() + 1000

    def blit(self, window):
        for dice in self.dices:
            dice.blit(window)



