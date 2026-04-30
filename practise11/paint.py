import pygame
import math

def paint_game():


    pygame.init()
    screen = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Simple Paint (Beginner)")

    clock = pygame.time.Clock()

    # main drawing surface
    canvas = pygame.Surface((1200, 600))
    canvas.fill((0, 0, 0))

    radius = 5

    # current color mode
    mode = 'blue'

    # drawing data
    points = []
    figures = []

    # drawing state
    drawing = True

    # modes:
    # 1 - free draw line
    # 2 - rectangle
    # 3 - circle
    # 4 - square
    # 5 - right triangle
    # 6 - equilateral triangle
    # 7 - rhombus
    drawing_mode = 1

    fig_start = None

    text = "P - pause | L line | Z rect | X circle | S square | T right tri | E equilateral | R rhombus | A clear"

    # color buttons
    r = pygame.Rect(30, 150, 30, 30)
    g = pygame.Rect(30, 200, 30, 30)
    b = pygame.Rect(30, 250, 30, 30)

    while True:
        pressed = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        ctrl = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        alt = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return

                # pause drawing
                if event.key == pygame.K_p:
                    drawing = not drawing

                # clear canvas
                if event.key == pygame.K_a:
                    canvas.fill((0, 0, 0))
                    points = []
                    figures = []

                # free draw
                if event.key == pygame.K_l:
                    drawing_mode = 1

                # rectangle
                if event.key == pygame.K_z:
                    drawing_mode = 2

                # circle
                if event.key == pygame.K_x:
                    drawing_mode = 3

                # square
                if event.key == pygame.K_s:
                    drawing_mode = 4

                # right triangle
                if event.key == pygame.K_t:
                    drawing_mode = 5

                # equilateral triangle
                if event.key == pygame.K_e:
                    drawing_mode = 6

                # rhombus
                if event.key == pygame.K_r:
                    drawing_mode = 7

            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    fig_start = mouse_pos

                if event.button == 3:
                    radius = max(1, radius - 1)

                # color selection
                if r.collidepoint(mouse_pos):
                    mode = 'red'
                if g.collidepoint(mouse_pos):
                    mode = 'green'
                if b.collidepoint(mouse_pos):
                    mode = 'blue'

            if event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1 and fig_start is not None:
                    figures.append((fig_start, mouse_pos, drawing_mode, mode, radius))
                    fig_start = None

            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] and drawing_mode == 1:
                    points.append(event.pos)

        # draw free hand
        if drawing and drawing_mode == 1 and len(points) > 1:
            draw_line(canvas, points[-2], points[-1], radius, mode)

        #shapes
        for f in figures:
            draw_shape(canvas, f)

        figures = []

        # render
        screen.fill((0, 0, 0))
        screen.blit(canvas, (0, 0))

        # preview shape
        if fig_start:
            draw_shape(screen, (fig_start, mouse_pos, drawing_mode, mode, radius))

        # UI text
        font = pygame.font.SysFont(None, 22)
        screen.blit(font.render(text, True, (255, 255, 255)), (10, 10))

        # color boxes
        pygame.draw.rect(screen, (255, 0, 0), r)
        pygame.draw.rect(screen, (0, 255, 0), g)
        pygame.draw.rect(screen, (0, 0, 255), b)

        pygame.display.flip()
        clock.tick(60)


# fraw shapes
def draw_shape(screen, data):
    start, end, mode, color_mode, width = data

    x1, y1 = start
    x2, y2 = end

    color = get_color(color_mode)

    # rectangle
    if mode == 2:
        pygame.draw.rect(screen, color,
                         pygame.Rect(min(x1, x2), min(y1, y2),
                                     abs(x2 - x1), abs(y2 - y1)), width)

    # circle
    elif mode == 3:
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        r = int(math.hypot(x2 - x1, y2 - y1) / 2)
        pygame.draw.circle(screen, color, (cx, cy), max(1, r), width)

    # square (force equal sides)
    elif mode == 4:
        size = max(abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(screen, color,
                         pygame.Rect(x1, y1, size, size), width)

    # right triangle
    elif mode == 5:
        points = [(x1, y1), (x2, y1), (x1, y2)]
        pygame.draw.polygon(screen, color, points, width)

    # equilateral triangle (simple approx)
    elif mode == 6:
        side = abs(x2 - x1)
        height = int((3 ** 0.5 / 2) * side)
        points = [(x1, y2), (x1 + side, y2), (x1 + side // 2, y2 - height)]
        pygame.draw.polygon(screen, color, points, width)

    # rhombus
    elif mode == 7:
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        points = [(mx, y1), (x2, my), (mx, y2), (x1, my)]
        pygame.draw.polygon(screen, color, points, width)


#draw a line

def draw_line(screen, start, end, width, mode):
    color = get_color(mode)

    dx = end[0] - start[0]
    dy = end[1] - start[1]

    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return

    for i in range(steps):
        t = i / steps
        x = int(start[0] + dx * t)
        y = int(start[1] + dy * t)
        pygame.draw.circle(screen, color, (x, y), width)



def get_color(mode):
    if mode == 'red':
        return (255, 0, 0)
    if mode == 'green':
        return (0, 255, 0)
    if mode == 'blue':
        return (0, 0, 255)
    return (255, 255, 255)

