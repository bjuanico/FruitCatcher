# main.py
import os
import pygame
import random
from settings import WIDTH, HEIGHT, LIGHT_BLUE
from classes import Basket, Fruit, Bomb
from utils import load_sound

# Set the SDL audio driver to 'dummy' to handle audio issues in WSL
os.environ['SDL_AUDIODRIVER'] = 'dummy'

def main():
    pygame.init()

    # Try to initialize the mixer
    try:
        pygame.mixer.init()
        mixer_available = True
    except pygame.error:
        print("Mixer initialization failed, disabling sound.")
        mixer_available = False

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fruit Catcher")
    clock = pygame.time.Clock()

    # Load sounds if mixer is available
    if mixer_available:
        catch_sound = load_sound('catch.wav')
        bomb_sound = load_sound('bomb.wav')
        pygame.mixer.music.load(os.path.join('..', 'assets', 'sounds', 'background_music.wav'))
        pygame.mixer.music.play(-1)  # Loop indefinitely
    else:
        catch_sound = None
        bomb_sound = None

    # Groups
    all_sprites = pygame.sprite.Group()
    fruits = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    basket = Basket()
    all_sprites.add(basket)

    # Score and lives
    score = 0
    lives = 3
    font = pygame.font.SysFont(None, 36)

    # Spawn event
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 1000)  # Adjust spawn rate as needed

    running = True
    while running:
        clock.tick(60)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWN_EVENT:
                x_pos = random.randint(20, WIDTH - 20)
                speed = random.randint(4, 6)
                if random.random() < 0.8:
                    fruit = Fruit(x_pos, 0, speed)
                    all_sprites.add(fruit)
                    fruits.add(fruit)
                else:
                    bomb = Bomb(x_pos, 0, speed)
                    all_sprites.add(bomb)
                    bombs.add(bomb)

        # Update
        basket.update(keys)
        fruits.update()
        bombs.update()

        # Check collisions
        fruit_hits = pygame.sprite.spritecollide(basket, fruits, True)
        for hit in fruit_hits:
            score += 10
            if mixer_available and catch_sound:
                catch_sound.play()

        bomb_hits = pygame.sprite.spritecollide(basket, bombs, True)
        for hit in bomb_hits:
            lives -= 1
            if mixer_available and bomb_sound:
                bomb_sound.play()
            if lives <= 0:
                running = False  # Game over

        # Draw
        screen.fill(LIGHT_BLUE)
        all_sprites.draw(screen)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

