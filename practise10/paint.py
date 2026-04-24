import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    clock = pygame.time.Clock()

    canvas = pygame.Surface((1200, 600))
    canvas.fill((0, 0, 0))

    radius = 15
    mode = 'blue'
    points = []
    strokes = []
    figures = []

    drawing = True
    drawing_mode = 1
    fig_start = None

    text = """
 P = Stop/Draw
 Z = Rectangle
 X = Circle
 L = Line
 C = Eraser
 A = Clear
"""

    r = pygame.Rect(30, 150, 30, 30)
    g = pygame.Rect(30, 200, 30, 30)
    b = pygame.Rect(30, 250, 30, 30)

    while True:
        pressed = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_p:
                    drawing = not drawing

                elif event.key == pygame.K_c:
                    mode = 'erase'
                    drawing_mode = 1
                    points = []

                elif event.key == pygame.K_l:
                    drawing_mode = 1

                elif event.key == pygame.K_z:
                    drawing_mode = 2

                elif event.key == pygame.K_x:
                    drawing_mode = 3

                elif event.key == pygame.K_a:
                    strokes = []
                    points = []
                    figures = []
                    canvas.fill((0, 0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    if drawing_mode in (2, 3):
                        fig_start = mouse_pos

                    if drawing_mode == 1:
                        if points and mode != 'erase':
                            strokes.append((points.copy(), mode, radius))
                        points = []

                elif event.button == 3:
                    radius = max(1, radius - 1)

                if r.collidepoint(mouse_pos):
                    mode = 'red'
                elif g.collidepoint(mouse_pos):
                    mode = 'green'
                elif b.collidepoint(mouse_pos):
                    mode = 'blue'

            if event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1:

                    if drawing_mode == 1 and points:
                        if mode != 'erase':
                            strokes.append((points.copy(), mode, radius))
                        points = []

                    if drawing_mode in (2, 3) and fig_start:
                        figures.append((fig_start, mouse_pos, drawing_mode))
                        fig_start = None

            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:

                    if drawing_mode == 1:
                        points.append(event.pos)
                        points = points[-256:]

        if drawing:
            if drawing_mode == 1 and len(points) > 1:
                drawLineBetween(canvas, 0, points[-2], points[-1], radius, mode)

        if fig_start is None and figures:
            for f in figures:
                s, e, t = f
                drawfig(canvas, s, e, radius, mode, t)
            figures = []

        screen.fill((0, 0, 0))
        screen.blit(canvas, (0, 0))

        if fig_start:
            drawfig(screen, fig_start, mouse_pos, radius, mode, drawing_mode)

        font = pygame.font.SysFont(None, 24)
        screen.blit(font.render(text, True, (255, 255, 255)), (10, 10))

        pygame.draw.rect(screen, (255, 0, 0), r)
        pygame.draw.rect(screen, (0, 255, 0), g)
        pygame.draw.rect(screen, (0, 0, 255), b)

        pygame.display.flip()
        clock.tick(60)


def drawfig(screen, start, end, width, mode, draw_mode):

    x1, y1 = start
    x2, y2 = end

    if mode == 'erase':
        color = (0, 0, 0)
    else:
        color = {
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255)
        }.get(mode, (255, 255, 255))

    if draw_mode == 2:
        rect = pygame.Rect(min(x1, x2), min(y1, y2),
                           abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(screen, color, rect, width)

    elif draw_mode == 3:
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        r = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 / 2)
        pygame.draw.circle(screen, color, (cx, cy), max(1, r), width)


def drawLineBetween(screen, index, start, end, width, mode):

    color = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'erase': (0, 0, 0)
    }.get(mode, (255, 255, 255))

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return

    for i in range(steps):
        t = i / steps
        x = int(start[0] * (1 - t) + end[0] * t)
        y = int(start[1] * (1 - t) + end[1] * t)
        pygame.draw.circle(screen, color, (x, y), width)


main()