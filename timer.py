import pygame

from utils import SingletonClass


class Timer(SingletonClass):
    def __init__(self):
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.delta_time = None

    def set_fps(self):
        self.delta_time = self.clock.tick(self.fps) / 1000

    def get_fps(self):
        return self.clock.get_fps()