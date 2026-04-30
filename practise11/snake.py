import pygame
import random

def snake_game(screen, clock):
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    CELL = 20
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    #цвета
    WHITE = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (255, 255, 255)
    YELLOW = (255, 255, 0)

    font = pygame.font.SysFont("Arial", 20)
    big_font = pygame.font.SysFont("Arial", 40)

    #змейка
    snake = [(100, 100), (80, 100), (60, 100)] #snake = [(голова),(тело),(хвост)]

    dx = CELL
    dy = 0

    score = 0
    level = 1
    speed = 10

    #еда ранд
    def new_food():
        while True:
            x = random.randrange(0, WIDTH, CELL)
            y = random.randrange(0, HEIGHT, CELL)

            if (x, y) not in snake:
                return (x, y, random.choice([1, 2, 3]), pygame.time.get_ticks())
    food_x, food_y, food_w, food_time = new_food()

    game_over = False

    running = True
    while running:

        screen.fill(BLACK)

        # game over menu 
        if game_over:
            #текст проигрыша
            #font.render(текст, сглаживание,цвет)
            text1 = big_font.render("YOU LOST", True, RED)
            text2 = font.render(f"Score: {score}", True, WHITE)
            text3 = font.render(f"Level: {level}", True, WHITE)
            text4 = font.render("Press R to restart, ESC to menu or close the window", True, WHITE)

            #вывод на экран
            screen.blit(text1, (200, 120))
            screen.blit(text2, (240, 180))
            screen.blit(text3, (240, 210))
            screen.blit(text4, (120, 260))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return #выходит из функции в менюшку

                    if event.key == pygame.K_r:
                        # перезапуск игры, берутся начальные данные
                        snake = [(100, 100), (80, 100), (60, 100)]
                        dx, dy = CELL, 0
                        score = 0
                        level = 1
                        speed = 10
                        food_x, food_y, food_w, food_time = new_food()
                        game_over = False

            pygame.display.flip()
            clock.tick(60)
            continue

        #клавиши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -CELL
                if event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, CELL
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -CELL, 0
                if event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = CELL, 0

        # движение змейки 
        head_x, head_y = snake[0]
        new_head = (head_x + dx, head_y + dy)

        #проверка стен
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            game_over = True

        #проверка столкновения с себой
        if new_head in snake:
            game_over = True
        snake.insert(0, new_head)

        #еда
        if new_head == (food_x, food_y):
            score += food_w

            level = score // 5 + 1
            speed = 10 + (level - 1) * 2 #за каждый уровень +2 к скорости

            food_x, food_y, food_w, food_time = new_food()
        else:
            snake.pop()

        # если еда долго лежит, создаем новую
        if pygame.time.get_ticks() - food_time > 5000: #get_ticks() берет время с момента запуска, далее если прошло 5000 милисекунд ~ 5 секунд с появление, то генерируется новый
        
            food_x, food_y, food_w, food_time = new_food()

        # генерация еды
        if food_w == 1:
            color = RED
        elif food_w == 2:
            color = YELLOW
        else:
            color = WHITE

        pygame.draw.rect(screen, color, (food_x, food_y, CELL, CELL))

        # генерируем изображение змейки на экране
        for part in snake: 
            pygame.draw.rect(screen, GREEN, (*part, CELL, CELL))



        #текст меню
        text = font.render(f"Score: {score} Level: {level}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(speed)