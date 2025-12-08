#!/usr/bin/env python3

import copy

fd = open("input.txt", "r")
lines = fd.readlines()
lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines
fd.close()


def determine_next_state(grid, row, col):
  """
  Checks the 8 neighbors of a cell.
  If an '@' cell has less than 4 '@' neighbors, it transforms to 'x'.
  If it has 4 or more '@' neighbors, it remains '@'.
  Returns: (new_character, has_changed_boolean)
  """
  neighbor_count = 0
  # Check 3x3 grid around the cell
  for i in range(row-1, row+2):
    for j in range(col-1, col+2):
      # Boundary checks and skip the cell itself
      if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or (i == row and j == col)):
        continue
      
      # Skip empty floor
      if(grid[i][j] == '.'):
        continue
      # Count occupied neighbors
      elif(grid[i][j] == '@'):
        neighbor_count += 1
        # Optimization: If we hit 4, we know the result immediately
        if neighbor_count >= 4:
          return '@', False # Stays as '@', no change
  
  # If loop finishes, neighbor_count is < 4. The cell changes.
  return 'x', True # Transforms to 'x', change occurred

def can_move(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue

            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    count += 1
    # print(f"Checking cell ({r}, {c}): count = {count}")
    if count < 4 and grid[r][c] == '@':
        return True
    else:
        return False
    
def can_move_with_replace(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue

            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    count += 1
                    # I want to change the '@' to 'X' to avoid double counting
                    # Replace '@' with 'X' to avoid double counting
                    
    #print(f"Checking cell ({r}, {c}): count = {count}")
    if count < 4 and grid[r][c] == '@':
        #print(type(grid[r][c]), type(r), type(c))
        grid[r][c].replace('@','X')
        return True, grid
    else:
        return False, grid

def build_neighbor_count_grid(grid):
    rows = len(grid)
    cols = len(grid[0])

    result = [[0] * cols for _ in range(rows)]
    
    C = 0
    
    my_new_grid = copy.deepcopy(grid)

    for r in range(rows):
        for c in range(cols):
            res = can_move(my_new_grid, r, c)
            if res:
                C += 1
    return C

def build_neighbor_count_grid_w_replace(grid):
    rows = len(grid)
    cols = len(grid[0])

    result = [[0] * cols for _ in range(rows)]
    
    C = 0
    my_new_grid = copy.deepcopy(grid)

    grid_changed = False

    last_row_changed = -1

    changes_in_round = -1

    while changes_in_round != 0:
        changes_in_round = 0
        for r in range(rows):
            for c in range(cols):
                cell = my_new_grid[r][c]
                
                if cell == '.':
                    continue
                elif cell == '@':
                    new_char, changed = determine_next_state(my_new_grid, r, c)
                my_new_grid[r][c] = new_char
                if changed:
                    changes_in_round += 1
        my_new_grid = [inner_list[:] for inner_list in grid]
        c += changes_in_round
        print(f"Changes in this round: {changes_in_round}")              
    return C

counts = build_neighbor_count_grid(lines)
print(counts)
part2_counts = build_neighbor_count_grid_w_replace(lines)
print(part2_counts)
    
