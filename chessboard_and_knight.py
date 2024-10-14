# Task 3
# https://medium.com/@davidlfliang/intro-python-algorithms-knights-tour-problem-closed-tour-edition-7d3258785db1

def print_board(board):
    for row in board:
        print(" ".join(f"[{str(cell).replace('-1',' '):2}]" for cell in row))
    print()

board = [[-1 for _ in range(8)] for _ in range(8)]
board[0][0] = 0
board[2][1] = 63
board[1][2] = 1

backtrack_count = [0]
print_board(board)
