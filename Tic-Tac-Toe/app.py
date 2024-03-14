import os

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def check_win(player):
    if (
        board[0] == board[1] == board[2] == player
        or board[3] == board[4] == board[5] == player
        or board[6] == board[7] == board[8] == player
    ):
        return True

    elif (
        board[0] == board[3] == board[6] == player
        or board[1] == board[4] == board[7] == player
        or board[2] == board[5] == board[8] == player
    ):
        return True

    elif (
        board[0] == board[4] == board[8] == player
        or board[2] == board[4] == board[6] == player
    ):
        return True

    else:
        return False


def check_draw():
    if "-" not in board:
        return True
    return False


def check_valid_move(move):
    return True if move in range(1, 10) and board[move - 1] == "-" else False


def player_move(player):
    while True:
        move = input("Enter a number between 1 and 9: ")

        if move.isdigit() and check_valid_move(int(move)):
            board[int(move) - 1] = player
            break
        else:
            os.system("clear")
            print_board()
            print("Invalid move. Try again.")


def print_board():
    os.system("clear")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def play_game():
    current_player = "X"
    while True:
        print_board()
        print(f"Player {current_player} turn!")
        player_move(current_player)

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            return
        elif check_draw():
            print_board()
            print("Draw!")
            return

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
