#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen on the board."""
    for i in range(row):
        if (board[i] == col
                or board[i] - i == col - row
                or board[i] + i == col + row):
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """Recursively solve the N-queens problem."""
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1


def print_solution(solution):
    """Print a single solution."""
    formatted_solution = []
    for row in solution:
        formatted_solution.append([solution.index(row), row])
    print(formatted_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    for solution in solutions:
        print_solution(solution)
