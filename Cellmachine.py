import pygame
import numpy as np

# Settings
CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cell Machine - Conway's Game of Life")
clock = pygame.time.Clock()

def update_grid(grid):
    new_grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = np.sum(grid[max(0,y-1):min(GRID_HEIGHT,y+2), max(0,x-1):min(GRID_WIDTH,x+2)]) - grid[y,x]
            if grid[y,x] == 1 and neighbors in [2, 3]:
                new_grid[y,x] = 1
            elif grid[y,x] == 0 and neighbors == 3:
                new_grid[y,x] = 1
    return new_grid

def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = GREEN if grid[y,x] == 1 else BLACK
            pygame.draw.rect(screen, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1))

def main():
    grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
    running = True
    paused = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Toggle pause with space bar
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_c:
                    grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)  # Clear grid

            # Toggle cells on click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_y, grid_x = y // CELL_SIZE, x // CELL_SIZE
                grid[grid_y, grid_x] = 1 - grid[grid_y, grid_x]

        if not paused:
            grid = update_grid(grid)

        draw_grid(grid)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
