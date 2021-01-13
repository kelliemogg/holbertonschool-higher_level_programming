#!/usr/bin/python3


if (check(board, row, col)):
    for i in range(n):
        print("()\n".format(board[i])

    if (check(board, row, col)):
        #set value of a cell to Q
            board[row][col] = "Q"
    if col = n - 1:
        #go to next row(recurs on row)
        solve(board, n, row + 1, col)
#go to next row if we set a queen
    if board[row]pcol] = "Q":
        solve(board, n, row + 1, col)
#go to next col (recurse on col)
    solve(baord, n, row, col + 1)
    return

def check(board, n, row, col):
    #check if Q exists in row
    if "Q" in board[row]:
        return False
    elif "Q" in board[col]:
    #check if Q exists in diagonal...4 dir?

if __name__ == "__main__":
