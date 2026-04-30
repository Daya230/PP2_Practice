import pygame

# ---------------- BUTTON ----------------
class Button:
    def __init__(self, x, y, w, h, text,
                 color=(60, 60, 60),
                 hover_color=(90, 90, 90),
                 text_color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 34)

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse)

        # shadow
        shadow_rect = self.rect.move(3, 3)
        pygame.draw.rect(surface, (0, 0, 0), shadow_rect, border_radius=10)

        # main button
        color = self.hover_color if is_hover else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)

        # border
        pygame.draw.rect(surface, (120, 120, 120), self.rect, 2, border_radius=10)

        # text
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )


# ---------------- TEXT INPUT ----------------
class TextInput:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ""
        self.font = pygame.font.Font(None, 32)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isprintable() and len(self.text) < 15:
                self.text += event.unicode

    def draw(self, surface):
        # background
        bg = (30, 30, 30) if self.active else (20, 20, 20)
        pygame.draw.rect(surface, bg, self.rect, border_radius=8)

        # border
        border = (0, 200, 255) if self.active else (80, 80, 80)
        pygame.draw.rect(surface, border, self.rect, 2, border_radius=8)

        # text
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surf, (self.rect.x + 10, self.rect.y + 8))