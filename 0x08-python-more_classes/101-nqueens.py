#!/usr/bin/python3

def check(board, n, row, col):
    #check if Q exists in row
    if row >= n or col >= n:
        return False
    if "Q" in board[row]:
        return False
    elif "Q" in board[col]:
        return False
    #check if Q exists in diagonal...4 dir?
    else:
        return True

def solve(board, n, row, col):
#base case
#when we reach last col of last row
    if (check(board, row, col)) and row == n - 1:
        board[row][col] = "Q"
        for i in range(n):
             print("()\n".format(board[i]))

    if col == n - 1:
#go to next row(recurs on row)
        solve(board, n, row + 1, 0)
#go to next row if we set a queen
    else:
        if (check(board, n, row, col)):
            board[row][col] = "Q"
#go to next col (recurse on col)
        solve(board, n, row, col + 1)
    return

def n_queens(n):
#check n > 4 & a number ect...
    if n < 4:
        print("N must be at least 4")
        exit(1)

    #create a blank square of size n
    board = [[0 for x in range(n)] for x in range(n)]
    print(board)
    solve(board, n, 0, 0)

# if __name__ == "__main__":
