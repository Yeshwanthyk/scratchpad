def max_area_island(grid):

    max_area = 0

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                area = [0]
                traverse(grid, area, row, col)
                max_area = max(max_area, area[0])

    return max_area


def traverse(grid, area, row, col):

    if not (0 <= row < len(grid) and 0 <= col < len(grid)) or grid[row][col] != 1:
        return

    area[0] += 1
    grid[row][col] = '#'

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dir in dirs:
        traverse(grid, area, row + dir[0], col + dir[1])


grid = [[0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
ans = max_area_island(grid)
print(ans)
