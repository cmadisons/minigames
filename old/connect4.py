ROWS = 6
COLS = 7
EMPTY = "."


def make_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]


def print_board(board):
    print()
    for row in board:
        print(" " + " ".join(row))
    print(" " + " ".join(str(c + 1) for c in range(COLS)))
    print()


def drop_piece(board, col, piece):
    """Drop a piece into a column. Returns the row it landed in, or None if full."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = piece
            return row
    return None


def is_win(board, row, col, piece):
    directions = ((0, 1), (1, 0), (1, 1), (1, -1))
    for dr, dc in directions:
        count = 1
        # Count in both directions along this axis.
        for sign in (1, -1):
            r, c = row + dr * sign, col + dc * sign
            while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == piece:
                count += 1
                r += dr * sign
                c += dc * sign
        if count >= 4:
            return True
    return False


def board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))


def get_move(board, player):
    while True:
        raw = input(f"Player {player}, pick a column (1-{COLS}, or 'q' to quit): ").strip().lower()

        if raw in ("q", "quit", "exit"):
            return None

        if not raw.isdigit() or not 1 <= int(raw) <= COLS:
            print(f"Please enter a number from 1 to {COLS}.")
            continue

        col = int(raw) - 1
        if board[0][col] != EMPTY:
            print("That column is full. Try another.")
            continue

        return col


def main():
    board = make_board()
    players = ("X", "O")
    turn = 0

    print("Let's play Connect 4!")
    print("Drop pieces into columns. First to connect four in a row wins.")

    while True:
        print_board(board)
        player = players[turn % 2]

        col = get_move(board, player)
        if col is None:
            print("Thanks for playing!")
            return

        row = drop_piece(board, col, player)

        if is_win(board, row, col, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            return

        turn += 1


if __name__ == "__main__":
    main()
