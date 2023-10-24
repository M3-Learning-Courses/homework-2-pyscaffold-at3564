# This code was generated using ChatGPT GPT-3.5

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False



def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def take_input(player, board, input_func=input):
    while True:
        try:
            position = int(input_func(f"Player {player}, enter the position (1-9): "))
            if not (1 <= position <= 9):
                print("Position should be a number between 1 and 9. Please try again.")
                continue

            row = (position - 1) // 3
            col = (position - 1) % 3

            if board[row][col] != " ":
                print("That position is already taken! Please choose an empty position.")
            else:
                return row, col
        except ValueError:
            print("Invalid input! Please enter a number.")



def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            row, col = take_input(players[current_player], board)
            board[row][col] = players[current_player]
            print_board(board)

            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break

            if is_board_full(board):
                print("It's a tie!")
                break

            current_player = (current_player + 1) % 2

        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    play_game()
