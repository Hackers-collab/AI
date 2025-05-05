def is_safe(board, row, col):
    # Check if placing a queen at (row, col) is safe
    # 1. Another queen in same col or not
    # 2. Another queen in same diagonal or not in 'top-left to bottom-right'
    # 3. Another queen in the same diagonal or not in 'top-right to bottom-left'
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_backtracking(board, row, n):
    # Base case: all queens are placed
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            if solve_n_queens_backtracking(board, row + 1, n): # try to solve the next row
                return True
            board[row] = -1  # Backtrack if it didn't work remove the queen 
    return False

def print_solution(board, n):
    for row in range(n):
        line = ['Q' if board[row] == col else '.' for col in range(n)]
        print(" ".join(line))

def n_queens_backtracking(n):
    board = [-1] * n  # Initialize board
    if solve_n_queens_backtracking(board, 0, n):
        print_solution(board, n)
    else:
        print("Solution does not exist")

# Main program
n = int(input("Enter a grid size: "))
n_queens_backtracking(n)
