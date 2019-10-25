"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is 
surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

    Input:
    11110
    11010
    11000
    00000

    Output: 1

    Example 2:

    Input:
    11000
    11000
    00100
    00011

    Output: 3

"""


def number_of_islands(matrix):

    if not in matrix:
        return 0

    visited = set()

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    number_of_islands = 0

    def traverse(i, j):

        if (i, j) in visited:
            return

        visited.add((i, j))

        if matrix[i][j] == '0':
            return

        for dir in directions:

            next_i, next_j = i + dir[0], j + dir[1]
            # if `0`, add to visited and continue
            if 0 <= next_i < rows and 0 <= next_j < cols:
                if matrix[next_i][next_j] == '0':
                    continue
                else:
                    traverse(next_i, next_j)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1' and (i, j) not in visited:
                number_of_islands += 1
            traverse(i, j)

    return number_of_islands


matrix = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
ans = number_of_islands(matrix)
print(ans)
