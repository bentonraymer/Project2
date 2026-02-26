import numpy as np

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

if __name__ == "__main__":
    add_piece(board, 0, 1)
    print_board(board)