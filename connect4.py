def print_board(board):
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print()

def check_win(board, player):
    # Check horizontal
    for row in board:
        for col in range(len(row) - 3):
            if all(cell == player for cell in row[col:col + 4]):
                return True

    # Check vertical
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonal (positive slope)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonal (negative slope)
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

def is_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def main():
    ROWS = 6
    COLS = 7
    board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        column = int(input(f"Player {player}, choose a column (0-6): "))

        # Check if the column is valid and the selected column is not full
        if column < 0 or column >= COLS or board[0][column] != ' ':
            print("Invalid move. Try again.")
            continue

        # Drop the piece
        for i in range(ROWS - 1, -1, -1):
            if board[i][column] == ' ':
                board[i][column] = player
                break

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    main()