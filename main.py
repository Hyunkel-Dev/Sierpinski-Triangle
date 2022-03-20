import math
import random
import sys
import pygame

from config import *



class Triangle:

    def __init__(self):
        self.update()

    def update(self):
        w, h = WINDOW_SIZE
        size = min(w, h)

        if size == w:
            offset = Vector2(0, 0 + (h - size) / 2)
        else:
            offset = Vector2(0 + (w - size) / 2, 0)

        dy = (2 - math.sqrt(3)) * size / 4

        self.points = (
            Vector2(0, size - dy) + offset,
            Vector2(size, size - dy) + offset,
            Vector2(size / 2, dy) + offset
        )

        self.center = Vector2(size / 2, size / 2 + dy) + offset


def add_point(points, n=1):
    for _ in range(n):
        other = random.choice(triangle.points)
        p = points[-1]
        points.append((other + p) / 2)


pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Sierpinski Triangle")

icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

triangle = Triangle()
points = [triangle.center]


while True:

    add_point(points, SPEED)

    window.fill(WINDOW_COLOR)

    # triangle
    pygame.draw.polygon(window, POINT_COLOR, triangle.points, 1)

    # points
    for point in points:
        if point != triangle.center:
            pygame.draw.rect(window, POINT_COLOR, (*point, 1, 1), 1)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            WINDOW_SIZE = Vector2(event.size)
            triangle.update()
            points = [triangle.center]

    pygame.time.wait(1000 // FPS)