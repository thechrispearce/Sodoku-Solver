"""Empty board:
        [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
"""

board = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]

def solve(brd):

    print(brd)
    blank = check_blk(brd)
    if not blank:
        return True
    else:
        row, col = blank
    for i in range(1,10):
        if validate(i,(row,col),brd):
            brd[row][col] = i

            if solve(brd):
                return True
            brd[row][col] = 0
    return False




def check_blk(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i,j)
    return None


def validate(num,pos,brd):
    # Check column
    for row in range(len(brd)):
        if brd[row][pos[1]] == num and pos[0] != row:
            return False
    # Check row
    for col in range(len(brd[0])):
        if brd[pos[0]][col] == num and pos[1] != col:
            return False
    # Check box
    x_box = pos[1] // 3
    y_box = pos[0] // 3
    for row in range(3 * y_box,3 * y_box + 3):
        for col in range(3 * x_box, 3 * x_box + 3):
            if brd[row][col] == num and (row,col) != pos:
                return False
    return True



for i in range(len(board)):
    print(board[i])
solve(board)
print("                                  ")
print("                                  ")
for i in range(len(board)):
    print(board[i])