#!/usr/bin/python3
""" This function finds the perimeter of the island """


def island_perimeter(grid):
    """ The function that does the job """
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell initially contributes 4 sides

                # Check adjacent cells (up, down, left, right)
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 2  # Reduce 2 sides if adjacent cell is land
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 2  # Reduce 2 sides if adjacent cell is land

    return perimeter
