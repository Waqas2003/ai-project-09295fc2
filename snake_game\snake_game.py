import pygame
import sys
import random
import time

pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
food_pos = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Pygame display
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

    # Validate direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= BLOCK_SIZE
    if direction == 'DOWN':
        snake_pos[1] += BLOCK_SIZE
    if direction == 'LEFT':
        snake_pos[0] -= BLOCK_SIZE
    if direction == 'RIGHT':
        snake_pos[0] += BLOCK_SIZE

    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Food spawn
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
        food_spawn = True

    # GFX
    game_window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(game_window, WHITE, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - BLOCK_SIZE:
        pygame.quit()
        sys.exit()
    if snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - BLOCK_SIZE:
        pygame.quit()
        sys.exit()

    # Self hit
    for block in snake_body[1:]:
        if snake_pos == block:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    time.sleep(SPEED / 1000)