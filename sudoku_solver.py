def IsValid(grid, row, col, number):
    for i in range(9):
        if grid[row][i] == number:
            return False
    for j in range(9):
        if grid[j][col] == number:
            return False
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
    return True

def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    for num in range(1, 10):
        if IsValid(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
            grid[row][col] = 0
    return False
grid = [[]]
while (len(grid) != 9 or len(grid[0]) != 9):
    grid = eval(input("Enter your Sudoku puzzle (9x9) grid: "))
    if (len(grid) != 9 or len(grid[0]) != 9):
        print("Wrong input! Enter again")


if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No solution for this sudoku")
