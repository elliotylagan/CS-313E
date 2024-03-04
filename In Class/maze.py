import unittest
# Kick-off function. Given a grid, we want to return a list
# of the coordinates as tuples of our path to the exit
# The start is always the top-left (0, 0), and the exit is the
# always the bottom right (len(grid) - 1, len(grid[0]) - 1) 
def find_path(grid):
    if not grid:
        return None

    path = []
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    if find_path_helper(grid, 0, 0, path, visited):
        return path
    return None

# Returns True if a path is found and false if not.
# Updates the path parameter with the valid path if it's found
# Grid is the maze
# row and col are our coordinates
# path tracks our current path we've taken
# visited is our "map" of where we have already tried.
def find_path_helper(grid, row, col, path, visited):
    #BASE CASES 
    #found exit
    if row == len(grid)-1 and col == len(grid[0]) - 1:
        return True
    #not on grid
    rows, cols = len(grid), len(grid[0])
    if not (0 <= row and row < rows and 0 <= col and 0 < cols):
        return False
    #hit a wall
    if grid[row][col] == 1:
        return False
    #already checked
    if visited[row][col]:
        return False
    
    #continuing next path
    visited[row][col] = True
    path.append((row, col))
    next_turns = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for dr, dc in next_turns:
        if find_path_helper(grid, row + dr, col + dc, path, visited):
            return True
    
    #if reach deadend
    path.pop(len(path) - 1)
    return False


class TestFindPath(unittest.TestCase):
    def test_grid1(self):
        grid = [
            [0, 0, 1],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(find_path(grid), [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])

    def test_grid2(self):
        grid = [
            [0, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 1, 1, 0]
        ]
        self.assertEqual(find_path(grid), [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)])

    def test_grid3(self):
        grid = [
            [0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(find_path(grid), [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])

    def test_grid4(self):
        grid = [
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
        self.assertIsNone(find_path(grid))

if __name__ == '__main__':
    unittest.main()