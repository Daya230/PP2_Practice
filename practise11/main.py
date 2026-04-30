import pygame
import sys

from snake import snake_game 
from racer import racer_game
from paint import paint_game
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Game Menu")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_menu():
    screen.fill(BLACK)

    title = font.render("Choose a game", True, WHITE)
    snake_text = font.render("'1' - Snake", True, WHITE)
    racer_text = font.render("'2' - Racer", True, WHITE)
    paint_text = font.render("'3' - Paint", True, WHITE)
    exit_text = font.render("ESC - Exit", True, WHITE)

    screen.blit(title, (180, 120))
    screen.blit(snake_text, (200, 170))
    screen.blit(racer_text, (200, 210))
    screen.blit(paint_text, (200, 250))
    screen.blit(exit_text, (200, 290))


def main():
    running = True

    while running:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snake_game(screen, clock)
                elif event.key == pygame.K_2:
                    racer_game()
                elif event.key == pygame.K_3:
                    paint_game()
                if event.key == pygame.K_ESCAPE:
                    running = False



        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()