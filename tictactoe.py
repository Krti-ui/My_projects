def game_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}\n"
          f"-----------\n"
          f" {board[3]} | {board[4]} | {board[5]}\n"
          f"-----------\n"
          f" {board[6]} | {board[7]} | {board[8]}")

def player_input(player_symbol):
    while True:
        try:
            value = int(input(f"Player {player_symbol}, enter a number between 0-8: "))
            if 0 <= value <= 8 and board[value] == " ":
                return value
            else:
                print("Invalid choice. Spot already taken or out of range.")
        except ValueError:
            print("Enter a valid number between 0 and 8.")

def check_draw(board):
    return " " not in board

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def play_game():
    print("Let's play Tic-Tac-Toe!")
    global board
    board = [" "] * 9
    game_board(board)
    current_player = "X"
    game_over = False

    while not game_over:
        choice = player_input(current_player)
        board[choice] = current_player
        game_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
