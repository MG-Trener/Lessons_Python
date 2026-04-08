import pygame
import random

pygame.init()

# размеры окна
WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# змейка
snake = [(100, 100), (80, 100), (60, 100)]
dx, dy = CELL, 0

# еда
food = (random.randrange(0, WIDTH, CELL),
        random.randrange(0, HEIGHT, CELL))

running = True

while running:
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -CELL
    if keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, CELL
    if keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -CELL, 0
    if keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = CELL, 0

    # движение змейки
    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    # съела еду?
    if head == food:
        food = (random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL))
    else:
        snake.pop()

    # проверка столкновений
    if (head in snake[1:] or
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT):
        running = False

    # рисуем
    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(screen, GREEN,
                         (segment[0], segment[1], CELL, CELL))

    pygame.draw.rect(screen, RED,
                     (food[0], food[1], CELL, CELL))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()