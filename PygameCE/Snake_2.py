import pygame
import random

pygame.init()

# настройки
WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# цвета
BLACK = (20, 20, 20)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 24)

def reset_game():
    snake = [(100, 100), (80, 100), (60, 100)]
    dx, dy = CELL, 0
    food = (random.randrange(0, WIDTH, CELL),
            random.randrange(0, HEIGHT, CELL))
    score = 0
    return snake, dx, dy, food, score


snake, dx, dy, food, score = reset_game()

running = True
game_over = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                snake, dx, dy, food, score = reset_game()
                game_over = False

    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_UP] and dy == 0:
            dx, dy = 0, -CELL
        if keys[pygame.K_DOWN] and dy == 0:
            dx, dy = 0, CELL
        if keys[pygame.K_LEFT] and dx == 0:
            dx, dy = -CELL, 0
        if keys[pygame.K_RIGHT] and dx == 0:
            dx, dy = CELL, 0

        head = (snake[0][0] + dx, snake[0][1] + dy)
        snake.insert(0, head)

        if head == food:
            score += 1
            food = (random.randrange(0, WIDTH, CELL),
                    random.randrange(0, HEIGHT, CELL))
        else:
            snake.pop()

        # столкновения
        if (head in snake[1:] or
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT):
            game_over = True

    # рисование
    screen.fill(BLACK)

    # змейка
    for segment in snake:
        pygame.draw.rect(screen, GREEN,
                         (segment[0], segment[1], CELL, CELL))

    # еда
    pygame.draw.rect(screen, RED,
                     (food[0], food[1], CELL, CELL))

    # счёт
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # game over
    if game_over:
        text1 = font.render("GAME OVER", True, WHITE)
        text2 = font.render("Press SPACE to restart", True, WHITE)

        screen.blit(text1, (WIDTH // 2 - 80, HEIGHT // 2 - 30))
        screen.blit(text2, (WIDTH // 2 - 140, HEIGHT // 2 + 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()