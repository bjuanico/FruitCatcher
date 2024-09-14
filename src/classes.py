# classes.py

import pygame
import random
from settings import WIDTH, HEIGHT
from utils import load_image

class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image('basket.png')
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
        self.speed = 8

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Keep within the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        fruit_images = ['apple.png', 'banana.png', 'orange.png']  # List of fruit images
        self.image = load_image(random.choice(fruit_images))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = load_image('bomb.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()
