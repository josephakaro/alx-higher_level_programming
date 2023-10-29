#!/usr/bin/python3


def check(board, n, row, col):

    if row >= n or col >= n:
        return False
    if "Q" in board[row]:
        return False
    elif "Q" in board[col]:
        return False
    else:
        return True


def solve(board, n, row, col):

    if (check(board, n, row, col)) and row == n - 1:
        board[row][col] = "Q"
        for i in range(n):
            print("()\n".format(board[i]))
        return False

    if col == n - 1:
        solve(board, n, row + 1, 0)
    else:
        if (check(board, n, row, col)):
            board[row][col] = "Q"
        solve(board, n, row, col + 1)
    return


def n_queens(n):

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for x in range(n)] for x in range(n)]
    print(board)
    solve(board, n, 0, 0)

if __name__ == "__main__":

    n_queens(4)
