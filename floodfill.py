import pygame

# Grid data
grid_data = [
    [1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 1, 0]
]

# Pygame setup
pygame.init()
cell_size = 30
width, height = len(grid_data[0]) * cell_size, len(grid_data) * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Drawing the grid
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    for y, row in enumerate(grid_data):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if cell == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect, 1)  # Draw the grid lines

    pygame.display.flip()

pygame.quit()
