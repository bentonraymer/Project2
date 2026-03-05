import numpy as np

# Settings
algorithm = "ab" # ab for alpha-beta, mcts_r for monte carlo tree search random, mcts_s for monte carlo tree search smart

# Color codes
yellow = '\033[93m'
red = '\033[91m'
white = '\033[0m'

# Set up blank board
board = np.zeros((6, 7), dtype=int)

# Function for adding piece to board
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

# Function for a human move
def human_move(board):
    good_move = False
    while not good_move:
        col = int(input("Human: Enter column (0-6): "))
        if add_piece(board, col, 1):
            good_move = True
        else:
            print("ERROR: Column is full")

# Function for an AI move
def ai_move(board):
    if algorithm == "ab":
        # Call alpha-beta pruning function here
        best_score = float('-inf')
        best_col = None
        for col in range(7):
            temp_board = board.copy()
            if add_piece(temp_board, col, 2):
                score = alpha_beta(temp_board, 0, float('-inf'), float('inf'), False)
                if score > best_score:
                    best_score = score
                    best_col = col
        add_piece(board, best_col, 2)
    elif algorithm == "mcts_r":
        # Call monte carlo tree search function here
        pass
    elif algorithm == "mcts_s":
        # Call smart monte carlo tree search function here
        pass

# Alpha-Beta Pruning Algorithm
def alpha_beta(board, depth, alpha, beta, player):
    MAX_DEPTH = 5
    # When to end
    # Human win
    if check_win(board, 1):
        return -1000 + depth
    # AI Win
    elif check_win(board, 2):
        return 1000 - depth
    # Draw state
    elif np.all(board != 0):
        return 0
    # Max depth reached
    elif depth >= MAX_DEPTH:
        return evaluate_board(board)

    # Evaluate for AI
    if player == 2:
        max_eval = float('-inf')
        for col in range(7):
            for row in range(5, -1, -1):
                if board[row][col] == 0:
                    board[row][col] = 2  # AI move
                    eval = alpha_beta(board, depth + 1, alpha, beta, 1)
                    board[row][col] = 0  # Undo move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    break
            if beta <= alpha:
                break
        return max_eval
    # Evaluate for Human
    else:
        min_eval = float('inf')
        for col in range(7):
            for row in range(5, -1, -1):
                if board[row][col] == 0:
                    board[row][col] = 1  # Human move
                    eval = alpha_beta(board, depth + 1, alpha, beta, 2)
                    board[row][col] = 0  # Undo move
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    break
            if beta <= alpha:
                break
        return min_eval

# Board evaluation function
def evaluate_board(board):
    score = 0
    ROWS, COLS = board.shape

    # Prioritize center columns for strategy
    center_array = board[:, COLS//2]
    center_count = np.count_nonzero(center_array == 2)
    score += center_count * 3

    # Scan for potential winning groups
    def score_window(window, player):
        opp = 1 if player == 2 else 2
        if np.count_nonzero(window == player) == 4:
            return 100
        elif np.count_nonzero(window == player) == 3 and np.count_nonzero(window == 0) == 1:
            return 5
        elif np.count_nonzero(window == player) == 2 and np.count_nonzero(window == 0) == 2:
            return 2
        elif np.count_nonzero(window == opp) == 3 and np.count_nonzero(window == 0) == 1:
            return -4
        return 0

    # Evaluate each possible window of 4
    # Horizontal
    for row in range(ROWS):
        for col in range(COLS-3):
            window = board[row, col:col+4]
            score += score_window(window, 2)
    # Vertical
    for col in range(COLS):
        for row in range(ROWS-3):
            window = board[row:row+4, col]
            score += score_window(window, 2)
    # Diagonal (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS-3):
            window = [board[row-i][col+i] for i in range(4)]
            score += score_window(np.array(window), 2)
    # Diagonal (bottom-right to top-left)
    for row in range(ROWS-3):
        for col in range(COLS-3):
            window = [board[row+i][col+i] for i in range(4)]
            score += score_window(np.array(window), 2)
    return score


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