import pygame
import math


def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)


def draw_rect(surface, color, start, end, size):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, size)


def draw_square(surface, color, start, end, size):
    side = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
    rect = pygame.Rect(start, (side, side))
    pygame.draw.rect(surface, color, rect, size)


def draw_circle(surface, color, start, end, size):
    radius = int(math.hypot(end[0]-start[0], end[1]-start[1]))
    pygame.draw.circle(surface, color, start, radius, size)


def draw_right_triangle(surface, color, start, end, size):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, color, points, size)


def draw_equilateral_triangle(surface, color, start, end, size):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    height = abs(dy)

    p1 = start
    p2 = end
    p3 = (start[0] + dx // 2, start[1] - height)

    pygame.draw.polygon(surface, color, [p1, p2, p3], size)


def draw_rhombus(surface, color, start, end, size):
    cx = (start[0] + end[0]) // 2
    cy = (start[1] + end[1]) // 2

    dx = abs(end[0] - start[0]) // 2
    dy = abs(end[1] - start[1]) // 2

    points = [
        (cx, cy - dy),
        (cx + dx, cy),
        (cx, cy + dy),
        (cx - dx, cy)
    ]

    pygame.draw.polygon(surface, color, points, size)


def flood_fill(surface, x, y, new_color):
    W, H = surface.get_size()
    target = surface.get_at((x, y))
    if target == new_color:
        return

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= W or y < 0 or y >= H:
            continue

        if surface.get_at((x, y)) != target:
            continue

        surface.set_at((x, y), new_color)

        stack.append((x+1, y))
        stack.append((x-1, y))
        stack.append((x, y+1))
        stack.append((x, y-1))


def erase(surface, pos, size):
    pygame.draw.circle(surface, (0, 0, 0), pos, size)