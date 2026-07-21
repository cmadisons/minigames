import random

SIZE = 4      # board is SIZE x SIZE (set by the player at game start)
NEED = 3      # how many in a row are needed to win


def build_win_lines():
    """All winning lines: every run of NEED consecutive cells in any direction."""
    lines = []
    directions = ((0, 1), (1, 0), (1, 1), (1, -1))  # right, down, down-right, down-left
    for row in range(SIZE):
        for col in range(SIZE):
            for dr, dc in directions:
                end_r, end_c = row + dr * (NEED - 1), col + dc * (NEED - 1)
                if 0 <= end_r < SIZE and 0 <= end_c < SIZE:
                    lines.append(tuple((row + dr * i) * SIZE + (col + dc * i) for i in range(NEED)))
    return tuple(lines)


WIN_LINES = build_win_lines()


def print_board(board):
    print()
    width = len(str(SIZE * SIZE))
    for row in range(SIZE):
        cells = []
        for col in range(SIZE):
            cell = board[row * SIZE + col]
            cells.append(cell.center(width) if cell != " " else str(row * SIZE + col + 1).rjust(width))
        print(" " + " | ".join(cells))
        if row < SIZE - 1:
            print("-" * (len(cells) * (width + 3) - 1))
    print()


def winner(board):
    for line in WIN_LINES:
        first = board[line[0]]
        if first != " " and all(board[i] == first for i in line):
            return first
    return None


def get_move(board, player):
    total = SIZE * SIZE
    while True:
        raw = input(f"Player {player}, pick a square (1-{total}, or 'q' to quit): ").strip().lower()

        if raw in ("q", "quit", "exit"):
            return None

        if not raw.isdigit() or not 1 <= int(raw) <= total:
            print(f"Please enter a number from 1 to {total}.")
            continue

        index = int(raw) - 1
        if board[index] != " ":
            print("That square is already taken. Try again.")
            continue

        return index


def ask_board_size():
    while True:
        raw = input(f"Choose a board size (3-12, default {SIZE}): ").strip()
        if raw == "":
            return SIZE
        if raw.isdigit() and 3 <= int(raw) <= 12:
            return int(raw)
        print("Please enter a number from 3 to 12.")


def main():
    global SIZE, WIN_LINES

    print("Let's play Tic-Tac-Toe!")
    SIZE = ask_board_size()
    WIN_LINES = build_win_lines()

    total = SIZE * SIZE
    board = [" "] * total
    cursed = random.randrange(total)  # hidden trap: land here and you lose
    player = "X"

    print(f"Board is {SIZE}x{SIZE}. Get {NEED} in a row to win.")
    print("Beware: one hidden square is cursed. Land on it and you lose!")

    for _ in range(total):
        print_board(board)

        index = get_move(board, player)
        if index is None:
            print("Thanks for playing!")
            return

        board[index] = player

        if index == cursed:
            board[index] = "*"
            print_board(board)
            other = "O" if player == "X" else "X"
            print(f"Player {player} hit the cursed square (*)! Player {other} wins!")
            return

        won = winner(board)
        if won:
            print_board(board)
            print(f"Player {won} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    main()
