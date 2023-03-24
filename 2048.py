import pygame
import random

# Define the size of the grid and the size of each tile
GRID_SIZE = 4
TILE_SIZE = 100

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen_size = (GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE)
screen = pygame.display.set_mode(screen_size)

# Set the title of the window
pygame.display.set_caption("2048")

# Load the font for the score
font = pygame.font.SysFont('Arial', 32)

# Define the game grid
grid = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

# Add two initial tiles to the grid
for i in range(2):
    x = random.randint(0, GRID_SIZE - 1)
    y = random.randint(0, GRID_SIZE - 1)
    grid[y][x] = 2

# Define a function to draw the game grid
def draw_grid():
    screen.fill(BLACK)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 3)
            if grid[y][x] > 0:
                text = font.render(str(grid[y][x]), True, WHITE)
                text_rect = text.get_rect()
                text_rect.center = rect.center
                screen.blit(text, text_rect)

# Define a function to add a new tile to the grid
def add_tile():
    empty_cells = []
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] == 0:
                empty_cells.append((x, y))
    if len(empty_cells) > 0:
        x, y = random.choice(empty_cells)
        grid[y][x] = 2

# Define a function to merge the tiles in a row or column
def merge_tiles(line):
    merged = [False for x in range(GRID_SIZE)]
    for i in range(GRID_SIZE - 1):
        if line[i] == line[i+1] and not merged[i] and not merged[i+1]:
            line[i] *= 2
            line[i+1] = 0
            merged[i] = True
    return line

# Define a function to move the tiles in a row or column
def move_tiles(line):
    new_line = [x for x in line if x > 0]
    while len(new_line) < GRID_SIZE:
        new_line.append(0)
    return new_line

# Define a function to rotate the grid
def rotate_grid(grid):
    new_grid = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            new_grid[x][GRID_SIZE - y - 1] = grid[y][x]
    return new_grid

# Define a function to move the tiles up
def move_up():
    global grid
    for x in range(GRID_SIZE):
        line = [grid[y][x] for y in range(GRID_SIZE)]
        merged_line = merge_tiles(line)
        new_line = move_tiles(merged_line)
        for y in range(GRID_SIZE):
            grid[y][x] = new_line[y]
    add_tile()

# Define a function to move the tiles down
def move_down():
    global grid
    for x in range(GRID_SIZE):
        line = [grid[y][x] for y in range(GRID_SIZE)]
        line.reverse()
        merged_line = merge_tiles(line)
        new_line = move_tiles(merged_line)
        new_line.reverse()
        for y in range(GRID_SIZE):
            grid[y][x] = new_line[y]
    add_tile()

# Define a function to move the tiles left
def move_left():
    global grid
    for y in range(GRID_SIZE):
        line = [grid[y][x] for x in range(GRID_SIZE)]
        merged_line = merge_tiles(line)
        new_line = move_tiles(merged_line)
        for x in range(GRID_SIZE):
            grid[y][x] = new_line[x]
    add_tile()

# Define a function to move the tiles right
def move_right():
    global grid
    for y in range(GRID_SIZE):
        line = [grid[y][x] for x in range(GRID_SIZE)]
        line.reverse()
        merged_line = merge_tiles(line)
        new_line = move_tiles(merged_line)
        new_line.reverse()
        for x in range(GRID_SIZE):
            grid[y][x] = new_line[x]
    add_tile()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up()
            elif event.key == pygame.K_DOWN:
                move_down()
            elif event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
