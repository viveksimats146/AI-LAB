# --------------------------
# Sudoku Solver (50 lines)
# --------------------------
def print_grid(grid):
    for row in grid:
        print(" ".join(str(n) for n in row))
def find_empty(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                return r,c
    return None
def is_valid(grid,r,c,num):
    if any(grid[r][x]==num for x in range(9)): return False
    if any(grid[x][c]==num for x in range(9)): return False
    sr,sc = 3*(r//3),3*(c//3)
    for i in range(sr,sr+3):
        for j in range(sc,sc+3):
            if grid[i][j]==num: return False
    return True
def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty: return True
    r,c = empty
    for num in range(1,10):
        if is_valid(grid,r,c,num):
            grid[r][c]=num
            if solve_sudoku(grid): return True
            grid[r][c]=0
    return False
# --------------------------
# Example Sudoku Puzzle
# --------------------------
grid=[
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]
# --------------------------
# Solve and Print
# --------------------------
if solve_sudoku(grid):
    print("Solved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists.")
