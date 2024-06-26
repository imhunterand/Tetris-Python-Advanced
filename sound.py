import pygame

def load_sounds():
    pygame.mixer.init()
    return {
        "rotate": pygame.mixer.Sound("sounds/rotate.wav"),
        "move": pygame.mixer.Sound("sounds/move.wav"),
        "line_clear": pygame.mixer.Sound("sounds/line_clear.wav"),
        "game_over": pygame.mixer.Sound("sounds/game_over.wav"),
        "background_music": "sounds/background_music.mp3"
    }

def play_sound(sound):
    pygame.mixer.Sound.play(sound)

def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()
