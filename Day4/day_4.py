# --- Day 4: Lobby - Part 2 ---
file_path = 'input.txt'

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

current_grid=[]
# Read and parse file into a 2D list of characters
with open(file_path, 'r') as f:
  content = f.read().split()
  # Convert list of strings into list of lists (mutable grid)
  for item in content:
    current_grid.append(list(item))

# Create a deep copy for the next generation's state
next_grid = [inner_list[:] for inner_list in current_grid]
changes_in_round = -1
total_changes = 0

# Run simulation until the grid stabilizes (no changes in a round)
while changes_in_round != 0:
  changes_in_round = 0
  
  for r in range(len(current_grid)):
    for c in range(len(current_grid[r])):
      cell = current_grid[r][c]
      
      if(cell == '.'):
        continue
      elif(cell == '@'):
        # Calculate what happens to this cell based on current neighbors
        new_char, changed = determine_next_state(current_grid, r, c)
        next_grid[r][c] = new_char
        
        if(changed):
          changes_in_round += 1
          
  # Update the current grid to match the calculated next state
  current_grid = [inner_list[:] for inner_list in next_grid]
  total_changes += changes_in_round

print(total_changes)