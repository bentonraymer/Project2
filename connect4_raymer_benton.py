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
    won = False
    while not won:
        print_board(board)
        col = int(input("PLAYER ONE: Enter column (0-6): "))
        if add_piece(board, col, 1):
            if check_win(board, 1):
                print("Player 1 wins!")
                won = True
        else:
            print("ERROR: Column is full")
        print_board(board)
        if not won:
            col = int(input("PLAYER TWO:Enter column (0-6): "))
            if add_piece(board, col, 2):
                if check_win(board, 2):
                    print("Player 2 wins!")
                    won = True
            else:
                print("ERROR: Column is full")