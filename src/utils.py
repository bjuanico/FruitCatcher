# utils.py

import os
import pygame
from settings import IMAGE_DIR, SOUND_DIR

def load_image(name):
    fullname = os.path.join(IMAGE_DIR, name)
    try:
        image = pygame.image.load(fullname)
        return image.convert_alpha()
    except pygame.error as message:
        print(f'Cannot load image: {name}')
        raise SystemExit(message)

def load_sound(name):
    fullname = os.path.join(SOUND_DIR, name)
    try:
        sound = pygame.mixer.Sound(fullname)
        return sound
    except pygame.error as message:
        print(f'Cannot load sound: {name}')
        return None
