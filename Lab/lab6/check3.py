
import lab06_util
from check2 import ok_to_add
from check2 import print_board

file = input("Enter a file name => ")
board = lab06_util.read_sudoku(file)


def verify_board(board):
    i = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '.':
                return False
    for i in range(len(board)):
        for j in range(len(board)):
            if ok_to_add(i, j, board[i][j], board) == False:
                return False
    return True


print_board(board)
while verify_board(board) == False:
    row = int(input("Enter a row => "))
    column = int(input("Enter a column => "))
    number = input("Enter a number => ")
    if ok_to_add(row, column, number, board) == True:
        board[row - 1][column - 1] = number
        print("Success")
    print_board(board)
    
    
    

