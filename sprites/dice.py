import random
import os
import pygame
from vars import screen_rect_size, BASE_DIR


class Dice(pygame.sprite.Sprite):
    ANIMATION_IMAGES = [os.path.join(BASE_DIR, "images", "dice", "animation", f"{i}.png") for i in range(1, 7)]

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.animation_images = self.load_images(self.ANIMATION_IMAGES)
        self.on_display = False
        self.animation_on = True
        self.image = pygame.Surface((screen_rect_size / 12, screen_rect_size / 12))
        self.rect = pygame.Rect(x, y, screen_rect_size / 12, screen_rect_size / 12)
        self.image.fill("white")
        self.current_image = self.animation_images[5]
        self.calculated_dice = None
        self.start = None
        self.end = None

    @staticmethod
    def load_images(location_array):
        res = []
        for location in location_array:
            image = pygame.image.load(location)
            image = pygame.transform.scale(image, (screen_rect_size / 12, screen_rect_size / 12))
            res.append(image)
        return res

    def update(self):
        if self.on_display:
            if self.animation_on:
                if self.start <= self.end:
                    self.start = pygame.time.get_ticks()
                    index = random.randint(0, 5)
                    self.image.fill("white")
                    self.current_image = self.animation_images[index]
                else:
                    self.animation_on = False
            else:
                self.calculated_dice = random.randint(1, 6)
                self.current_image = self.animation_images[self.calculated_dice - 1]
                self.on_display = False
                self.animation_on = True
        self.image.blit(self.current_image, (0, 0))

    def blit(self, surface):
        surface.blit(self.image, (self.x, self.y))
