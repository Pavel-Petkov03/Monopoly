import pygame
import numpy as np
from math import *

from timer import Timer
from vars import screen


class Rotation:

    def __init__(self):
        self.angle = 0.0

    def rotate_z(self):
        return np.matrix([
            [cos(self.angle), -sin(self.angle), 0],
            [sin(self.angle), cos(self.angle), 0],
            [0, 0, 1],
        ])

    def rotate_y(self):
        return np.matrix([
            [cos(self.angle), 0, sin(self.angle)],
            [0, 1, 0],
            [-sin(self.angle), 0, cos(self.angle)],
        ])

    def rotate_x(self):
        return np.matrix([
            [1, 0, 0],
            [0, cos(self.angle), -sin(self.angle)],
            [0, sin(self.angle), cos(self.angle)],
        ])


class DiceAnimation(Rotation):
    vertecies = (
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1],
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1]
    )

    quads = (
        (0, 1, 2, 3),
        (4, 5, 6, 7),
        (0, 1, 5, 4),
        (2, 3, 7, 6),
        (1, 2, 6, 5),
        (0, 3, 7, 4)
    )

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (1, 2),
        (1, 5),
        (2, 3),
        (2, 6),
        (3, 7),
        (4, 5),
        (4, 7),
        (5, 6),
        (6, 7)
    )

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.points = [np.matrix(ar) for ar in self.vertecies]
        self.projected_points = [[n, n] for n in range(len(self.points))]
        self.projection_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.timer = Timer()
        self.speed = 5

    def animate(self):
        self.project_points()
        self.draw_polygon()
        self.draw_edges()

        self.angle += self.speed * self.timer.delta_time

    def project_points(self):
        for i, point in enumerate(self.points):
            rotated2d = np.dot(self.rotate_z(), point.reshape((3, 1)))
            rotated2d = np.dot(self.rotate_y(), rotated2d)
            rotated2d = np.dot(self.rotate_x(), rotated2d)
            projected2d = np.dot(self.projection_matrix, rotated2d)

            x = int(projected2d[0][0] * self.width) + self.x
            y = int(projected2d[1][0] * self.height) + self.y
            self.projected_points[i] = [x, y]

    def draw_polygon(self):
        for i, quad in enumerate(self.quads):
            all_projected_points = [self.projected_points[i] for i in quad]
            pygame.draw.polygon(screen, "white", all_projected_points)

    def draw_edges(self):
        for edge in self.edges:
            pygame.draw.line(screen,
                             "black",
                             (self.projected_points[edge[0]][0], self.projected_points[edge[0]][1]),
                             (self.projected_points[edge[1]][0], self.projected_points[edge[1]][1])
                             )
