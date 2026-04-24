import pygame
import sys
import random
from pygame.locals import *

pygame.init()

FPS = 60
clock = pygame.time.Clock()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont(None, 36)

class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2, HEIGHT-80, 40, 60)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        if keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(40, WIDTH-40), 0, 40, 60)

    def reset(self):
        self.rect.x = random.randint(40, WIDTH-40)
        self.rect.y = 0

    def move(self):
        self.rect.move_ip(0, 6)

        if self.rect.top > HEIGHT:
            self.reset()

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

class Coin:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(40, WIDTH-40), 0, 20, 20)

    def spawn(self):
        self.rect.x = random.randint(40, WIDTH-40)
        self.rect.y = 0

    def move(self):
        self.rect.move_ip(0, 5)

        if self.rect.top > HEIGHT:
            self.spawn()

    def draw(self):
        pygame.draw.rect(screen, YELLOW, self.rect)

player = Player()
enemy = Enemy()
coin = Coin()

score = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player.update()
    enemy.move()
    coin.move()

    if player.rect.colliderect(enemy.rect):
        pygame.quit()
        sys.exit()

    if player.rect.colliderect(coin.rect):
        score += 1
        coin.spawn()

    screen.fill(WHITE)

    player.draw()
    enemy.draw()
    coin.draw()

    text = font.render(f"Coins: {score}", True, BLACK)
    screen.blit(text, (WIDTH - 140, 20))

    pygame.display.update()
    clock.tick(FPS)