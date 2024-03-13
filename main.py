sample_board = [
    [8,0,1,0,0,0,0,0,0],
    [2,5,0,0,7,0,0,9,0],
    [0,4,0,0,0,8,0,2,6],
    [0,0,7,8,0,5,0,1,3],
    [0,0,5,0,4,3,0,0,7],
    [0,0,3,7,9,0,0,0,4],
    [0,9,0,4,0,7,0,6,2],
    [1,0,0,5,8,6,0,7,9],
    [0,6,4,0,1,2,0,0,0]
]

# Print out the soduku board with "dividers"
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
                
def check_board_valid(board, number, position):
    # Check row (loop every sinlge column, in the given row)
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Check column
     for i in range(len(bo[0])):
        if bo[i][position[1] == num and position[0] != i:
            return False

    # Check "box" - 9 box in total
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Loop through "boxes"
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False

    return True


# print_board(sample_board)

def find_empty_squares(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if bo[i][j] == 0:
                return (i,j)   # row, col