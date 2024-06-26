# tetris.py
import pygame
import random
from settings import *

class Tetromino:
    shapes = [
        [[1, 1, 1, 1]],
        [[1, 1], [1, 1]],
        [[0, 1, 0], [1, 1, 1]],
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1, 1], [1, 1, 0]],
        [[1, 1, 1], [0, 0, 1]],
        [[1, 1, 1], [1, 0, 0]]
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(Tetromino.shapes)
        self.color = random.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Tetris:
    def __init__(self):
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_tetromino = Tetromino(GRID_WIDTH // 2 - 1, 0)
        self.next_tetromino = Tetromino(GRID_WIDTH // 2 - 1, 0)
        self.score = 0
        self.level = 1
        self.game_over = False
        self.lines_cleared = 0

    def draw_grid(self, screen):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = self.grid[y][x]
                pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    def draw_tetromino(self, screen, tetromino):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, tetromino.color, ((tetromino.x + x) * GRID_SIZE, (tetromino.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    def draw_side_panel(self, screen):
        font = pygame.font.SysFont(FONT_NAME, 24)
        next_text = font.render("Next:", True, WHITE)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        level_text = font.render(f"Level: {self.level}", True, WHITE)
        lines_text = font.render(f"Lines: {self.lines_cleared}", True, WHITE)
        screen.blit(next_text, (SCREEN_WIDTH + 10, 20))
        screen.blit(score_text, (SCREEN_WIDTH + 10, 100))
        screen.blit(level_text, (SCREEN_WIDTH + 10, 140))
        screen.blit(lines_text, (SCREEN_WIDTH + 10, 180))
        self.draw_tetromino(screen, self.next_tetromino)

    def can_move(self, dx, dy, shape=None):
        shape = shape or self.current_tetromino.shape
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_tetromino.x + x + dx
                    new_y = self.current_tetromino.y + y + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return False
                    if new_y >= 0 and self.grid[new_y][new_x] != BLACK:
                        return False
        return True

    def lock_tetromino(self):
        for y, row in enumerate(self.current_tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_tetromino.y + y][self.current_tetromino.x + x] = self.current_tetromino.color
        self.clear_lines()
        self.current_tetromino = self.next_tetromino
        self.next_tetromino = Tetromino(GRID_WIDTH // 2 - 1, 0)
        if not self.can_move(0, 0):
            self.game_over = True

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == BLACK for cell in row)]
        lines_cleared = GRID_HEIGHT - len(new_grid)
        self.lines_cleared += lines_cleared
        self.score += lines_cleared * 100 * self.level
        new_grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(lines_cleared)] + new_grid
        self.grid = new_grid
        if lines_cleared:
            self.level += 1

    def update(self):
        if self.can_move(0, 1):
            self.current_tetromino.y += 1
        else:
            self.lock_tetromino()

    def move(self, dx):
        if self.can_move(dx, 0):
            self.current_tetromino.x += dx

    def rotate(self):
        rotated_shape = [list(row) for row in zip(*self.current_tetromino.shape[::-1])]
        if self.can_move(0, 0, rotated_shape):
            self.current_tetromino.rotate()
