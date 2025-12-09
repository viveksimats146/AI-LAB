# Knight's Tour using Backtracking

# Possible knight moves (x, y)
moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def is_safe(x, y, board, N):
    """Check if (x, y) is valid and unvisited."""
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def solve_knight_tour(N, start_x=0, start_y=0):
    """Attempts to solve the Knight's Tour problem from (start_x, start_y)."""
    
    # Initialize N×N board with -1 meaning unvisited
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[start_x][start_y] = 0  # starting position is step 0

    if knight_tour_util(start_x, start_y, 1, board, N):
        print("Knight's Tour found!")
        print_board(board)
    else:
        print("No Knight's Tour exists for this starting position.")

def knight_tour_util(x, y, move_count, board, N):
    """Recursive helper to perform backtracking."""
    # If all squares have been visited, tour is complete
    if move_count == N * N:
        return True

    # Try all possible knight moves
    for dx, dy in moves:
        next_x, next_y = x + dx, y + dy

        if is_safe(next_x, next_y, board, N):
            board[next_x][next_y] = move_count  # make move

            # Recursively attempt next steps
            if knight_tour_util(next_x, next_y, move_count + 1, board, N):
                return True

            # Backtracking: undo move
            board[next_x][next_y] = -1  

    return False  # no valid moves

def print_board(board):
    """Pretty prints the board."""
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))
    print()

# Run example
if __name__ == "__main__":
    N = 8  # Size of chessboard
    start_x, start_y = 0, 0
    solve_knight_tour(N, start_x, start_y)
