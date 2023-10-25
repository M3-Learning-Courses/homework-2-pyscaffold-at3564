# This code was mostly generated using ChatGPT GPT-3.5

class TicTacToe:
    """this contains necessary subroutines to play a game of tic-tac-toe on the computer
    """
    def __init__(self):
        """initialize the game with the tic-tac-toe board and starting player
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        """creates a tic-tac-toe board which is a 3x3 square; only internal lines showed
        """
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def take_input(self, position):
        """taking values from each player on where to put a mark on the board

        Args:
            position (integer): a number from 1-9 with each number corresponding to a specific location on the board

        Raises:
            ValueError: integer input not in the specified range of 1 to 9, inclusive

        Returns:
            boolean: true if successfully placed a marking on the board, else false and continues to ask for an input
        """
        try:
            if not (1 <= int(position) <= 9) or not (float(position) % 1 == 0) or not str(position).isdigit(): # hard-coding input restrictions 
                raise ValueError("Position should be an integer between 1 and 9.")
        except ValueError as e:
            print(f"Error: {e}")
            return False

        position = int(position)
        row, col = divmod(position - 1, 3)
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            print("That position is already taken! Please choose an empty position.")
            return False

    def switch_player(self):
        """switches between player 'X' and player 'O'
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        """checks if the board has the same markings of some player that is 3 in a row, 3 in a column, or along the diagonal

        Returns:
            boolean: true if a player won, false otherwise
        """
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':     # checking if a player has 3 in a single row
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':     # checking if a player has 3 in a column
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':         # checking if a player has 3 across a diagonal from top left to bottom right
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':         # checking if a player has 3 across a diagonal from top right to bottom left
            return True
        return False

    def is_board_full(self):
        """checks if all allowable spaces on the board is filled

        Returns:
            boolean: false if at least one free space (as ' ') exists, else true
        """
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def reset_board(self):
        """resets the board to initial condition as in __init__
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def play_game(self):
        """combines subroutines and plays the game
        """
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()                  # prints a tic-tac-toe board
        while True:
            try:
                position = input(f"Player {self.current_player}, enter the position (1-9) or 'exit' to quit: ")
                if position.lower() == 'exit':
                    print("Exiting the game.")
                    break

                if self.take_input(position):   # if the position taken is acceptable, returns true and prints a new board with the player's marking
                    self.print_board()

                    if self.check_winner():     # checks if any winning conditions are met
                        print(f"Player {self.current_player} wins!")
                        self.reset_board()
                        break

                    if self.is_board_full():    
                        print("It's a tie!")
                        self.reset_board()
                        break

                    self.switch_player()        # switches between players
                else:
                    pass 

            except (KeyboardInterrupt, EOFError):
                print("\nGame interrupted. Exiting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
