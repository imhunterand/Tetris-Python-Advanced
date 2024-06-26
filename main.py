# main.py
import pygame
from tetris import Tetris
from settings import *
from menu.py import main_menu
from sound.py import load_sounds, play_sound, play_music, stop_music
from score.py import load_high_scores, save_high_scores, add_score

def draw_game_over(screen):
    font = pygame.font.SysFont(FONT_NAME, 72)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    sounds = load_sounds()
    play_music(sounds["background_music"])
    high_scores = load_high_scores()
    
    while True:
        choice = main_menu(screen)
        if choice == "start":
            tetris = Tetris()
            running = True
            while running:
                screen.fill(BLACK)
                tetris.draw_grid(screen)
                tetris.draw_tetromino(screen, tetris.current_tetromino)
                tetris.draw_side_panel(screen)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            tetris.move(-1)
                        elif event.key == pygame.K_RIGHT:
                            tetris.move(1)
                        elif event.key == pygame.K_DOWN:
                            tetris.update()
                        elif event.key == pygame.K_UP:
                            tetris.rotate()
                        elif event.key == pygame.K_p:
                            paused = True
                            while paused:
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                                        paused = False

                tetris.update()
                clock.tick(FPS)
                
                if tetris.game_over:
                    draw_game_over(screen)
                    play_sound(sounds["game_over"])
                    pygame.time.wait(2000)
                    new_score = {"name": "Player", "score": tetris.score}
                    high_scores = add_score(new_score, high_scores)
                    save_high_scores(high_scores)
                    running = False

    pygame.quit()

if __name__ == "__main__":
    main()
