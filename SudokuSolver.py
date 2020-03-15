# returns a position of cell
def emptyCell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0: return i, j    # return row, column
    return None

# check if the number is valid at the position in the cell
def validResponse(board, position, num):
    row = position[0]
    col = position[1]
    # check row
    for i in range(len(board[0])):
        if board[row][i] == num and col != i: return False
    # check column
    for i in range(len(board)):
        if board[i][col] == num and row != i: return False
    # check cell
    x_axis = row // 3
    y_axis = col // 3
    for i in range(x_axis*3, x_axis*3 + 3):
        for j in range(y_axis*3, y_axis*3 + 3):
            if board[i][j] == num and (i, j) != (row, col): return False
    return True

# The function uses recursion for finding a optimal solution
def solution(board):
    pos = emptyCell(board)
    if pos: row, col = pos
    else: return True

    for num in range(1, 10):
        if validResponse(board, pos, num):
            board[row][col] = num
            if solution(board): return True
            board[row][col] = 0
    return False

# To print the board in sudoku style
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0: print('----------------------')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0: print('| ', end='')
            if j == 8: print(board[i][j])
            else: print(str(board[i][j]) + ' ', end='')


# '0' refer to empty place
sudoku_board = [
    [4,0,0,9,0,0,8,0,1], [0,1,0,8,0,0,0,4,0], [0,8,0,0,0,6,9,0,3],
    [0,0,0,7,0,8,0,3,0], [7,9,0,0,1,0,2,0,0], [0,0,0,2,0,0,0,1,0],
    [9,0,0,0,0,1,3,0,5], [0,0,8,3,0,5,0,0,0], [5,0,0,0,8,0,7,0,6]
]

printBoard(sudoku_board)
print('Solving.................')
solution(sudoku_board)
if emptyCell(sudoku_board) is not None: print('Sudoku is unsolvable')
else:
    print('Solved')
    printBoard(sudoku_board)