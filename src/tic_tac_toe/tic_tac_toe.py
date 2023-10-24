# This code was generated using ChatGPT GPT-3.5
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def take_input(self, position):
        try:
            position = int(position)
            if not (1 <= position <= 9):
                raise ValueError("Position should be a number between 1 and 9.")
        except ValueError as e:
            print(f"Error: {e}")
            return False

        row, col = divmod(position - 1, 3)
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            print("That position is already taken! Please choose an empty position.")
            return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()
        while True:
            try:
                position = input(f"Player {self.current_player}, enter the position (1-9) or 'exit' to quit: ")
                if position.lower() == 'exit':
                    print("Exiting the game.")
                    break

                if self.take_input(position):
                    self.print_board()

                    if self.check_winner():
                        print(f"Player {self.current_player} wins!")
                        self.reset_board()
                        break

                    if self.is_board_full():
                        print("It's a tie!")
                        self.reset_board()
                        break

                    self.switch_player()
                else:
                    pass  # Handle the case when the position is already taken or invalid

            except (KeyboardInterrupt, EOFError):
                print("\nGame interrupted. Exiting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
