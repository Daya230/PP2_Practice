"""
-------------------------------------------------------------------------
PROJECT: TSIS 3 — Advanced Racer Arcade
AUTHOR: Dayana Muratkyzy Dutpaeva
STUDENT ID: PP2_25B030159
DESCRIPTION: Усовершенствованный гоночный симулятор с системой уровней,
             динамическими препятствиями и интеграцией базы данных.
-------------------------------------------------------------------------
"""

import pygame
import sys
import os
import random

# Импортируем функционал из твоих дополнительных файлов
from racer import Player, Enemy, Obstacle, PowerUp
from persistence import load_settings, save_settings, load_leaderboard, save_score
from ui import Button, TextInput

# Принудительно устанавливаем рабочую папку, чтобы ресурсы загружались корректно[cite: 3]
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- Инициализация систем ---
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Professional: Dayana's Edition")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Загружаем настройки из settings.json[cite: 3, 4]
user_settings = load_settings()

def get_sound(name):
    """Метод для безопасной загрузки звуков."""
    path = os.path.join('assets', 'sounds', name)
    try:
        return pygame.mixer.Sound(path)
    except:
        return None

snd_crash = get_sound('crash.wav')
snd_powerup = get_sound('powerup.wav')

# Проверка наличия музыки
music_found = False
try:
    pygame.mixer.music.load(os.path.join('assets', 'sounds', 'background.mp3'))
    music_found = True
except:
    pass

# --- Игровые переменные ---
state = "MENU"
active_player_name = "Dayana"
score = 0
distance = 0
current_level = 1
level_xp = 0
XP_THRESHOLD = 1000 

# Группы спрайтов для отрисовки и коллизий[cite: 3, 5]
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
powerups = pygame.sprite.Group()
coins = pygame.sprite.Group()

class GameCoin(pygame.sprite.Sprite):
    """Класс монеток с разной ценностью[cite: 3]."""
    def __init__(self):
        super().__init__()
        self.value = random.choice([1, 2, 5])
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        # Цвет монетки зависит от её веса[cite: 3, 5]
        self.color = (255, 215, 0) if self.value == 1 else (0, 255, 0) if self.value == 2 else (255, 0, 255)

        pygame.draw.circle(self.image, self.color, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([180, 260, 340])
        self.rect.y = -20
        self.speed = 4

    def update(self):
        self.rect.y += self.speed

player_car = None

def reset_session():
    """Сброс всех параметров перед началом заезда[cite: 3]."""
    global player_car, score, distance, current_level, level_xp
    all_sprites.empty()
    enemies.empty()
    obstacles.empty()
    powerups.empty()
    coins.empty()
    
    player_car = Player(user_settings["car_color"])
    all_sprites.add(player_car)
    
    score = 0
    distance = 0
    current_level = 1
    level_xp = 0
    
    if music_found and user_settings["sound"]:
        pygame.mixer.music.play(-1)

# Создание кнопок интерфейса[cite: 3, 6]
btn_play = Button(200, 150, 200, 50, "GO!")
btn_board = Button(200, 220, 200, 50, "TOP 10")
btn_settings = Button(200, 290, 200, 50, "SETTINGS")
btn_quit = Button(200, 360, 200, 50, "EXIT")
btn_back = Button(200, 500, 200, 50, "BACK")
btn_retry = Button(200, 350, 200, 50, "RETRY")
btn_menu = Button(200, 420, 200, 50, "MENU")
name_input = TextInput(200, 250, 200, 40)

# Таймеры спавна объектов[cite: 3]
ENEMY_EVENT = pygame.USEREVENT + 1
COIN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(ENEMY_EVENT, 1500)
pygame.time.set_timer(COIN_EVENT, 1200)

# --- Главный цикл ---
running = True
while running:
    # Отрисовка трассы и динамической разметки[cite: 3]
    screen.fill((50, 150, 50)) 
    pygame.draw.rect(screen, (40, 40, 40), (150, 0, 300, 600)) 
    for y in range(0, 600, 40):
        offset = (y + int(distance * 10)) % 600
        pygame.draw.rect(screen, (255, 255, 255), (245, offset, 10, 20))
        pygame.draw.rect(screen, (255, 255, 255), (345, offset, 10, 20))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        if state == "MENU":
            if btn_play.is_clicked(event): state = "NAME_INPUT"
            if btn_board.is_clicked(event): state = "LEADERBOARD"
            if btn_settings.is_clicked(event): state = "SETTINGS"
            if btn_quit.is_clicked(event): running = False
        
        elif state == "NAME_INPUT":
            name_input.handle_event(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                active_player_name = name_input.text if name_input.text else "Player"
                reset_session()
                state = "PLAY"

        elif state == "PLAY":
            if event.type == ENEMY_EVENT:
                e = Enemy(user_settings["difficulty"])
                e.speed += current_level * 0.5
                if not pygame.sprite.spritecollideany(e, enemies):
                    all_sprites.add(e); enemies.add(e)
            if event.type == COIN_EVENT:
                c = GameCoin()
                all_sprites.add(c); coins.add(c)

        elif state in ["LEADERBOARD", "SETTINGS"]:
            if btn_back.is_clicked(event): state = "MENU"

        elif state == "GAMEOVER":
            if btn_retry.is_clicked(event):
                reset_session()
                state = "PLAY"
            if btn_menu.is_clicked(event): state = "MENU"

    # --- Отрисовка экранов ---
    if state == "MENU":
        btn_play.draw(screen); btn_board.draw(screen)
        btn_settings.draw(screen); btn_quit.draw(screen)
        
    elif state == "NAME_INPUT":
        screen.blit(font.render("Who is the driver?", True, (255,255,255)), (180, 200))
        name_input.draw(screen)

    elif state == "PLAY":
        all_sprites.update()
        
        # Логика прогрессии[cite: 3, 5]
        keys = pygame.key.get_pressed()
        move_mod = 0.08 if keys[pygame.K_UP] else -0.04 if keys[pygame.K_DOWN] else 0
        
        distance += max(0.02, (0.1 + move_mod))
        score += 0.2
        level_xp += 1

        if level_xp >= (XP_THRESHOLD * current_level):
            current_level += 1
            level_xp = 0
            for e in enemies: e.speed += 1
        
        # Обработка столкновений[cite: 3]
        if not player_car.shield_active:
            if pygame.sprite.spritecollideany(player_car, enemies):
                if snd_crash: snd_crash.play()
                pygame.mixer.music.stop()
                save_score(active_player_name, int(score), int(distance))
                state = "GAMEOVER"

        # Сбор монеток[cite: 3, 5]
        for coin in pygame.sprite.spritecollide(player_car, coins, True):
            score += coin.value * 10
            for e in enemies: e.speed += 0.2

        all_sprites.draw(screen)
        
        # HUD индикаторы
        screen.blit(font.render(f"Score: {int(score)}", True, (255,255,255)), (15, 15))
        screen.blit(font.render(f"LVL: {current_level}", True, (255,255,255)), (15, 45))

    elif state == "LEADERBOARD":
        screen.fill((30, 30, 30))
        board = load_leaderboard()
        for i, entry in enumerate(board[:10]):
            txt = f"{i+1}. {entry['name']} - {entry['score']}"
            screen.blit(font.render(txt, True, (255,255,255)), (150, 50 + i*35))
        btn_back.draw(screen)

    elif state == "GAMEOVER":
        screen.fill((0, 0, 0))
        screen.blit(font.render(f"GAME OVER! Score: {int(score)}", True, (255, 0, 0)), (180, 200))
        btn_retry.draw(screen); btn_menu.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()