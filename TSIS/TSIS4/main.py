import pygame
import sys
import random
from config import *
from db import init_db, get_top_scores
from game import run_game

# Базовая инициализация
pygame.init()
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Pro: Neon Edition") # Изменили название

# Подготовка шрифтов (имена переменных изменены)
ui_font = pygame.font.SysFont("Verdana", 22)
header_font = pygame.font.SysFont("Verdana", 44, bold=True)
caption_font = pygame.font.SysFont("Verdana", 16)

class MenuButton: # Переименовали класс
    def __init__(self, pos_x, pos_y, width, height, label, theme_color=GRAY):
        self.area = pygame.Rect(pos_x, pos_y, width, height)
        self.label = label
        self.base_theme = theme_color

    def render(self, surface): # Переименовали метод draw
        cursor = pygame.mouse.get_pos()
        # Изменили логику подбора цветов
        if self.area.collidepoint(cursor):
            bg_fill = (255, 150, 180)  # Мягкий розовый при наведении
            edge_color = (255, 80, 150)
        else:
            bg_fill = (230, 20, 120)   # Насыщенный розовый в покое
            edge_color = (255, 180, 210)

        # Рисуем кнопку с более выраженным скруглением
        pygame.draw.rect(surface, bg_fill, self.area, border_radius=18)
        pygame.draw.rect(surface, edge_color, self.area, width=3, border_radius=18)
        
        # Отрисовка надписи
        text_render = ui_font.render(self.label, True, (255, 255, 255))
        text_place = text_render.get_rect(center=self.area.center)
        surface.blit(text_render, text_place)

    def was_pressed(self, event_obj): # Переименовали is_clicked
        if event_obj.type == pygame.MOUSEBUTTONDOWN and event_obj.button == 1:
            return self.area.collidepoint(event_obj.pos)
        return False

def show_message(msg, font_obj, color_val, y_offset): # Переименовали draw_text
    surface = font_obj.render(msg, True, color_val)
    display_surface.blit(surface, surface.get_rect(center=(WIDTH // 2, y_offset)))

def login_screen(): # Переименовали ask_username
    name_input = ""
    while True:
        display_surface.fill(BLACK)
        show_message("IDENTIFY YOURSELF", ui_font, (255, 100, 200), 200)
        
        # Поле ввода в стиле "мягкий квадрат"
        entry_box = pygame.Rect(WIDTH//2 - 140, 250, 280, 45)
        pygame.draw.rect(display_surface, (30, 30, 30), entry_box, border_radius=10)
        show_message(name_input + "_", ui_font, WHITE, 272)
        
        show_message("Press Enter to Confirm", caption_font, GRAY, 340)
        
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return None
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and name_input: return name_input
                elif e.key == pygame.K_BACKSPACE: name_input = name_input[:-1]
                elif len(name_input) < 12: name_input += e.unicode

def start_menu(): # Переименовали main_menu
    # Кнопки с новыми названиями и структурой
    play_opt = MenuButton(200, 200, 200, 50, "START GAME")
    rank_opt = MenuButton(200, 270, 200, 50, "HALL OF FAME")
    cfg_opt = MenuButton(200, 340, 200, 50, "PREFERENCES")
    exit_opt = MenuButton(200, 410, 200, 50, "EXIT GAME")

    while True:
        display_surface.fill((10, 10, 15)) # Немного изменили цвет фона
        show_message("SNAKE ADVENTURE", header_font, WHITE, 100)
        
        for option in [play_opt, rank_opt, cfg_opt, exit_opt]: 
            option.render(display_surface)
        
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT or exit_opt.was_pressed(e): return "quit"
            if play_opt.was_pressed(e): return "play"
            if rank_opt.was_pressed(e): return "leaderboard"
            if cfg_opt.was_pressed(e): return "settings"

def leaderboard_view(): # Изменено название
    data_rows = get_top_scores()
    back_btn = MenuButton(200, 520, 200, 40, "GO BACK")
    
    while True:
        display_surface.fill(BLACK)
        show_message("BEST SCORES", ui_font, (255, 200, 0), 50)
        
        v_offset = 120
        for pos, (user, pts, level, timestamp) in enumerate(data_rows):
            line = f"#{pos+1} {user[:10]} - {pts} pts (Lvl {level})"
            show_message(line, caption_font, WHITE, v_offset)
            v_offset += 35
            
        back_btn.render(display_surface)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return "quit"
            if back_btn.was_pressed(e): return "menu"

def settings_view(): # Изменено название
    cfg = load_settings()
    grid_btn = MenuButton(150, 200, 300, 50, f"GRID RENDERING: {'ON' if cfg['grid'] else 'OFF'}")
    skin_btn = MenuButton(150, 270, 300, 50, "RANDOMIZE SKIN")
    exit_btn = MenuButton(200, 400, 200, 50, "APPLY & EXIT")

    while True:
        display_surface.fill(BLACK)
        show_message("GAME CONFIG", ui_font, (100, 150, 255), 100)
        
        # Превью цвета змейки (теперь с обводкой)
        preview_rect = (WIDTH//2 - 20, 330, 40, 40)
        pygame.draw.rect(display_surface, cfg['snake_color'], preview_rect, border_radius=8)
        pygame.draw.rect(display_surface, WHITE, preview_rect, 1, border_radius=8)
        
        for ctrl in [grid_btn, skin_btn, exit_btn]: ctrl.render(display_surface)
        
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return "quit"
            if grid_btn.was_pressed(e):
                cfg['grid'] = not cfg['grid']
                grid_btn.label = f"GRID RENDERING: {'ON' if cfg['grid'] else 'OFF'}"
            if skin_btn.was_pressed(e):
                cfg['snake_color'] = [random.randint(60, 255) for _ in range(3)]
            if exit_btn.was_pressed(e):
                save_settings(cfg)
                return "menu"

def end_game_view(stats): # Изменено название
    retry_btn = MenuButton(100, 400, 180, 50, "TRY AGAIN")
    home_btn = MenuButton(320, 400, 180, 50, "TO MENU")

    while True:
        display_surface.fill((20, 0, 0))
        show_message("SESSION ENDED", header_font, (255, 50, 50), 150)
        show_message(f"Final Score: {stats['score']}", ui_font, WHITE, 230)
        show_message(f"Best: {stats['best']}", ui_font, (255, 200, 0), 300)
        
        retry_btn.render(display_surface)
        home_btn.render(display_surface)
        
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return "quit"
            if retry_btn.was_pressed(e): return "retry"
            if home_btn.was_pressed(e): return "menu"

def run_app(): # Переименовали main()
    try:
        init_db()
    except Exception as db_err:
        print(f"Database connection failed: {db_err}")

    active = True
    while active:
        action = start_menu()
        
        if action == "quit": 
            active = False
        elif action == "leaderboard": 
            leaderboard_view()
        elif action == "settings": 
            settings_view()
        elif action == "play":
            current_user = login_screen()
            if not current_user: continue
            
            gaming = True
            while gaming:
                status, info = run_game(display_surface, current_user, load_settings())
                if status == "quit": 
                    pygame.quit()
                    sys.exit()
                
                decision = end_game_view(info)
                if decision == "retry": continue
                gaming = False

    pygame.quit()

if __name__ == "__main__":
    run_app()