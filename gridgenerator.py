import random

def generate_grid(n, start_row, start_col, end_row, end_col):
    grid = [['.' for _ in range(n)] for _ in range(n)]
    grid[start_row][start_col] = 'S'
    grid[end_row][end_col] = 'T'
    path = []
    current_row, current_col = start_row, start_col
    while current_row != end_row or current_col != end_col:
        if current_row < end_row:
            current_row += 1
        elif current_row > end_row:
            current_row -= 1
        if current_col < end_col:
            current_col += 1
        elif current_col > end_col:
            current_col -= 1
        path.append((current_row, current_col))

    wall_count = 0
    while wall_count < n * n // 4: 
        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)
        if (row, col) not in path and (row, col) != (start_row, start_col) and (row, col) != (end_row, end_col):
            grid[row][col] = '#'
            wall_count += 1

    return grid

import random
n=int(input())
WALL_COLOR = '\033[30;47m'  # Black text on white background
START_COLOR = '\033[32;47m'  # Green text on white background
END_COLOR = '\033[31;47m'  # Red text on white background
EMPTY_COLOR = '\033[34;47m'  # Blue text on white background
RESET_COLOR = '\033[0m'

# Generate a grid
grid = generate_grid(n, 0, 0, n - 1, n - 1)

# Draw the grid
def draw_grid():
    for row in range(n):
        for col in range(n):
            cell = grid[row][col]
            if cell == '#':
                print(WALL_COLOR + '██' + RESET_COLOR, end='')
            elif cell == 'S':
                print(START_COLOR + '██' + RESET_COLOR, end='')
            elif cell == 'T':
                print(END_COLOR + '██' + RESET_COLOR, end='')
            else:
                print(EMPTY_COLOR + '░░' + RESET_COLOR, end='')
        print()

# Draw the grid
draw_grid()


# grid = generate_grid(10, 0, 0, 9, 9)
# for row in grid:
#     print(''.join(row))
