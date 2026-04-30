import pygame
import sys
from datetime import datetime
from tools import *

pygame.init()

W, H = 1200, 700
TOOLBAR_H = 110

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("TSIS2 Paint")

canvas = pygame.Surface((W, H - TOOLBAR_H))
canvas.fill((0, 0, 0))

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

# ---------- STATE ----------
color = (255, 255, 255)
brush_size = 5
tool = "pencil"

drawing = False
start_pos = None
last_pos = None

text_mode = False
text = ""
text_pos = (0, 0)


# ---------- UI ----------
buttons = [
    ("Pen", "pencil", 10),
    ("Line", "line", 90),
    ("Rect", "rect", 170),
    ("Square", "square", 250),
    ("Circle", "circle", 330),
    ("R-Tr", "rtri", 410),
    ("E-Tr", "etri", 490),
    ("Rh", "rhomb", 570),
    ("Fill", "fill", 650),
    ("Erase", "erase", 730),
    ("Text", "text", 810),
]

sizes = [
    ("S", 2, 950),
    ("M", 5, 1000),
    ("L", 10, 1050),
]

palette = [
    ((255, 255, 255), 10),
    ((255, 0, 0), 50),
    ((0, 255, 0), 90),
    ((0, 0, 255), 130),
    ((255, 255, 0), 170),
    ((255, 0, 255), 210),
    ((0, 255, 255), 250),
]


def draw_toolbar():
    pygame.draw.rect(screen, (40, 40, 40), (0, 0, W, TOOLBAR_H))

    for name, t, x in buttons:
        r = pygame.Rect(x, 10, 70, 30)
        pygame.draw.rect(screen, (90, 90, 90), r)
        screen.blit(font.render(name, True, (255, 255, 255)), (x + 5, 15))

    for name, size, x in sizes:
        r = pygame.Rect(x, 10, 40, 30)
        pygame.draw.rect(screen, (120, 120, 120), r)
        screen.blit(font.render(name, True, (255, 255, 255)), (x + 12, 15))

    for col, x in palette:
        pygame.draw.rect(screen, col, (x, 55, 25, 25))


def get_tool(pos):
    for name, t, x in buttons:
        if pygame.Rect(x, 10, 70, 30).collidepoint(pos):
            return t
    return None


def get_size(pos):
    for name, size, x in sizes:
        if pygame.Rect(x, 10, 40, 30).collidepoint(pos):
            return size
    return None


def get_color(pos):
    for col, x in palette:
        if pygame.Rect(x, 55, 25, 25).collidepoint(pos):
            return col
    return None


# ---------- MAIN LOOP ----------
while True:
    screen.fill((30, 30, 30))
    draw_toolbar()

    screen.blit(canvas, (0, TOOLBAR_H))

    mouse = pygame.mouse.get_pos()
    pos = (mouse[0], mouse[1] - TOOLBAR_H)

    # preview
    if drawing and tool in ["line", "rect", "square", "circle", "rtri", "etri", "rhomb"]:
        temp = canvas.copy()

        if tool == "line":
            draw_line(temp, color, start_pos, pos, brush_size)
        elif tool == "rect":
            draw_rect(temp, color, start_pos, pos, brush_size)
        elif tool == "square":
            draw_square(temp, color, start_pos, pos, brush_size)
        elif tool == "circle":
            draw_circle(temp, color, start_pos, pos, brush_size)
        elif tool == "rtri":
            draw_right_triangle(temp, color, start_pos, pos, brush_size)
        elif tool == "etri":
            draw_equilateral_triangle(temp, color, start_pos, pos, brush_size)
        elif tool == "rhomb":
            draw_rhombus(temp, color, start_pos, pos, brush_size)

        screen.blit(temp, (0, TOOLBAR_H))

    # text preview
    if text_mode:
        screen.blit(font.render(text, True, color), (text_pos[0], text_pos[1] + TOOLBAR_H))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # keyboard
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                brush_size = 2
            elif event.key == pygame.K_2:
                brush_size = 5
            elif event.key == pygame.K_3:
                brush_size = 10

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                name = datetime.now().strftime("img_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, name)

            if text_mode:
                if event.key == pygame.K_RETURN:
                    canvas.blit(font.render(text, True, color), text_pos)
                    text_mode = False
                    text = ""
                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text = ""
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # mouse
        if event.type == pygame.MOUSEBUTTONDOWN:

            if mouse[1] < TOOLBAR_H:
                t = get_tool(mouse)
                if t: tool = t

                s = get_size(mouse)
                if s: brush_size = s

                c = get_color(mouse)
                if c: color = c

                continue

            if tool == "fill":
                flood_fill(canvas, *pos, color)

            elif tool == "text":
                text_mode = True
                text = ""
                text_pos = pos

            else:
                drawing = True
                start_pos = pos
                last_pos = pos

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:

                if tool == "line":
                    draw_line(canvas, color, start_pos, pos, brush_size)
                elif tool == "rect":
                    draw_rect(canvas, color, start_pos, pos, brush_size)
                elif tool == "square":
                    draw_square(canvas, color, start_pos, pos, brush_size)
                elif tool == "circle":
                    draw_circle(canvas, color, start_pos, pos, brush_size)
                elif tool == "rtri":
                    draw_right_triangle(canvas, color, start_pos, pos, brush_size)
                elif tool == "etri":
                    draw_equilateral_triangle(canvas, color, start_pos, pos, brush_size)
                elif tool == "rhomb":
                    draw_rhombus(canvas, color, start_pos, pos, brush_size)

            drawing = False

        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                draw_line(canvas, color, last_pos, pos, brush_size)
                last_pos = pos

            if drawing and tool == "erase":
                erase(canvas, pos, brush_size)

    pygame.display.flip()
    clock.tick(60)