import numpy as np

# Settings
algorithm = "ab" # ab for alpha-beta, mcts for monte carlo tree search

# Color codes
yellow = '\033[93m'
red = '\033[91m'
white = '\033[0m'

# Set up blank board
board = np.zeros((6, 7), dtype=int)

def add_piece(board, col, team):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            board[row][col] = team
            return True
    return False

# Check for win conditions
def check_win(board, team):
    # Horozontal
    for row in range(6):
        for col in range(4):
            if all(board[row][col+i] == team for i in range(4)):
                return True
    # Vertical
    for col in range(7):
        for row in range(3):
            if all(board[row+i][col] == team for i in range(4)):
                return True
    # Diagonal (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if all(board[row-i][col+i] == team for i in range(4)):
                return True
    # Diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if all(board[row+i][col+i] == team for i in range(4)):
                return True
    return False

# Print current status of the board
def print_board(board):
    for row in board:
        for cell in row:
            if cell == 0:
                print(white + '■', end=' ')
            elif cell == 1:
                print(yellow + '■', end=' ')
            else:
                print(red + '■', end=' ')
        print(white)

def human_move(board):
    good_move = False
    while not good_move:
        col = int(input("Human: Enter column (0-6): "))
        if add_piece(board, col, 1):
            good_move = True
        else:
            print("ERROR: Column is full")

def ai_move(board):
    if algorithm == "ab":
        # Call alpha-beta pruning function here
        pass
    elif algorithm == "mcts":
        # Call monte carlo tree search function here
        pass

# Alpha-Beta Pruning Algorithm




if __name__ == "__main__":
    won = False
    while not won:
        print_board(board)
        human_move(board)
        if check_win(board, 1):
            print_board(board)
            print("Human wins!")
            won = True
            break
        ai_move(board)
        if check_win(board, 2):
            print_board(board)
            print("AI wins!")
            won = True