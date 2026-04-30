import pygame
import sys
import random

def racer_game():
    pygame.init()
    WIDTH, HEIGHT = 400, 800

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Racer")

    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.SysFont("arial", 40)
    small_font = pygame.font.SysFont("arial", 20)

    BASE_SPEED = 5
    SPEED = BASE_SPEED

    SCORE = 0
    COINS = 0
    N = 5

    game_over = False

    # player
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((40, 60))
            self.image.fill((0, 0, 255))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 2, HEIGHT - 80)

        def move(self):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.move_ip(-5, 0)

            if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.move_ip(5, 0)

    # enemy
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((40, 60))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect()
            self.reset()

        def reset(self):
            self.rect.center = (random.randint(50, WIDTH - 50), 0)

        def move(self):
            self.rect.move_ip(0, SPEED)
            if self.rect.top > HEIGHT:
                self.reset()

    player = Player()
    enemy = Enemy()

    enemies = pygame.sprite.Group(enemy)
    all_sprites = pygame.sprite.Group(player, enemy)

    coin_x = random.randint(50, WIDTH - 50)
    coin_y = 0
    coin_value = random.choice([1, 2, 5])

    while True:

        screen.fill(WHITE)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if game_over:
                    if event.key == pygame.K_r:
                        # restart
                        SCORE = 0
                        COINS = 0
                        SPEED = BASE_SPEED

                        player.rect.center = (WIDTH // 2, HEIGHT - 80)
                        enemy.reset()

                        coin_x = random.randint(50, WIDTH - 50)
                        coin_y = 0
                        coin_value = random.choice([1, 2, 5])

                        game_over = False

                    if event.key == pygame.K_ESCAPE:
                        return

        # level
        level = COINS // N + 1
        SPEED = BASE_SPEED + (level - 1)

        # gameover
        if game_over:

            text1 = font.render("YOU LOST", True, BLACK)
            text2 = small_font.render(f"Score: {SCORE}", True, BLACK)
            text3 = small_font.render(f"Coins: {COINS}", True, BLACK)
            text4 = small_font.render("R - restart | ESC - menu", True, BLACK)

            screen.blit(text1, (WIDTH//2-100, HEIGHT//2 - 60))
            screen.blit(text2, (WIDTH//2-100, HEIGHT//2 + 10))
            screen.blit(text3, (WIDTH//2-100, HEIGHT//2 - 10))
            screen.blit(text4, (WIDTH//2-100, HEIGHT//2 + 60))

            pygame.display.update()
            clock.tick(10)
            continue

        # move
        player.move()
        enemy.move()

        # coin system
        pygame.draw.circle(screen, (255, 215, 0), (coin_x, coin_y), 10)
        coin_y += SPEED

        if coin_y > HEIGHT:
            coin_x = random.randint(50, WIDTH - 50)
            coin_y = 0
            coin_value = random.choice([1, 2, 5])

        coin_rect = pygame.Rect(coin_x, coin_y, 20, 20)

        if player.rect.colliderect(coin_rect):
            SCORE += coin_value
            COINS += 1

            coin_x = random.randint(50, WIDTH - 50)
            coin_y = 0
            coin_value = random.choice([1, 2, 5])

        # draw
        for obj in all_sprites:
            screen.blit(obj.image, obj.rect)

        screen.blit(small_font.render(f"Score: {SCORE}", True, BLACK), (10, 10))
        screen.blit(small_font.render(f"Coins: {COINS}", True, BLACK), (10, 30))
        screen.blit(small_font.render(f"Level: {level}", True, BLACK), (10, 50))
        screen.blit(small_font.render(f"Speed: {SPEED}", True, BLACK), (10, 70))

        if pygame.sprite.spritecollideany(player, enemies):
            game_over = True

        pygame.display.flip()
        clock.tick(60)