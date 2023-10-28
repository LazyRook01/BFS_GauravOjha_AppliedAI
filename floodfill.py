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
BLUE = (0, 0, 255)

# Flood Fill function
def flood_fill_iterative(start_x, start_y, target_color, replacement_color):
    stack = [(start_x, start_y)]
    while stack:
        x, y = stack.pop()
        if grid_data[y][x] == target_color:
            grid_data[y][x] = replacement_color
            if x > 0:
                stack.append((x - 1, y))
            if x < len(grid_data[0]) - 1:
                stack.append((x + 1, y))
            if y > 0:
                stack.append((x, y - 1))
            if y < len(grid_data) - 1:
                stack.append((x, y + 1))

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

    # Perform flood fill on click event
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        click_x, click_y = mouse_pos[0] // cell_size, mouse_pos[1] // cell_size
        target_color = grid_data[click_y][click_x]
        flood_fill_iterative(click_x, click_y, target_color, 2)  # 2 represents the replacement color, here blue

    for y, row in enumerate(grid_data):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if cell == 1:
                pygame.draw.rect(screen, BLACK, rect)
            elif cell == 2:
                pygame.draw.rect(screen, BLUE, rect)  # Fill with blue color for flooded region
            else:
                pygame.draw.rect(screen, WHITE, rect, 1)  # Draw the grid lines

    pygame.display.flip()

pygame.quit()
