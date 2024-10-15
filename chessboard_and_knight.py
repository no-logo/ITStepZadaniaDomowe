# Task 3
import os


solution = [[-1 for _ in range(8)] for _ in range(8)]

# print board [ ] or [ move number ]
def print_board(board):
    for row in board:
        print(" ".join(f"[{str(cell).replace('-1',' '):2}]" for cell in row))
    print()

#check if move is safe so if it is inside of board and the field was not visited before
def is_safe(x, y, board):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1

# list of tuples all possible moves for the knight
def knight_moves(x, y):
    return [
        (x + 2, y + 1), (x + 2, y - 1),
        (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x + 1, y - 2),
        (x - 1, y + 2), (x - 1, y - 2)
    ]

# count all safe next moves of knight for current board
def count_possible_moves(x, y, board):
    return sum(1 for move in knight_moves(x, y) if is_safe(move[0], move[1], board))

def dfs_knight_tour(x, y, current_step, board, backtrack_count, solution):

    #end condition if it is possible to move form position 62 to field [2,1] then success solution was found
    if current_step == 62:
        if (2, 1) in knight_moves(x, y):
            print("Solution found:")
            print_board(board)
            # copy all moves from board to solution list
            for i in range(8):
                for j in range(8):
                    solution[i][j] = board[i][j]  # Save the solution
            return True
        # if we cant move from position 62 to field [2,1] the solution was not found
        return False
    # moves = all moves
    moves = knight_moves(x, y)
    #sort based on how many next moves are possible for current move the less moves are possible the better
    moves.sort(key=lambda move: count_possible_moves(move[0], move[1], board))

    #list valid moves with number of possible next moves
    valid_moves_with_counts = [
        (next_x, next_y, count_possible_moves(next_x, next_y, board))
        for next_x, next_y in moves if is_safe(next_x, next_y, board)
    ]


    for next_x, next_y, _ in valid_moves_with_counts:
        board[next_x][next_y] = current_step + 1
        print(f'step {current_step + 1}, x = {next_x}, y = {next_y}')
        print_board(board)
        #if we will find solution then return true and end this for loop
        if dfs_knight_tour(next_x, next_y, current_step + 1, board, backtrack_count, solution):
            return True
        #if we won't find solution then go one move back "Backtrack" and try next move from the list valid_moves_with_counts
        board[next_x][next_y] = -1
        backtrack_count[0] += 1
        print(f"Backtracking to ({x}, {y}), backtrack count: {backtrack_count[0]}")

    return False

board = [[-1 for _ in range(8)] for _ in range(8)]
board[0][0] = 0 # start point 0,0
board[2][1] = 63 # last step
board[1][2] = 1  # first step

backtrack_count = [0]

os.system('cls')

print_board(board)
if not dfs_knight_tour(1, 2, 1, board, backtrack_count, solution):
    print("No closed tour found.")
else:
    print("Solution found and saved:")
print_board(solution)