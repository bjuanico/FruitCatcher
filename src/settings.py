# settings.py

import os

# Game settings
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)

# Asset directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, '..', 'assets')
IMAGE_DIR = os.path.join(ASSET_DIR, 'images')
SOUND_DIR = os.path.join(ASSET_DIR, 'sounds')
