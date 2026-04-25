import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 20)

snake = [(100, 100), (80, 100), (60, 100)]
dx, dy = CELL, 0

def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            return (x, y)

food = generate_food()


score = 0
level = 1
speed = 10

running = True

while running:
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL
            if event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL
            if event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL, 0
            if event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL, 0

    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False

    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = generate_food()

        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, CELL, CELL))

    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()