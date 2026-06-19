import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Simulator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (30, 120, 30)

dice_values = [1, 1]
dice_size = 200
font = pygame.font.SysFont(None, 40)

PIP_POSITIONS = {
    1: [(0.5, 0.5)],
    2: [(0.25, 0.25), (0.75, 0.75)],
    3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)],
    4: [(0.25, 0.25), (0.75, 0.25), (0.25, 0.75), (0.75, 0.75)],
    5: [(0.25, 0.25), (0.75, 0.25), (0.5, 0.5), (0.25, 0.75), (0.75, 0.75)],
    6: [(0.25, 0.25), (0.75, 0.25), (0.25, 0.5), (0.75, 0.5), (0.25, 0.75), (0.75, 0.75)],
}

def draw_die(value, x, y):
    pygame.draw.rect(screen, WHITE, (x, y, dice_size, dice_size), border_radius=20)
    pygame.draw.rect(screen, BLACK, (x, y, dice_size, dice_size), 4, border_radius=20)
    for (px, py) in PIP_POSITIONS[value]:
        cx = int(x + px * dice_size)
        cy = int(y + py * dice_size)
        pygame.draw.circle(screen, BLACK, (cx, cy), 14)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            dice_values = [random.randint(1, 6), random.randint(1, 6)]

    gap = 40
    total_width = dice_size * 2 + gap
    start_x = (WIDTH - total_width) // 2
    die_y = (HEIGHT - dice_size) // 2

    draw_die(dice_values[0], start_x, die_y)
    draw_die(dice_values[1], start_x + dice_size + gap, die_y)

    hint = font.render("Press SPACE to roll", True, WHITE)
    screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 30))

    total = font.render(f"Total: {sum(dice_values)}", True, WHITE)
    screen.blit(total, (WIDTH // 2 - total.get_width() // 2, HEIGHT - 60))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()