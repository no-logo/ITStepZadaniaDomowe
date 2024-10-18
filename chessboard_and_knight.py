# Task 3
import os


solution = [[-1 for _ in range(8)] for _ in range(8)]

# print board [ ] or [ move number ]
def print_board(board):
    for row in board:
        print(" ".join(f"[{str(cell).replace('-1',' '):2}]" for cell in row))
    print()

def change_solution_start_point(board, y, x):
    move_number = board[y][x]

    for i in range(8):
        for j in range(8):
            if board[i][j] - move_number >= 0:
                board[i][j] = board[i][j] - move_number
            else:
                board[i][j] = (63 + board[i][j] + 1) - move_number
    return board


#check if move is safe so if it is inside of board and the field was not visited before
def is_safe(y, x, board):
    return 0 <= y < 8 and 0 <= x < 8 and board[y][x] == -1

# list of tuples all possible moves for the knight
def knight_moves(y, x):
    return [
        (y + 2, x + 1), (y + 2, x - 1),
        (y - 2, x + 1), (y - 2, x - 1),
        (y + 1, x + 2), (y + 1, x - 2),
        (y - 1, x + 2), (y - 1, x - 2)
    ]

# count all safe next moves of knight for current board
def count_possible_moves(y, x, board):
    return sum(1 for move in knight_moves(y, x) if is_safe(move[0], move[1], board))

def dfs_knight_tour(y, x, current_step, board, backtrack_count, solution):

    #end condition if it is possible to move form position 62 to field [2,1] then success solution was found
    if current_step == 62:
        if (2, 1) in knight_moves(y, x):
            #print("Solution found:")
            # copy all moves from board to solution list
            for i in range(8):
                for j in range(8):
                    solution[i][j] = board[i][j]  # Save the solution
            return True
        # if we cant move from position 62 to field [2,1] the solution was not found
        return False
    # moves = all moves
    moves = knight_moves(y, x)
    #sort based on how many next moves are possible for current move the less moves are possible the better
    moves.sort(key=lambda move: count_possible_moves(move[0], move[1], board))

    #list valid moves with number of possible next moves
    valid_moves_with_counts = [
        (next_y, next_x, count_possible_moves(next_y, next_x, board))
        for next_y, next_x in moves if is_safe(next_y, next_x, board)
    ]


    for next_y, next_x, _ in valid_moves_with_counts:
        board[next_y][next_x] = current_step + 1
        #print(f'step {current_step + 1}, y = {next_y}, x = {next_x}')
        #if we will find solution then return true and end this for loop
        if dfs_knight_tour(next_y, next_x, current_step + 1, board, backtrack_count, solution):
            return True
        #if we won't find solution then go one move back "Backtrack" and try next move from the list valid_moves_with_counts
        board[next_y][next_x] = -1
        backtrack_count[0] += 1
        #print(f"Backtracking to ({x}, {y}), backtrack count: {backtrack_count[0]}")

    return False

board = [[-1 for _ in range(8)] for _ in range(8)]
board[0][0] = 0 # start point 0,0
board[2][1] = 63 # last step
board[1][2] = 1  # first step

backtrack_count = [0]

os.system('cls')

x = int(input('Podaj współrzędną startu x: '))
y = int(input('Podaj współrzędną startu y: '))

if not dfs_knight_tour(1, 2, 1, board, backtrack_count, solution):
    print("\nNo closed tour found.")
else:
    print('\nSolution found and saved:')

solution = change_solution_start_point(solution, y, x)
print_board(solution)