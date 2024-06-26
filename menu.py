import pygame
from settings import *

class Button:
    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont(FONT_NAME, font)
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True
        return False

def main_menu(screen):
    start_button = Button("Start", (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50), 50, bg="navy")
    exit_button = Button("Exit", (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50), 50, bg="navy")

    running = True
    while running:
        screen.fill(BLACK)
        start_button.show(screen)
        exit_button.show(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if start_button.click(event):
                return "start"
            if exit_button.click(event):
                pygame.quit()
                exit()
